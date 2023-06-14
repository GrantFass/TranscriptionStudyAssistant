## Table of Contents
[[_TOC_]]

## [Sprint Goal](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/milestones/6#tab-issues)

Hardware: Begin Assembling Prototype & Printing. Update designs based on survey feedback.

ML: Build out classes for Summarizers, Topic Modeling, and Sentences.

Software: Implement API endpoints in backend. Get frontend to be minimally viable.






***
## Issues From Last Sprint
This list is ordered from highest priority to lowest priority. These are the issues that have been carried over from the previous sprint, either due to being not completed, or out of scope.

***None*** 







***
## Overhead Issues
This list of issues deals with overhead tasks such as planning, presentations, SO objectives, and other deliverables.

### [Sprint 7 Planning](#151)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Plan for the next sprint by creating stories.

***Business Value Gained:*** Helps to make decisions for next sprint and allocate time for this.

***Acceptance Criteria:***  
- [ ] Sprint issues are created.
</details>

### [Sprint 6 Retro](#150)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Perform retrospective on the current sprint by going through the KSS process.

***Business Value Gained:*** Help evaluate what can be improved in the next sprint. Allocates time for this process.

***Acceptance Criteria:***  
- [ ] Sprint Retro completed.
</details>

### [Update the Software Engineering Team Components Document](#138)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Team should update the Software Engineering Team components document to reflect the progress made this quarter.

***Business Value Gained:*** This relates to the grade for the class. It also serves as a form of documentation for the work done to date.

***Acceptance Criteria:***  
- [ ] Updated requirements section
- [ ] Updated software architecture and modeling section
- [ ] Updated design section
- [ ] Updated testing section
- [ ] Updated security and privacy section
- [ ] Updated tools section
- [ ] Updated experimentation and prototyping section
- [ ] Updated third party components section
- [ ] Updated documentation section
- [ ] Updated managing risks section
- [ ] Updated standards used section
</details>

### [Presentation Draft](#139)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** The end of quarter presentation needs to be drafted by Monday night of Week 9. This way it is ready for our meeting the following day. 

***Business Value Gained:*** This is required so that our presentation is drafted and can be reviewed during the week 9 meeting. This will give us time in order to make any final changes. It will also give us time in order to practice the presentation.

***Acceptance Criteria:***  
- [ ] Goal and scope of the project is drafted
- [ ] Importance of the project is drafted
- [ ] Technology investigation is drafted
- [ ] Summary of work completed is drafted
- [ ] Sprint 5 review is drafted
- [ ] Current functionality is drafted
- [ ] High Priority PBI's section is drafted
- [ ] Feedback from last round of presentations is accounted for.
</details>

### [Update The Tech Report](#95)
<details open><summary></summary>

***Story Points:*** $`10`$  

***Issue Summary:***    
We have performed more research since the last time we updated the report. This information needs to be added to the report. Additionally, the report is currently hard to read. We should add dropdowns to make it more legible. This will also include moving most of the text to breakout pages. The current hardware pages are examples of the breakout pages for specialization. This is designed to make the report much easier to read.

***Business Value Gained:***    
This will assist in the legibility and understanding of the tech report

***Acceptance Criteria:***  
- [ ] Tech Report has new information added
- [ ] Report has formatting updated
- [ ] Information moved to breakout pages
- [ ] Home and Sidebar for the Wiki are updated
</details>



***
## Priority Ordered List of New PBIs
This list is ordered from highest to lowest priority

### [Implement Authentication Backend Topics](#149)
<details open><summary></summary>

***Story Points:*** $`11`$  

***Issue Summary:*** Implement the minimal versions of the backend topics under the Authentication sub header in the API Communications Protocol Document. Does not involve dealing with the error codes for now. This will likely require a new MINIO S3 bucket for storing account information.

***Business Value Gained:*** Required for functionality of our site. Needed to be able to login and sign up.

***Acceptance Criteria:***  
- [ ] User Accounts S3 bucket created
- [ ] Access options for new s3 bucket added to backend
- [ ] new s3 bucket creation instructions added to readme
- [ ] Bucket names added to env file and readme
- [ ] User data file JSON format added to API doc.
- [ ] No Plain Text Passwords.
- [ ] Create New User endpoint implemented
- [ ] Login New User endpoint implemented
- [ ] Logout user endpoint implemented
- [ ] Password reset endpoint implemented or problems are listed
- [ ] Username / Token validation implemented. 
</details>

### [Implement Account Info Backend Topics](#148)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Implement the minimal versions of the backend topics under the Account Information sub header in the API Communications Protocol Document. Does not involve dealing with the error codes for now.

***Business Value Gained:*** Required for functionality of our site. Needed to be able to check stored information and manage account

***Acceptance Criteria:***  
- [ ] Get Device History List implemented
- [ ] Clear Device History List implemented
- [ ] Get connected devices implemented
- [ ] Set maximum connections implemented
- [ ] Get stored information implemented
- [ ] Delete Account Implemented
</details>

### [Implement File Management Backend Topics](#147)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Implement the minimal versions of the backend topics under the File Management sub header in the API Communications Protocol Document. Does not involve dealing with the error codes for now.

***Business Value Gained:*** Required for functionality of our site. Needed to be able to allow users to add new files

***Acceptance Criteria:***  
- [ ] Method to query S3 user data to determine if file associated with account created
- [ ] File upload implemented
- [ ] File download implemented
- [ ] get storage size implemented
- [ ] get user files / dir information implemented
- [ ] delete files implemented
</details>

### [Implement Transformer Prediction Class](#145)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Create a class to train and run part of the Machine Learning models for the backend.

***Business Value Gained:*** Required to link the ML models to the backend.

***Acceptance Criteria:***  
- [ ] Created a new S3 bucket. Involves updating Readme, MinIO, and env file.
- [ ] Created a python class
- [ ] Python class has a method to 'train' transformer and save best result to S3
- [ ] Python class has a predict / inference method.
- [ ] Prediction method loads the stored model from S3
- [ ] Prediction method summarizes passed in text.
- [ ] Prediction method returns the summary and the accuracy if possible.
</details>

### [Implement LDA Prediction Class](#144)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Create a class to train and run part of the Machine Learning models for the backend.

***Business Value Gained:*** Required to link the ML models to the backend.

***Acceptance Criteria:***  
- [ ] Created a new S3 bucket. Involves updating Readme, MinIO, and env file.
- [ ] Created a python class
- [ ] Python class has a method to 'train' LDA model and save best result to S3
- [ ] Trained models over different datasets and saved them all to MinIO. Examples: specific khan academy domains, all khan academy, all ted, all text results.
- [ ] Python class has a predict / inference method.
- [ ] Prediction method loads the stored model from S3
- [ ] Prediction method returns the topic & keyword prediction result.
- [ ] Some method of testing which model is most accurate / best if possible.
</details>

### [Update API Comms Doc](#143)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Update the API Comms doc with some of the changes learned from backend implementation

***Business Value Gained:*** Will make the backend more concise, easier to understand, and faster.

***Acceptance Criteria:***  
- [ ] Remove the Edit Transcript endpoint from data processing as its the same as file upload with an overwrite option.
- [ ] Change all JSON True to true to be in proper format
- [ ] Add preprocessing / cleaning option to the file upload
- [ ] Store uploaded files in their own JSON format in backend (defined in API)
</details>

### [Implement Frontend for Account Information Topic Pages](#129)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** This issue involves creating frontend pages that are related to the account information topics. The main account information page probably will use the topics for *get device history list*, *clear device history list*, and *get connected devices*.

***Business Value Gained:*** This will let us show and display the account information portion of the site. 

***Acceptance Criteria:***  
- [ ] account information page created.
- [ ] Account deletion page created
- [ ] set maximum connections page created
- [ ] get stored information page created
</details>

### [Implement Frontend for File Management Topic Pages](#130)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** This issue involves creating frontend pages that are related to the file management topics. The browse page will likely include the endpoints for download, storage size, delete, and get dir info.

***Business Value Gained:*** This will let us show and display the file management portion of the site.

***Acceptance Criteria:***  
- [ ] upload page created
- [ ] browse page created.
</details>

### [Implement Frontend for Data Processing Topic Pages](#131)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** This issue involves creating frontend pages that are related to the data processing topics. This also includes the file editor portion of the site.

***Business Value Gained:*** This will let us show and display the data processing portion of the site.

***Acceptance Criteria:***  
- [ ] get file data & editor page created
- [ ] transcript summary page created
- [ ] transcript topics page created
- [ ] question and answer page created
- [ ] sentences by keyword page created
</details>

### [Test Camera](#141)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** This issue involves acquiring relevant libraries needed to operate the specified component. These libraries should then be used to set ups a simple test file to verify that the component functions as expected.

***Business Value Gained:*** This will help us determine if we have any unexpected hardware issues so that they can be addressed before more of the modeling is completed.

***Acceptance Criteria:***  
- [ ] Camera can receive video
</details>

### [Test Motor](#142)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** This issue involves acquiring relevant libraries needed to operate the specified component. These libraries should then be used to set ups a simple test file to verify that the component functions as expected.

***Business Value Gained:*** This will help us determine if we have any unexpected hardware issues so that they can be addressed before more of the modeling is completed.

***Acceptance Criteria:***  
- [ ] Motor is able to move as expected
</details>

### [Investigate I2C](#156)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Look into a protocol to try to get the microphones to work.

***Business Value Gained:*** May solve issue of microphones being too quiet.

***Acceptance Criteria:***  
- [ ] Will this work with our microphones
- [ ] What sort of hardware would this be from
- [ ] How will it interface with our board
- [ ] What benefit will this provide us
- [ ] Wiki page created
</details>

### [Find Amplification Circuit](#155)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Need to find an amplification circuit so that the microphones are loud enough to be heard by the device.

***Business Value Gained:*** Required to use microphones

***Acceptance Criteria:***  
- [ ] Design amplification circuit or find prebuilt chip
- [ ] Do audio amplification chips exist?
- [ ] Does the audio amplification chip perform audio filtering for us?
- [ ] Add to BOM
- [ ] Purchase
</details>

### [Find Voltage Regulator for Omni Mic](#154)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Need to find a regulator to make the omni mic work to fix the 2.2v line.

***Business Value Gained:*** Required to use microphones

***Acceptance Criteria:***  
- [ ] Find some regulator to work.
- [ ] Add to BOM
- [ ] Purchase
</details>

### [Redesign PCB with required microphone updates](#153)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Need to modify the PCB to make space for the new audio amplification chip.

***Business Value Gained:*** Required to use microphones

***Acceptance Criteria:***  
- [ ] Update the PCB to fit the new audio chip
- [ ] Communicate how the size of the board changes.
</details>

### [PCB Redesign Meeting](#152)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Need to hold a meeting to review the PCB again after the Audio Chip Redesign.

***Business Value Gained:*** Required to use microphones

***Acceptance Criteria:***  
- [ ] Changes OK'd by the team
</details>







***
## Standby Issues
This is a list of the issues that we are blocked on and waiting on certain events in order to start. As we do not know when these events will occur, we will leave these issues out of the sprint and pull them in if needed.

### [Create 3D Assembly of full Device](#113)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** This issue requires assembling the entire device. This follows the same rules as specified by #110

***Business Value Gained:*** This lets us model the full device for animations, exploded views, and other digital needs. It will also aid in identifying conflicts in assembly.

***Acceptance Criteria:***  
- [ ] Create a 3d model of the device
- [ ] Solidworks or preferably Autodesk Inventor are used
- [ ] The model is uploaded to the repo
- [ ] Every part is properly constrained in the right locations so it does not move
- [ ] Electronic components (not necessarily including wires) are included. 
</details>

### OTHER
<details open><summary></summary>

This is a list of other things that need to be done in the future.
- REST API unit tests
- kill logging process when the main ends
- API error codes and error handling for all endpoints
- Classes for sentences and QA endpoints.
- Make a launcher to launch / install everything required.
- Fix endpoints to not all be GET requests.
- Speech to text with OpenAI Whispers.

</details>

### [Implement Core Machine Learning Backend Topics](#146)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Implement the minimal versions of the backend topics under the Machine Learning sub header in the API Communications Protocol Document. Does not involve dealing with the error codes for now. Requires the relevant ML issues on creating classes for LDA and transformers being completed.

***Business Value Gained:*** Required for functionality of our site. Needed to be able to allow users to summarize files, get topics, etc.

***Acceptance Criteria:***  
- [ ] Transformer prediction class linked to Get Transcript Summary
- [ ] LDA prediction class linked to Get Transcript Topics
</details>

### [Analyze the results of the customer discovery survey](#6)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** look into the customer discovery survey and summarize the findings in a wiki page.

***Value Gained:*** This helps us get a better idea of what would be useful to students and instructors so we can better create our device.

***Acceptance Criteria***  
- [ ] Record findings in a wiki page
</details>

### [Update Device Design With Survey Feedback](#88)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** Incorporate feedback from the survey into the device design.

***Business Value Gained:*** Updating the device design will assist us in meeting the needs of both students and educators.

***Acceptance Criteria:***  
- [ ] Update sketches as necessary
- [ ] Note any major hardware changes that will need to be made
</details>

### [Create 3D Assembly of Device Base](#110)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** The main goal of this issue is to create a 3d assembly for the base of the device. This should be a proper 3d model created in solidworks or Autodesk inventor. The 3d model should be uploaded to the repo. Proper constraints should be used in the model so that the parts are not free floating. This means that everything should be constrained in all dimensions so it is fixed. IE: constrain touching surfaces so they are flush and constrain along the center axes of holes. Ask Grant if you have any questions about this process. This assembly file should contain models for most of the electronics (rough shapes are fine as long as holes are exact. Talk to Grant if you need a Caliper). It should also include the assembled device shell. It should likely include the main motor for rotation as well. Make sure that thermals and dust are considered. 

***Business Value Gained:*** This lets us create a full 3d model of our device so we can determine how it is assembled. This also lets us identify where there may be undue wear or structural weakness. We can also animate this model for our presentations as required.

***Acceptance Criteria:***  
- [ ] create a 3d assembly for the base of the device
- [ ] Solidworks or preferably Autodesk Inventor are used
- [ ] The model is uploaded to the repo
- [ ] Every part is properly constrained in the right locations so it does not move
- [ ] Electronic components (not necessarily including wires) are included. 
</details>

### [Create 3D Models of Device Camera Shell Components](#112)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** The main goal of this issue is to create 3d models (or just a 3d model) for the rotating camera pole of the device. This will let us print it by exporting it to a stl later. The model should be uploaded to the repo. This pole will be set on top of the base and connected to the motor in the base. This part needs to be designed to be stable when rotating on the base. Additionally it should not disconnect when the device is flipped upside down. Wires should be able to be run down the center of the column or along one of the outer edges. There should be space to mount the camera (and optionally the microphone if it is not in the base) on the device.

***Business Value Gained:*** This lets us model the camera pole for the device so we can print and assemble it later.

***Acceptance Criteria:***  
- [ ] Create a 3d model of the camera tower for the device
- [ ] Model is created in Solidworks or preferably Autodesk Inventor
- [ ] The models are uploaded to the repo (not their stl versions)
- [ ] Camera must fit
- [ ] How wires will be run is taken into account
- [ ] How this connects to the base is taken into account
- [ ] Should be stable on the base and not disconnect on flipping the device.
- [ ] There should be some way to easily disconnect the wires going between the base of the device and the camera area.
</details>




