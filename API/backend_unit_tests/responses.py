import requests
import json
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
backend_url = os.getenv('BACKEND_URL_FOR_TESTS')


def get_unix_time_millis():
    epoch = datetime.datetime.utcfromtimestamp(0)
    now = datetime.datetime.utcnow()
    return int((now - epoch).total_seconds() * 1000.0)


def verify_timestamp(sent, received) -> bool:
    return received > sent


def get_standard_body(ts, cId, username, token, remove_standard_keys=None) -> json:
    data = {
        "ts": ts,
        "cId": cId,
        "username": username,
        "token": token
    }
    if remove_standard_keys is not None and isinstance(remove_standard_keys, list):
        for key in remove_standard_keys:
            data.pop(key)
    return data


def get_file_upload_json(path, data, overwrite, preprocess, remove_standard_keys=None) -> json:
    file = {
        "path": path,
        "data": data,
        "overwrite": overwrite,
        "preprocess": preprocess
    }
    if remove_standard_keys is not None and isinstance(remove_standard_keys, list):
        for key in remove_standard_keys:
            data.pop(key)
    return file


# region GET RESPONSE METHODS
def get_new_user_response(ts, cId, email, password, birthday, org, first, last, gender, phone, job, username,
                          remove_standard_keys=None, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/auth/new"
    data = {
        "ts": ts,
        "cId": cId,
        "p": {
            "email": email,
            "password": password,
            "birthday": birthday,
            "org": org,
            "first": first,
            "last": last,
            "gender": gender,
            "phone": phone,
            "job": job,
            "username": username
        }
    }
    if remove_standard_keys is not None and isinstance(remove_standard_keys, list):
        for key in remove_standard_keys:
            data.pop(key)
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_login_user_response(ts, cId, username, password, ip, os, browser, device, location, redirect,
                            remove_standard_keys=None, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/auth/in"
    data = {
        "ts": ts,
        "cId": cId,
        "p": {
            "username": username,
            "password": password,
            "ip": ip,
            "os": os,
            "browser": browser,
            "device": device,
            "location": location,
            "redirect": redirect
        }
    }
    if remove_standard_keys is not None and isinstance(remove_standard_keys, list):
        for key in remove_standard_keys:
            data.pop(key)
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_logout_user_response(ts, cId, username, token, logout_all,
                             remove_standard_keys=None, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/auth/out"
    data = {
        "ts": ts,
        "cId": cId,
        "p": {
            "username": username,
            "token": token,
            "all": logout_all
        }
    }
    if remove_standard_keys is not None and isinstance(remove_standard_keys, list):
        for key in remove_standard_keys:
            data.pop(key)
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_password_reset_response(ts, cId, username, email, phone,
                                remove_standard_keys=None, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/auth/exchange"
    data = {
        "ts": ts,
        "cId": cId,
        "p": {
            "username": username,
            "email": email,
            "phone": phone
        }
    }
    if remove_standard_keys is not None and isinstance(remove_standard_keys, list):
        for key in remove_standard_keys:
            data.pop(key)
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_device_history_list_response(body, num, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/acc/list"
    data = body
    data['p'] = {
        "num": num
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_clear_device_history_list_response(body, num, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/acc/clear"
    data = body
    data['p'] = {
        "num": num
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_connected_devices_response(body) -> json:
    endpoint = backend_url + "/fb/acc/connected"
    data = body
    return json.loads(requests.get(endpoint, json=data).content)


def set_maximum_connections_response(body, max_connections, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/acc/max"
    data = body
    data['p'] = {
        "max": max_connections
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_stored_information_response(body) -> json:
    endpoint = backend_url + "/fb/acc/info"
    data = body
    return json.loads(requests.get(endpoint, json=data).content)


def get_delete_account_response(body) -> json:
    endpoint = backend_url + "/fb/acc/delete"
    data = body
    return json.loads(requests.get(endpoint, json=data).content)


def get_upload_response(body, files, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/file/up"
    data = body
    data['p'] = {
        "files": files
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_download_response(body, files, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/file/down"
    data = body
    data['p'] = {
        "files": files
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_storage_size_response(body) -> json:
    endpoint = backend_url + "/fb/file/space"
    data = body
    return json.loads(requests.get(endpoint, json=data).content)


def get_directory_information_response(body) -> json:
    endpoint = backend_url + "/fb/file/list"
    data = body
    return json.loads(requests.get(endpoint, json=data).content)


def get_delete_files_response(body, files, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/file/remove"
    data = body
    data['p'] = {
        "files": files
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_preprocess_response(body, path, inplace, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/proc/clean"
    data = body
    data['p'] = {
        "path": path,
        "inplace": inplace
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_summary_response(body, path, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/proc/summary"
    data = body
    data['p'] = {
        "path": path
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_topics_response(body, path, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/proc/topics"
    data = body
    data['p'] = {
        "path": path
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_questions_response(body, path, question, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/proc/qa"
    data = body
    data['p'] = {
        "path": path,
        "question": question
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_sentences_response(body, path, keyword, num, remove_payload_keys=None) -> json:
    # raise NotImplementedError("error")
    endpoint = backend_url + "/fb/proc/sentences"
    data = body
    data['p'] = {
        "path": path,
        "keyword": keyword,
        "num": num
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)


def get_transcription_response(body, path, remove_payload_keys=None) -> json:
    endpoint = backend_url + "/fb/proc/transcribe"
    data = body
    data['p'] = {
        "path": path
    }
    if remove_payload_keys is not None and isinstance(remove_payload_keys, list):
        for key in remove_payload_keys:
            data['p'].pop(key)
    return json.loads(requests.get(endpoint, json=data).content)

# endregion
