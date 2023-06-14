import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE
from pathlib import Path
import os
# import progressbar
import urllib.request
import sys
import time


# https://blog.shichao.io/2012/10/04/progress_speed_indicator_for_urlretrieve_in_python.html
def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    duration = 1 if duration == 0 else duration
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                     (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


def cli(s: str):
    return subprocess.run(s, shell=True, check=True)


# check python version
cli("python --version")
print("Update Pip")
cli("python -m pip install pip")  # --upgrade
print("Install required libraries")
cli("pip install -r requirements.txt --user")
print("Spacy Downloads")
cli("python -m spacy download en_core_web_sm")
cli("python -m spacy download en_core_web_md")
cli("python -m spacy download en_core_web_lg")
print("NLTK downloads")
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('stopwords')
print("Create the .env file under API directory")
f = open("API/.env", "w")
f.write("""
AWS_ACCESS_KEY_ID = "tsa-backend"
AWS_SECRET_ACCESS_KEY = "minioadmin"
MINIO_URL = "http://localhost:9000"
AWS_DEFAULT_ID = "minioadmin"
AWS_DEFAULT_KEY = "minioadmin"
ENDPOINT_LOG_PATH = "endpoint_log_file.json"
ENDPOINT_LOGS_BUCKET = 'tsa-backend-endpoint-logs'
USER_FILES_BUCKET = 'tsa-backend-user-files'
ACCOUNT_INFO_BUCKET = 'tsa-backend-account-info'
LOGIN_TRACKING_BUCKET = 'tsa-backend-login-tracking'
BACKEND_URL_FOR_TESTS = "http://localhost:8844"
LOGGING_INTERVAL_MINUTES = 1
INACTIVE_LOGOUT_INTERVAL_MINUTES = 1
""")
f.close()
print("verify .env file")
f = open("API/.env", "r")
print(f.read())

print("\nDownloading Minio Server")
urllib.request.urlretrieve("https://dl.min.io/server/minio/release/windows-amd64/minio.exe", "minio.exe",
                           reporthook=reporthook)
print("\nDownloading Minio Client")
urllib.request.urlretrieve("https://dl.min.io/client/mc/release/windows-amd64/mc.exe", "minio_client.exe",
                           reporthook=reporthook)
print()
cli("refreshenv")
print("Creating Minio Data Directory")
os.mkdir("minio_data")

print("launching minio in external cli")
# cd %HOMEPATH%
# cd Downloads
Popen('launch_minio.bat', creationflags=CREATE_NEW_CONSOLE)  # https://stackoverflow.com/a/20612529

print("Creating boto3 connection")
import boto3
from dotenv import load_dotenv

load_dotenv("API/.env")
s3_client = boto3.client('s3',
                         endpoint_url=os.getenv('MINIO_URL'),
                         aws_access_key_id=os.getenv('AWS_DEFAULT_ID'),
                         aws_secret_access_key=os.getenv('AWS_DEFAULT_KEY'),
                         aws_session_token=None,
                         config=boto3.session.Config(signature_version='s3v4'),
                         verify=False
                         )
print("Creating Bucket: %s" % os.getenv("ENDPOINT_LOGS_BUCKET"))
s3_client.create_bucket(Bucket=os.getenv("ENDPOINT_LOGS_BUCKET"))
print("Creating Bucket: %s" % os.getenv("USER_FILES_BUCKET"))
s3_client.create_bucket(Bucket=os.getenv("USER_FILES_BUCKET"))
print("Creating Bucket: %s" % os.getenv("ACCOUNT_INFO_BUCKET"))
s3_client.create_bucket(Bucket=os.getenv("ACCOUNT_INFO_BUCKET"))
print("Creating Bucket: %s" % os.getenv("LOGIN_TRACKING_BUCKET"))
s3_client.create_bucket(Bucket=os.getenv("LOGIN_TRACKING_BUCKET"))
print("Creating minio alias")
command = "minio_client alias set local %s %s %s" % (os.getenv("MINIO_URL"),
                                                     os.getenv("AWS_DEFAULT_ID"),
                                                     os.getenv("AWS_DEFAULT_ID"))
cli(command)
print("Creating minio user")
command = "minio_client admin user add local %s %s" % (os.getenv("AWS_ACCESS_KEY_ID"),
                                                       os.getenv("AWS_SECRET_ACCESS_KEY"))
cli(command)
print("Giving created user access")
command = "minio_client admin policy attach local readwrite --user %s" % (os.getenv("AWS_ACCESS_KEY_ID"))
cli(command)
print("Install HuggingFace Models")
from transformers import BartTokenizer, BartForConditionalGeneration, WhisperProcessor, \
    WhisperForConditionalGeneration, AutoModelWithLMHead, AutoTokenizer, pipeline

model = BartForConditionalGeneration.from_pretrained('kajan1/bart-large-cnn-khan')
tokenizer = BartTokenizer.from_pretrained('kajan1/bart-large-cnn-khan')
model = WhisperForConditionalGeneration.from_pretrained('openai/whisper-tiny')
processor = WhisperProcessor.from_pretrained('openai/whisper-tiny')
model = pipeline('question-answering', model='distilbert-base-cased-distilled-squad')
model = AutoModelWithLMHead.from_pretrained("tuner007/t5_abs_qa")
tokenizer = AutoTokenizer.from_pretrained("tuner007/t5_abs_qa")
del model, tokenizer, processor

print("launching web server in external cli")
Popen('install_website.bat', creationflags=CREATE_NEW_CONSOLE)  # https://stackoverflow.com/a/20612529
cli('start http://localhost:4200/')

# these two will not work due to no admin access
# # install choco
# cli('@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"')

# # install nodejs long term service using choco
# cli("cinst nodejs-lts -y")

