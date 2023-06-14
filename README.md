# 24-Transcription-Study-Assistant

## Description
This project aims to create a tool that will assist in taking transcripts of courses and
breaking them down into pieces that can more easily be used for studying. This tool is 
intended to be utilized by all audiences but may be particularly beneficial for
neurodivergent students that face sensory overload during long lectures. 

This project is divided into three primary components.
1. Hardware
2. Web Software
3. Machine Learning

The hardware team is focusing on developing a video taking device for use with Microsoft
Teams, and other meeting software. This is meant to be an alternative to the [Meeting Owl 3](https://owllabs.com/products/meeting-owl-3?utm_source=adwords&utm_campaign=US_Branded&utm_medium=ppc&utm_term=meeting%20owl%203&hsa_kw=meeting%20owl%203&hsa_mt=e&hsa_tgt=kwd-1664191677785&hsa_src=g&hsa_ad=617179448370&hsa_ver=3&hsa_cam=1485487619&hsa_net=adwords&hsa_acc=2493962266&hsa_grp=78790216762&gclid=Cj0KCQiA_bieBhDSARIsADU4zLcaWRQWOvktF4fADjmooEcVXLYf4rbGnzq8EmovNgqnJcjop1JarCsaAsLBEALw_wcB).
The primary benefit that our device has over the meeting owl is cost. Our device aims to be
manufacturable as a proof of concept for under $200. This is much cheaper than the $1050
price tag the Meeting Owl 3 costs. Our device is meant to be an assistant for tracking
presenters in a classroom like environment for meetings.

The software team is focusing on developing a website that will support all the necessary
functions of our application, including our machine learning models. The website will be
designed so that video transcripts and other text based files can be uploaded to the server.
Then the server will allow you to modify and clean up the text, generate summaries of the
content, identify relevant topics, and possibly build study aids. An example study aid would
be question and answer flashcards.

The machine learning team is focusing on the models that allow us to summarize text and topics.
This is primarily done through transformers and Latent Dirichlet Allocation models.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Automatic Installation
Running this project locally can be done through a few simple steps. 
The first step is to install `python 3.10.0`. Once that is done,
you should be able to install the project by running setup.py. Once this is
completed you can run the entire project through run.py

## Manual Installation
Running this project locally can be somewhat difficult as there are external requirements.
Assuming that the proper python version (as noted in the requirements section) is installed
it should be possible to install relevant python library files by running the command
`pip install -r requirements.txt` out of the software home directory.

This application uses the SpaCy library and its language kits. Unfortunately, these can not be
installed through pip. Instead, they must be installed through the command line.
There are three model sizes that must be installed to be able to run the software. These
models can be found from [SpaCy](https://spacy.io/models/en). Download using the following commands:
- `python -m spacy download en_core_web_sm`
- `python -m spacy download en_core_web_md`
- `python -m spacy download en_core_web_lg`

The SpaCy `en_core_web_trf` model is not required.

The step is installing MinIO. MinIO is an object store that can be downloaded [here](https://min.io/download#/windows).
Both the server, and the client, must be downloaded. If on Windows, this will give two files:
`minio.exe` and `mc.exe`. Place these two executeables in a folder that you can run things from.
In order to run the web backend you must launch a console out of the folder and run the command:
`minio server minio_data`. This starts the object store which allows for storing log files as
well as files that are uploaded to the program.

The next step is to set up users and buckets inside MinIO. Access the [MinIO web interface](http://127.0.0.1:9000/).
Log in with the default username `minioadmin` and default password `minioadmin`.
Next you should see a sidebar of options. Click on Administrator -> Identity -> Users ->
Create User. You should then create a user called `tsa-backend`. Give it a password you can
remember as well as read write access then save. Next navigate to Administrator -> Buckets.
We need to create a bucket called `tsa-backend-endpoint-logs` and another bucket called 
`tsa-backend-user-files`. We also need to create a bucket called `tsa-backend-account-info`. No parameters need to be changed on these buckets, so they can be saved right after setting their names.

After the MinIO setup is complete you need to add a .env file under the API folder.
This file should have the below format. You should fill in the password for the user you
created under the access key. If your object store is on another computer then set the
endpoint url to its location. If you decided to name your user something other than `tsa-backend`
above than change that as well.
```
AWS_ACCESS_KEY_ID = "tsa-backend"
AWS_SECRET_ACCESS_KEY = "minioadmin"
MINIO_URL = "http://localhost:9000"
ENDPOINT_LOG_PATH = "endpoint_log_file.json"
ENDPOINT_LOGS_BUCKET = 'tsa-backend-endpoint-logs'
USER_FILES_BUCKET = 'tsa-backend-user-files'
ACCOUNT_INFO_BUCKET = 'tsa-backend-account-info'
LOGIN_TRACKING_BUCKET = 'tsa-backend-login-tracking'
BACKEND_URL_FOR_TESTS = "http://localhost:8844"
```

If you are planning on testing the backend without the use of a frontend then you will
need to either use curl commands or install a tool to send http requests. Much of the
testing during development was done using [Postman](https://www.postman.com/downloads/).

## Running the Web Software
- Pull down the repo in Visual Studio Code.
- cd or navigate into the transcript-study-assistant folder using the terminal within VS Code.
- Type in "ng serve". The website should run at an address like http://localhost:4200/.
- If the website does not run, try running "npm install -g @angular/cli".
- Please contact Teresa with further questions. I'm happy to improve these instructions further.

## Requirements
- Python version 3.10

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Hardware Team:
- Angela Christie
- Alexander Karpov

Software Team:
- Teresa Toohill
- Grant Fass

Machine Learning Team:
- Nicholas Kaja
- Grant Fass

Advisor:
- Dr. Sohum Sohoni

Institution:
- Milwaukee School of Engineering 2022-2023

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
