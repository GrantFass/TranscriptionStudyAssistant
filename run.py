from subprocess import Popen, CREATE_NEW_CONSOLE
import subprocess
from pathlib import Path


def cli(s: str):
    return subprocess.run(s, shell=True, check=True)


print("launching minio in external cli")
Popen('launch_minio.bat', creationflags=CREATE_NEW_CONSOLE)  # https://stackoverflow.com/a/20612529
print("launching web server in external cli")
Popen('run_web_server.bat', creationflags=CREATE_NEW_CONSOLE)  # https://stackoverflow.com/a/20612529
cli('start http://localhost:4200/')
cli('start http://localhost:9000/')
backend = Path('API/backend.py').resolve()
print("launching %s\nPlease allow up to 1 min." % backend)
print("Alternatively comment this out and launch the backend manually")
with open(backend) as f:
    code = compile(f.read(), backend, 'exec')
    exec(code)

