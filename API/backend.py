from flask import Flask, request, jsonify
import datetime
import json
import os
import uuid  # https://docs.python.org/3/library/uuid.html
import structlog  # for event logging
# from dotenv import load_dotenv # enviornment vars if we want
import base64
import bcrypt

from pygtail import Pygtail
import boto3
from minio import Minio
from dotenv import load_dotenv
from datetime import timedelta, date
import time
from time import sleep
from sys import argv
import threading
from smart_open import smart_open
import gensim
import gensim.corpora as corpora
import pandas as pd
import io

# setup to import the preprocessor
import sys
from botocore.errorfactory import ClientError

os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath("Preprocessing.py"))))
from MachineLearningModels.Preprocessing import Preprocessor
preprocessor = Preprocessor(1)

from MachineLearningModels.transformer_predict import TransformerPredict
summarizer = TransformerPredict()

from MachineLearningModels.lda_predict import LDAPredict
lda = LDAPredict()

from MachineLearningModels.transcriber import Transcriber
transcriber = Transcriber()

from MachineLearningModels.question_answerer import QuestionAnswerer
qa = QuestionAnswerer()

from MachineLearningModels.question_generator import QuestionGenerator
qg = QuestionGenerator()

# import psycopg2 # postgres support if we want it

# create the flask app for the rest endpoints
app = Flask(__name__)

# load the environment files
load_dotenv()

# set up the structured logging file for endpoints
with open(os.getenv('ENDPOINT_LOG_PATH'), "wt", encoding="utf-8") as log_fl:
    structlog.configure(
        processors=[structlog.processors.TimeStamper(fmt="iso"),
                    structlog.processors.JSONRenderer()],
        logger_factory=structlog.WriteLoggerFactory(file=log_fl))

# set up the connection to the S3 object store. Login properties are read from the environment file
# going to need to connect to two separate buckets as well. One bucket will be for storing files from the app
# the other bucket will be for storing the log files. It should only be pushed every 15? minutes.
# the timed push will be defined by a command line arg on launch. Needs a separate thread or program.
s3_resource = boto3.resource('s3',
                             endpoint_url=os.getenv('MINIO_URL'),
                             aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                             aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                             aws_session_token=None,
                             config=boto3.session.Config(signature_version='s3v4'),
                             verify=False
                             )

# Set up the currently active session dataframe. This is used to track who is logged into the system and their auth tokens.
auth_df = pd.DataFrame(columns=['username', 'token', 'ts_login', 'ts_last_active'])
# auth_df.loc[len(auth_df)] = ['DoeJ1970', '0', '0', '0'] # dummy user for testing with postman

s3_client = boto3.client('s3',
                         endpoint_url=os.getenv('MINIO_URL'),
                         aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                         aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                         aws_session_token=None,
                         config=boto3.session.Config(signature_version='s3v4'),
                         verify=False
                         )


s3_paginator = s3_client.get_paginator('list_objects_v2')


def keys(bucket_name, prefix='/', delimiter='/', start_after=''):
    # method returns an iterator of all of the keys present in a bucket.
    # https://stackoverflow.com/a/54014862
    prefix = prefix.lstrip(delimiter)
    start_after = (start_after or prefix) if prefix.endswith(delimiter) else start_after
    for page in s3_paginator.paginate(Bucket=bucket_name, Prefix=prefix, StartAfter=start_after):
        for content in page.get('Contents', ()):
            yield content['Key']


# going to need to add instructions on how to set up minio... Launch args: minio server minio_data
def send_to_bucket(body: str, log_name="", bucket_name=os.getenv("USER_FILES_BUCKET")):
    if not log_name:
        log_name = "log_file_%s.json" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    return s3_resource.Bucket(bucket_name).put_object(Key=log_name, Body=body)


def read_from_s3(file_name: str, bucket_name=os.getenv("USER_FILES_BUCKET"), raw=False):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html
    obj = s3_resource.Object(bucket_name=bucket_name, key=file_name)
    response = obj.get()
    data = response['Body'].read()
    # print(data)
    if raw:
        return data
    elif isinstance(data, bytes):
        data = data.decode()
    elif not isinstance(data, str):
        data = str(data)  # https://stackoverflow.com/a/45928164 possible base64 check
    return data


def read_from_s3_iter(file_name: str, bucket_name=os.getenv("USER_FILES_BUCKET")):
    # https://stackoverflow.com/questions/36205481/read-file-content-from-s3-bucket-with-boto3
    bucket = s3_resource.Bucket(bucket_name)
    # Iterates through all the objects, doing the pagination for you. Each obj
    # is an ObjectSummary, so it doesn't contain the body. You'll need to call
    # get to get the whole body.
    found = False
    data = ""
    for obj in bucket.objects.all():
        key = obj.key
        if file_name in str(key):
            data = obj.get()['Body'].read()
            print("%s : %s" % (key, data))
            found = True
    if found:
        return data
    else:
        print("ERROR KEY NOT FOUND")
        return -1


def check_for_file_s3(file_name: str, bucket_name=os.getenv("USER_FILES_BUCKET")):
    # return s3_client.head_object(Bucket=bucket_name, Key=file_name)['ContentLength']
    try:
        return s3_resource.Object(bucket_name, file_name).content_length
    except ClientError:
        return -1


def get_user_login_records(file_keys: list) -> pd.DataFrame:
    user_login_records = pd.DataFrame(columns=['ip', 'os', 'browser', 'device', 'location', 'ts'])
    for key in file_keys:
        file_data = json.loads(read_from_s3(file_name=key, bucket_name=os.getenv('LOGIN_TRACKING_BUCKET')))
        r = {"ip": file_data['ip'], "os": file_data['os'], "browser": file_data['browser'],
             "device": file_data['device'], "location": file_data['location'], "ts": file_data['ts']}
        user_login_records = pd.concat([user_login_records, pd.DataFrame.from_records([r])]).reset_index(drop=True)
    user_login_records = user_login_records.sort_values(by='ts', ascending=True)
    return user_login_records


def get_user_login_records_keys(username: str, n: int) -> pd.DataFrame:
    user_login_records_keys = pd.DataFrame(columns=['key', 'ts'])
    if n == 0:
        return user_login_records_keys
    for key in keys(os.getenv('LOGIN_TRACKING_BUCKET'), prefix=username, delimiter='_'):
        r = {"key": key, "ts": int(key.removeprefix(username + "_").removesuffix(".json"))}
        user_login_records_keys = pd.concat([user_login_records_keys, pd.DataFrame.from_records([r])]).reset_index(
            drop=True)
    user_login_records_keys = user_login_records_keys.sort_values(by='ts', ascending=True)
    if len(user_login_records_keys.index) > n > 0:
        user_login_records_keys = user_login_records_keys.tail(n)
    print(user_login_records_keys)  # FIXME
    return user_login_records_keys


def logout_inactive():
    global auth_df
    epoch = datetime.datetime.utcfromtimestamp(0)
    diff = datetime.datetime.utcnow() - datetime.timedelta(minutes=int(os.getenv('INACTIVE_LOGOUT_INTERVAL_MINUTES')))
    diff = int((diff - epoch).total_seconds() * 1000.0)
    # print(diff)
    print("Logging out %d users" % len(auth_df[auth_df['ts_last_active'] <= diff]))
    auth_df = auth_df[auth_df['ts_last_active'] > diff]


def run_periodic_logger():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    while True:
        start = datetime.datetime.now()
        until = start + timedelta(minutes=int(os.getenv('LOGGING_INTERVAL_MINUTES')))
        while datetime.datetime.now() < until:
            sleep(1)
        logout_inactive()
        tail = Pygtail(os.getenv('ENDPOINT_LOG_PATH'), save_on_end=True, copytruncate=False)
        temp_str = ""
        for line, offset in tail.with_offsets():
            j = json.loads(line)
            temp_str += json.dumps(j) + "\n"
            temp_str = temp_str.replace("\\u", "/u")
        if temp_str:
            print("Sending data to MINIO of length %d" % (len(temp_str)))
            send_to_bucket(body=temp_str, bucket_name=os.getenv("ENDPOINT_LOGS_BUCKET"))


def run_flask():
    with open(os.getenv('ENDPOINT_LOG_PATH'), "wt", encoding="utf-8") as log_fl:
        structlog.configure(
            processors=[structlog.processors.TimeStamper(fmt="iso"),
                        structlog.processors.JSONRenderer()],
            logger_factory=structlog.WriteLoggerFactory(file=log_fl))
        app.run(debug=True, port=8844, host='0.0.0.0', use_reloader=False)  # Added host= so I can access from devices on same network


def get_unix_time_millis():
    epoch = datetime.datetime.utcfromtimestamp(0)
    now = datetime.datetime.utcnow()
    return int((now - epoch).total_seconds() * 1000.0)


def encode_password(s: str) -> str:
    # https://www.makeuseof.com/encrypt-password-in-python-bcrypt/
    password = s.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    hashed = hashed.decode('utf-8')
    return hashed


def check_password_hash(s: str, hashed: str) -> bool:
    # https://www.makeuseof.com/encrypt-password-in-python-bcrypt/
    hashed = hashed.encode('utf-8')
    password = s.encode('utf-8')
    return bcrypt.checkpw(password, hashed)


def receive(main_topic: str, sub_topic: str, request):
    logger = structlog.get_logger()
    print(request.data)
    data = json.loads(request.data.decode('utf-8'))
    timestamp = data['ts']
    cId = data['cId']
    payload = data['p'] if 'p' in data else {}
    if main_topic != "auth":
        username = data['username']
        token = data['token']
        logger.info(event="fb::" + main_topic + "::" + sub_topic, direction="fb", main_topic=main_topic,
                    sub_topic=sub_topic, ts=timestamp, cId=cId, username=username, token=token, payload=payload)
        validation = validate_session(username, token)
        validation_code = validation['error_code']
        validation_msg = validation['error_msg']
    else:
        # do not log payload under the auth topics as it contains confidential user information.
        logger.info(event="fb::" + main_topic + "::" + sub_topic, direction="fb", main_topic=main_topic,
                    sub_topic=sub_topic, ts=timestamp, cId=cId)
        validation_code = 0
        validation_msg = ""
        username = ""
    return cId, payload, username, validation_code, validation_msg


def respond(main_topic: str, cId: str, payload: dict, error_code: int, error_msg: str):
    # this method builds the response message, logs it, and then returns it as a json dict.
    logger = structlog.get_logger()
    timestamp = get_unix_time_millis()
    response = {"ts": timestamp, "cId": cId, "err": {"code": error_code, "msg": error_msg}, "p": payload}
    if error_code != 0:
        logger.warn(event="bf::" + main_topic + "::" + cId, main_topic=main_topic, ts=timestamp, cId=cId,
                    error_code=error_code, error_msg=error_msg, payload=payload)
    else:
        logger.info(event="bf::" + main_topic + "::" + cId, main_topic=main_topic, ts=timestamp, cId=cId,
                    error_code=error_code, error_msg=error_msg, payload=payload)
    return response


def validate_session(username: str, token: str) -> dict:
    global auth_df
    # method to validate that the specified session exists
    user = auth_df.loc[auth_df['username'] == username]
    active_sessions = len(user.index)
    if active_sessions == 0:
        # user is not logged in
        return {"error_code": 22, "error_msg": "The specified user does not currently have any sessions in " +
                                               "the system. This means they are not logged in anywhere.",
                "active_sessions": active_sessions}
    elif len(user.loc[user['token'] == token].index) == 0:
        # token is not valid
        return {"error_code": 23, "error_msg": "The specified token is not valid for the specified user. " +
                                               "This means you are not authenticated. Please sign out and sign back in before trying again.",
                "active_sessions": active_sessions}
    else:
        # session is valid. Update the timestamp associated with that token as well.
        auth_df['ts_last_active'] = auth_df.apply(lambda x: get_unix_time_millis() if str(x['token']) == str(token) else x['ts_last_active'], axis=1)
        return {"error_code": 0, "error_msg": "", "active_sessions": active_sessions}

@app.after_request
def apply_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response

# Another helper func to add CORS headers
def prepare_response(res_object, status_code):
    response = jsonify(res_object)
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    # response.headers.set('Access-Control-Allow-Credentials', 'true')
    response.headers.set('Access-Control-Allow-Headers', 'Access-Control-Allow-Headers, Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers')
    return response, status_code


# region AUTHENTICATION TOPICS

@app.route('/fb/auth/new', methods=['GET', 'POST'])
def get_new_user():
    # parse the message to extract the components
    cId, p, _, _, _ = receive("auth", "new", request)
    username = p['username']
    password = p['password']
    # check if the username is already taken by checking against the bucket keys.
    if -1 == check_for_file_s3(username, bucket_name=os.getenv('ACCOUNT_INFO_BUCKET')):
        # username does not exist yet. Good to create the new user
        password = encode_password(password)
        information = {"email": p['email'], "password": password, "birthday": p['birthday'],
                       "org": p['org'], "first": p['first'], "last": p['last'], "gender": p['gender'],
                       "phone": p['phone'], "job": p['job'], "max_concurrent": 2, "created": get_unix_time_millis()}
        information = json.dumps(information)
        send_to_bucket(information, log_name=username, bucket_name=os.getenv('ACCOUNT_INFO_BUCKET'))
        # return a response. Redirect to the login page so new account can try to login right away.
        payload = {"username": username, "redirect": "login.ts"}
        resp = respond("auth", cId, payload, error_code=0, error_msg="")
        return json.dumps(resp)
    else:
        resp = respond("auth", cId, payload={}, error_code=15, error_msg="The specified user could not be generated. "
                                                                         "Username already taken.")
        return prepare_response(json.dumps(resp), 200)


@app.route('/fb/auth/in', methods=['GET', 'POST'])
def get_user_login():
    global auth_df
    # parse the message to extract the components
    cId, p, _, _, _ = receive("auth", "in", request)
    username = p['username']
    password = p['password']
    redirect = p['redirect']
    # first check if the username is valid by comparing against S3
    if -1 == check_for_file_s3(username, bucket_name=os.getenv('ACCOUNT_INFO_BUCKET')):
        resp = respond("auth", cId, payload={}, error_code=10, error_msg="No account with the specified username was "
                                                                         "found in the system.")
        return prepare_response(json.dumps(resp), 200)
    else:
        # need to read the username file now from S3 to compare the password
        file_data = read_from_s3(file_name=username, bucket_name=os.getenv('ACCOUNT_INFO_BUCKET'))
        file_data = json.loads(file_data)
        # the file_data['password'] field should contain the hashed password setup in the sign-up endpoint.
        if not check_password_hash(password, str(file_data['password'])):
            resp = respond("auth", cId, payload={}, error_code=26,
                           error_msg="The username or password did not match")
            return prepare_response(json.dumps(resp), 200)
        else:
            # username and password both match. Now check how many concurrent sessions are allowed and are active.
            user = auth_df.loc[auth_df['username'] == username]
            active_sessions = len(user.index)
            max_concurrent_sessions = int(file_data['max_concurrent'])
            if active_sessions < max_concurrent_sessions:
                # Generate token and log the login.
                token = str(uuid.uuid4())
                timestamp = get_unix_time_millis()
                auth_df = pd.concat([auth_df, pd.DataFrame.from_records([{"username": username,
                                                                          "token": token,
                                                                          "ts_login": timestamp,
                                                                          "ts_last_active": timestamp}])]).reset_index(drop=True)
                print(auth_df)  # FIXME
                # build the data to log to MINIO
                # the log message is built here so that we only log successful logins.
                log_payload = {"ip": p['ip'], "os": p['os'], "browser": p['browser'], "device": p['device'],
                               "location": p['location'], "username": username, 'ts': timestamp}
                log_name = "%s_%s.json" % (username, timestamp)
                send_to_bucket(json.dumps(log_payload), log_name=log_name, bucket_name=os.getenv(
                    'LOGIN_TRACKING_BUCKET'))
                # return a response
                payload = {"token": token, "username": username, "redirect": redirect}
                resp = respond("auth", cId, payload, error_code=0, error_msg="")
                return json.dumps(resp)
            else:
                resp = respond("auth", cId, payload={}, error_code=25, error_msg="Login failed. The specified account "
                                                                                 "already has the maximum number of "
                                                                                 "concurrent sessions active.")
                return prepare_response(json.dumps(resp), 200)


@app.route('/fb/auth/out', methods=['GET', 'POST'])
def get_user_logout():
    global auth_df
    # parse the message to extract the components
    cId, p, _, _, _ = receive("auth", "out", request)
    username = p['username']
    token = p['token']
    logout_all = p['all']
    validation = validate_session(username, token)
    validation_code = validation['error_code']
    validation_msg = validation['error_msg']
    if validation_code != 0:
        # failed validation.
        count = 0
    elif logout_all:
        auth_df = auth_df[auth_df['username'] != username]
        count = validation['active_sessions']
    else:
        auth_df = auth_df[auth_df['token'] != token]
        count = 1
    payload = {"username": username, "count": count}
    resp = respond("auth", cId, payload, error_code=validation_code, error_msg=validation_msg)
    print(auth_df)  # FIXME
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/auth/exchange', methods=['GET', 'POST'])
def get_password_reset():
    cId, p, _, _, _ = receive("auth", "exchange", request)
    # uid = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org'))
    # payload = {}
    # payload['username'] = "DoeJ1970"
    # resp = generate_response(uid, payload)
    # logger = structlog.get_logger()
    # logger.info(event='fb::auth::new', uuid=uid)
    return {"status": 501}


# endregion


# region ACCOUNT INFORMATION TOPICS

@app.route('/fb/acc/list', methods=['GET', 'POST'])
def get_device_history():
    cId, p, username, validation_code, validation_msg = receive("acc", "list", request)
    n = p['num']
    if validation_code != 0:
        # failed validation
        payload = {}
    else:
        list_of_keys = list(get_user_login_records_keys(username, n)['key'])
        records = get_user_login_records(list_of_keys).to_json(orient='records')
        payload = {"username": username, "list": json.loads(records)}
    resp = respond("auth", cId, payload, error_code=validation_code, error_msg=validation_msg)
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/acc/clear', methods=['GET', 'POST'])
def get_clear_device_history():
    cId, p, username, validation_code, validation_msg = receive("acc", "clear", request)
    n = p['num']
    if validation_code != 0:
        # failed validation
        payload = {}
    else:
        count = 0
        for key in get_user_login_records_keys(username, n)['key']:
            s3_client.delete_object(Bucket=os.getenv('LOGIN_TRACKING_BUCKET'), Key=key)
            count += 1
        payload = {"num": count}
    resp = respond("auth", cId, payload, error_code=validation_code, error_msg=validation_msg)
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/acc/connected', methods=['GET', 'POST'])
def get_concurrent_users():
    global auth_df
    cId, p, username, validation_code, validation_msg = receive("acc", "connected", request)
    if validation_code != 0:
        # failed validation
        payload = {}
    else:
        user = auth_df.loc[auth_df['username'] == username]  # dataframe of all active user sessions
        user_login_records_keys = get_user_login_records_keys(username, n=-1) # dataframe of records and times of logins
        user_login_records_keys = user_login_records_keys[user_login_records_keys['ts'].isin(list(user['ts_login']))]
        list_of_keys = list(user_login_records_keys['key'])
        records = get_user_login_records(list_of_keys).to_json(orient='records')
        payload = {"username": username, "list": json.loads(records)}
    resp = respond("auth", cId, payload, error_code=validation_code, error_msg=validation_msg)
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/acc/max', methods=['GET', 'POST'])
def get_set_max_concurrent():
    cId, p, username, validation_code, validation_msg = receive("acc", "max", request)
    n = int(p['max'])
    n = n if 0 < n <= 8 else 2
    if validation_code != 0:
        # failed validation
        payload = {}
    else:
        file_data = json.loads(read_from_s3(file_name=username, bucket_name=os.getenv('ACCOUNT_INFO_BUCKET')))
        file_data['max_concurrent'] = n
        file_data = json.dumps(file_data)
        send_to_bucket(file_data, log_name=username, bucket_name=os.getenv('ACCOUNT_INFO_BUCKET'))
        payload = {"username": username, "max": n}
    resp = respond("auth", cId, payload, error_code=validation_code, error_msg=validation_msg)
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/acc/info', methods=['GET', 'POST'])
def get_stored_user_info():
    cId, p, username, validation_code, validation_msg = receive("acc", "info", request)
    if validation_code != 0:
        # failed validation
        payload = {}
    else:
        # grab account information
        file_data = json.loads(read_from_s3(file_name=username, bucket_name=os.getenv('ACCOUNT_INFO_BUCKET')))
        # grab login information
        list_of_keys = list(get_user_login_records_keys(username, n=-1)['key'])
        records = get_user_login_records(list_of_keys)
        # get number of files
        list_of_files = list(keys(os.getenv('USER_FILES_BUCKET'), prefix=username))
        n_files = len(list_of_files)
        # get storage space used
        storage_used = 0
        for key in list_of_files:
            storage_used += check_for_file_s3(key)
        # date calculations
        created = file_data['created']
        now = get_unix_time_millis()
        s, ms = divmod(created, 1000) # https://stackoverflow.com/a/21787689
        created = datetime.datetime.fromtimestamp(s)
        s, ms = divmod(now, 1000)  # https://stackoverflow.com/a/21787689
        now = datetime.datetime.fromtimestamp(s)
        days = (now - created).days
        # parse information
        payload = {"email": file_data['email'], "birthday": file_data['birthday'], "org": file_data['org'],
                   "first": file_data['first'], "last": file_data['last'], "gender": file_data['gender'],
                   "phone": file_data['phone'], "job": file_data['job'], "nUniqueIP": records['ip'].nunique(),
                   "nUniqueOS": records['os'].nunique(), "nUniqueBrowser": records['browser'].nunique(),
                   "nUniqueLocation": records['location'].nunique(), "nStoredFiles": n_files, "StorageSize": storage_used,
                   "CreationDate": created, "days": days}
    resp = respond("auth", cId, payload, error_code=validation_code, error_msg=validation_msg)
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/acc/delete', methods=['GET', 'POST'])
def get_user_delete():
    global auth_df
    cId, p, username, validation_code, validation_msg = receive("acc", "delete", request)
    if validation_code != 0:
        # failed validation
        payload = {}
    else:
        # needs to delete the username file in the ACCOUNT_INFO_BUCKET
        # needs to delete all login files in LOGIN_TRACKING_BUCKET
        # needs to delete all files with the username prefix in USER_FILES_BUCKET
        # needs to remove user info from the login auth_df
        auth_df = auth_df[auth_df['username'] != username]
        # should probably delete data from the endpoint logs? may be fine since we do not log any account information there
        s3_client.delete_object(Bucket=os.getenv('ACCOUNT_INFO_BUCKET'), Key=username)
        n_login_logs = 0
        for key in get_user_login_records_keys(username, n=-1)['key']:
            s3_client.delete_object(Bucket=os.getenv('LOGIN_TRACKING_BUCKET'), Key=key)
            n_login_logs += 1
        n_user_files = 0
        for key in keys(os.getenv('USER_FILES_BUCKET'), prefix=username):
            s3_client.delete_object(Bucket=os.getenv('USER_FILES_BUCKET'), Key=key)
            n_user_files += 1
        payload = {"username": username, "n_login_logs": n_login_logs, "n_user_files": n_user_files,
                   "redirect": "goodbye"}
    resp = respond("auth", cId, payload, error_code=validation_code, error_msg=validation_msg)
    return prepare_response(json.dumps(resp), 200)


# endregion

# region FILE MANAGEMENT TOPICS

@app.route('/fb/file/up', methods=['GET', 'POST'])
def get_upload_files():
    cId, p, username, validation_code, validation_msg = receive("file", "up", request)
    
    if validation_code != 0:
        # failed validation
        return respond("file", cId, {}, error_code=validation_code, error_msg=validation_msg)    
    
    files = p["files"]
    err_info = [] # used to collect files names that fail to upload
    payload = {}
    payload['success'] = []
    for file in files:
        try:
            location = username + "/" + file['path']
            if (not file['overwrite'] and check_for_file_s3(location) < 0) or file['overwrite']:
                filename, extension = os.path.splitext(os.path.basename(file['path']))
                if(extension not in ['.txt','.vtt']): # raw bytes files will come base64 encoded, this is so they could be utf encoded + json serialized before sending
                    send_to_bucket(body=base64.b64decode(file['data'].encode('utf')), log_name=location)
                else:
                    formatted_data = {
                        "filename" : filename,
                        "original_extension" : extension[1:],
                        "processed" : file['preprocess'],
                        "text" : preprocessor.vtt_to_txt(file['data']) if extension == '.vvt' else file['data']
                    }
                    json_str = json.dumps(formatted_data)
                    encoded_data = base64.b64encode(json_str.encode('ascii'))
                    send_to_bucket(body=encoded_data, log_name=location)
                payload['success'].append({
                    "path" : file['path'],
                    "size" : len(file['data']),
                    "processed" : file['preprocess']
                })
            else:
                err_info.append(file['path'])
        except Exception as e:
            err_info.append(file['path'])
            
    resp = respond("file", cId, payload, error_code=0, error_msg="")
    if len(err_info) > 0:
        info = []
        for filepath in err_info:
            info.append({
                "path" : filepath
            })
        resp['err']['code'] = 24
        resp['err']['msg'] = f"The upload operation failed for {len(err_info)} files."
        resp['err']['info'] = info
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/file/down', methods=['GET', 'POST'])
def get_download_files():
    cId, p, username, validation_code, validation_msg = receive("file", "down", request)
    
    if validation_code != 0:
        # failed validation
        resp = respond("file", cId, {}, error_code=validation_code, error_msg=validation_msg)
        return prepare_response(json.dumps(resp), 200)

    
    files = p["files"]
    err_info = [] # used to collect files that fail to download
    payload = {}
    payload['success'] = []
    result = None
    for file in files:
        location = username + "/" + file['path']
        if check_for_file_s3(location) >= 0: 
            try:
                file_content = read_from_s3(file_name=location)
                formatted_data = json.loads(base64.b64decode(file_content.encode('ascii')))
                payload['success'].append({
                    "path" : file['path'],
                    "data" : formatted_data
                })
            except Exception as e:
                err_info.append(file['path'])
            
    resp = respond("file", cId, payload, error_code=0, error_msg="")
    if len(err_info) > 0:
        info = []
        for filepath in err_info:
            info.append({
                "path" : filepath
            })
        resp['err']['code'] = 13
        resp['err']['msg'] = f"The download operation failed for {len(err_info)} files."
        resp['err']['info'] = info
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/file/space', methods=['GET', 'POST'])
def get_storage_size():
    cId, p, username, validation_code, validation_msg = receive("file", "space", request)
    
    if validation_code != 0:
        # failed validation
        resp = respond("file", cId, {}, error_code=validation_code, error_msg=validation_msg)
        return prepare_response(json.dumps(resp), 200)


    used = 0
    for key in keys(os.getenv('USER_FILES_BUCKET'), prefix=username):
        used += check_for_file_s3(key)

    payload = {
        "used": used,
        "total": 256000000
    }
    resp = respond("file", cId, payload, error_code=0, error_msg="")
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/file/list', methods=['GET', 'POST'])
def get_directory_info():
    cId, p, username, validation_code, validation_msg = receive("file", "list", request)
    
    if validation_code != 0:
        # failed validation
        resp = respond("file", cId, {}, error_code=validation_code, error_msg=validation_msg)
        return prepare_response(json.dumps(resp), 200)

    
    payload = {}
    payload['files'] = []
    
    for key in keys(os.getenv('USER_FILES_BUCKET'), prefix=username):
        payload['files'].append({
            "path" : key,
            "size" : check_for_file_s3(key)
        })
        
    resp = respond("file", cId, payload, error_code=0, error_msg="")
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/file/remove', methods=['GET', 'POST'])
def get_file_removal():
    cId, p, username, validation_code, validation_msg = receive("file", "remove", request)
    
    if validation_code != 0:
        # failed validation
        resp = respond("file", cId, {}, error_code=validation_code, error_msg=validation_msg)
        return prepare_response(json.dumps(resp), 200)

    
    files = p["files"]
    err_info = [] # used to collect files that fail to delete
    payload = {}
    payload['success'] = []
    result = None
    for file in files:
        location = username + "/" + file['path']
        if check_for_file_s3(location) >= 0: 
            try:
                s3_client.delete_object(Bucket=os.getenv("USER_FILES_BUCKET"), Key=location)
                payload['success'].append({
                    "path" : file['path']
                })
            except Exception as e:
                err_info.append(file['path'])
            
    resp = respond("file", cId, payload, error_code=0, error_msg="")
    if len(err_info) > 0:
        info = []
        for filepath in err_info:
            info.append({
                "path" : filepath
            })
        resp['err']['code'] = 14
        resp['err']['msg'] = "File Deletion Failed"
        resp['err']['info'] = info
    return prepare_response(json.dumps(resp), 200)


# endregion

# region DATA PROCESSING TOPICS

# @app.route('/fb/proc/data', methods=['GET', 'POST'])
# def get_file_data():
#     cId, p, username, validation_code, validation_msg = receive("proc", "data", request)
#     file_data = read_from_s3(file_name=p['path'])
#
#     # start building the output response
#     payload = {'data': file_data}
#     resp = respond("auth", cId, payload, error_code=0, error_msg="")
#     return json.dumps(resp)


@app.route('/fb/proc/clean', methods=['GET', 'POST'])
def get_clean_raw():
    cId, p, username, validation_code, validation_msg = receive("proc", "clean", request)
    inplace = p['inplace']
    path = p['path']

    # read in the file data from the path specified
    file_data = read_from_s3(file_name=path)

    # preprocess the file data
    # TODO switch based on extension of file
    acronyms = preprocessor.get_acronyms(file_data)
    # print(acronyms)
    cleaned = preprocessor.clean(file_data)
    # print(cleaned)

    # start building the output response using sample data
    payload = {}
    payload['Acronyms'] = acronyms  # TODO: update api doc
    # payload['Acronyms'].append({})
    # payload['Acronyms'][0]['acronym'] = 'MSOE'
    # payload['Acronyms'][0]['expanded'] = 'Milwaukee School Of Engineering'
    payload['Equations'] = []  # TODO: implement this
    payload['data'] = ' '.join(cleaned)
    if inplace:
        print("sending file %s to MINIO" % path)
        send_to_bucket(payload['data'], log_name=path)
    resp = respond("proc", cId, payload, error_code=0, error_msg="")
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/proc/summary', methods=['GET', 'POST'])
def get_transcript_summary():
    cId, p, username, validation_code, validation_msg = receive("proc", "summary", request)
    
    if validation_code != 0:
        # failed validation
        resp = respond("proc", cId, {}, error_code=validation_code, error_msg=validation_msg)
        return prepare_response(json.dumps(resp), 200)

    
    location = username + "/" + p['path']
    if check_for_file_s3(location) < 0:
        resp = respond("proc", cId, {}, error_code=11, error_msg=f"The specified file at {p['path']} does not exist.")
        return prepare_response(json.dumps(resp), 200)


    file_data = json.loads(base64.b64decode(read_from_s3(location).encode()).decode())['text']
    payload = {}
    payload['data'] = base64.b64encode(summarizer.summarize(file_data).encode()).decode()
    payload['accuracy'] = 0.0
    
    resp = respond("proc", cId, payload, error_code=0, error_msg="")
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/proc/topics', methods=['GET', 'POST'])
def get_transcript_topics():
    cId, p, username, validation_code, validation_msg = receive("proc", "topics", request)
    
    if validation_code != 0:
        # failed validation
        resp = respond("proc", cId, {}, error_code=validation_code, error_msg=validation_msg)
        return prepare_response(json.dumps(resp), 200)

    
    location = username + "/" + p['path']
    if check_for_file_s3(location) < 0:
        resp = respond("proc", cId, {}, error_code=11, error_msg=f"The specified file at {p['path']} does not exist.")
        return prepare_response(json.dumps(resp), 200)

    
    file_data = json.loads(base64.b64decode(read_from_s3(location).encode()).decode())['text']
    payload = {}
    payload['topics'] = lda.get_topics(file_data)

    resp = respond("proc", cId, payload, error_code=0, error_msg="")
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/proc/qa', methods=['GET', 'POST'])
def get_q_and_a():
    cId, p, username, validation_code, validation_msg = receive("proc", "qa", request)
    
    if validation_code != 0:
        # failed validation
        resp = respond("proc", cId, {}, error_code=validation_code, error_msg=validation_msg)
        return prepare_response(json.dumps(resp), 200)

    
    location = username + "/" + p['path']
    if check_for_file_s3(location) < 0:
        resp = respond("proc", cId, {}, error_code=11, error_msg=f"The specified file at {p['path']} does not exist.")
        return prepare_response(json.dumps(resp), 200)

        
    file_data = json.loads(base64.b64decode(read_from_s3(location).encode()).decode())['text']
    payload = qa.ask(p['question'], file_data)
    payload['extractive_answer'] = base64.b64encode(payload['extractive_answer'].encode()).decode() 
    payload['abstractive_answer'] = base64.b64encode(payload['abstractive_answer'].encode()).decode() 
    
    resp = respond("proc", cId, payload, error_code=0, error_msg="")
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/proc/transcribe', methods=['GET', 'POST'])
def get_audio_transcription():
    cId, p, username, validation_code, validation_msg = receive("proc", "transcribe", request)
    
    if validation_code != 0:
        # failed validation
        resp = respond("proc", cId, {}, error_code=validation_code, error_msg=validation_msg)
        return prepare_response(json.dumps(resp), 200)

    
    location = username + "/" + p['path']
    if check_for_file_s3(location) < 0:
        resp = respond("proc", cId, {}, error_code=11, error_msg=f"The specified file at {p['path']} does not exist.")
        return prepare_response(json.dumps(resp), 200)


    audio_bytes = read_from_s3(location, raw=True) 
    payload = {}
    transcript = transcriber.transcribe(io.BytesIO(audio_bytes))
    payload['data'] = base64.b64encode(transcript.encode()).decode()
    
    resp = respond("proc", cId, payload, error_code=0, error_msg="")
    return prepare_response(json.dumps(resp), 200)


@app.route('/fb/proc/qg', methods=['GET', 'POST'])
def get_questions():
    cId, p, username, validation_code, validation_msg = receive("proc", "qg", request)
    
    if validation_code != 0:
        # failed validation
        resp = respond("proc", cId, {}, error_code=validation_code, error_msg=validation_msg)
        return prepare_response(json.dumps(resp), 200)

    
    location = username + "/" + p['path']
    if check_for_file_s3(location) < 0:
        resp = respond("proc", cId, {}, error_code=11, error_msg=f"The specified file at {p['path']} does not exist.")
        return prepare_response(json.dumps(resp), 200)


    file_data = json.loads(base64.b64decode(read_from_s3(location).encode()).decode())['text']
    payload = {}
    payload['questions'] = []
    raw_questions = qg.generate(file_data)
    for question in raw_questions:
        payload['questions'].append(base64.b64encode(question.encode()).decode())
    
    resp = respond("proc", cId, payload, error_code=0, error_msg="")
    return prepare_response(json.dumps(resp), 200)


# endregion


if __name__ == '__main__':
    # diff = int(argv[1])
    # remove old offset and endpoint log
    if os.path.exists(os.getenv("ENDPOINT_LOG_PATH")):
        os.remove(os.getenv("ENDPOINT_LOG_PATH"))
    if os.path.exists(os.getenv("ENDPOINT_LOG_PATH") + ".offset"):
        os.remove(os.getenv("ENDPOINT_LOG_PATH") + ".offset")

    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))
    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

    # TODO: Fix Endpoint Methods to not all be GET
    # creating thread
    # t1 = threading.Thread(target=run_periodic_logger, args=(diff,))
    # https://stackoverflow.com/a/2564282 how to exit thread.
    t1 = threading.Thread(target=run_periodic_logger, daemon=True)
    t1.start()

    run_flask()

    # wait until thread 1 is completely executed
    # t1.join()
