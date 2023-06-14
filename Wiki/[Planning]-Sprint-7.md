## Table of Contents
[[_TOC_]]

## [Sprint Goal](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/milestones/6#tab-issues)

Hardware: Review Survey Feedback, 3d modeling, camera / microphone testing

ML: Investigate Missing Functionality (STT & Question Answer Systems)

Software: Finish Backend, Link Backend to Frontend






***
## Issues From Last Sprint
This list is ordered from highest priority to lowest priority. These are the issues that have been carried over from the previous sprint, either due to being not completed, or out of scope.

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








***
## Overhead Issues
This list of issues deals with overhead tasks such as planning, presentations, SO objectives, and other deliverables.

### [Sprint 8 Planning](#160)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Plan for the next sprint by creating stories.

***Business Value Gained:*** Helps to make decisions for next sprint and allocate time for this.

***Acceptance Criteria:***  
- [ ] Sprint issues are created.
</details>

### [Sprint 7 Retro](#159)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** Perform retrospective on the current sprint by going through the KSS process.

***Business Value Gained:*** Help evaluate what can be improved in the next sprint. Allocates time for this process.

***Acceptance Criteria:***  
- [ ] Sprint Retro completed.
</details>

### [Final Report](#176)
<details open><summary></summary>

***Story Points:*** $`14`$  

***Issue Summary:*** Work on the final report [assignment](https://csse.msoe.us/srdsgn/finalreport/). This should only account for writing up the parts of the paper.

***Business Value Gained:*** This will help by creating a standalone document to help others understand our project.

***Acceptance Criteria:***  
- [ ] project information section drafted
- [ ] Executive summary section drafted
- [ ] project summary section drafted
- [ ] software engineering team components documentation section drafted
- [ ] project postmortem drafted
- [ ] remaining work left in comment on issue.
</details>










***
## Priority Ordered List of New PBIs
This list is ordered from highest to lowest priority


### [Analyze the results of the customer discovery survey](#6)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** look into the customer discovery survey and summarize the findings in a wiki page.

***Value Gained:*** This helps us get a better idea of what would be useful to students and instructors so we can better create our device.

***Acceptance Criteria***  
- [ ] Record findings in a wiki page
</details>

### [Create 3D Assembly of Device Base](#110)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** The main goal of this issue is to create a 3d assembly for the base of the device. This should be a proper 3d model created in solidworks or Autodesk inventor. The 3d model should be uploaded to the repo. Proper constraints should be used in the model so that the parts are not free floating. This means that everything should be constrained in all dimensions so it is fixed. IE: constrain touching surfaces so they are flush and constrain along the center axes of holes. Ask Grant if you have any questions about this process. This assembly file should contain models for most of the electronics (rough shapes are fine as long as holes are exact. Talk to Grant if you need a Caliper). It should also include the assembled device shell. It should likely include the main motor for rotation as well. Make sure that thermals and dust are considered. 

***Business Value Gained:*** This lets us create a full 3d model of our device so we can determine how it is assembled. This also lets us identify where there may be undue wear or structural weakness. We can also animate this model for our presentations as required.

***Acceptance Criteria:***  
- [ ] create a 3d assembly for the base of the device
- [ ] Solidworks or preferably Autodesk Inventor are used
- [ ] The model is uploaded to the repo
- [ ] Every part is properly constrained in the right locations so it does not move
- [ ] Electronic components (not necessarily including wires) are included. 
</details>

### [Create Device Base Part Files](#157)
<details open><summary></summary>

***Story Points:*** $`11`$  

***Issue Summary:*** The main goal of this issue is to create the individual part files to assemble the device base. References #110.

***Business Value Gained:*** This lets us start printing the shell for our device so we can start assembly

***Acceptance Criteria:***  
- [ ] create a 3d assembly for the base of the device
- [ ] Solidworks or preferably Autodesk Inventor are used
- [ ] The model is uploaded to the repo
- [ ] Every part is properly dimensioned
- [ ] There is adequate spacing around electrical components for thermals and shrink of plastic
- [ ] mounting columns are wide enough that heat-set nuts can be used (ask Grant if you do not know what / how these are used)
- [ ] Ideally this is no more than 2 components, possibly 3 if there would be a need for quick access to internals through a single-screw door. Preferably a top and bottom shell piece would be better than a left and right shell piece design. This is so that the camera tower is fully supported.
</details>

### [Microphone Testing](#161)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Perform tests with the new microphone amplification circuit.

***Value Gained:*** This helps us confirm that our new microphone setup works and is the proper quality

***Acceptance Criteria***  
- [ ] testing performed
- [ ] Testing documented in wiki
</details>

### [Camera Quality Investigation](#162)
<details open><summary></summary>

***Story Points:*** $`11`$  

***Issue Summary:*** The original camera testing yielded very low performance results. We need to look into ways to improve these results or determine if we need another camera.

***Value Gained:*** This helps us confirm and address what is wrong with our camera setup.

***Acceptance Criteria***  
- [ ] testing performed
- [ ] Testing documented in wiki
</details>

### [Speech To Text (STT) Transcription Implementation](#163)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Implement STT in the backend. May additionally require a class if enough code is needed. If research is performed, document it in a wiki page.

***Value Gained:*** This helps us implement our own STT endpoint to address our project goals

***Acceptance Criteria***  
- [ ] STT endpoint implemented
- [ ] STT Class created (optional)
- [ ] STT Wiki Page Created (conditional)
</details>

### [Question And Answer Systems Investigation](#164)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Look into methods that we can use for question and answer systems.

***Value Gained:*** This helps us research how we can implement Question Answer Systems to meet our project goals

***Acceptance Criteria***  
- [ ] research performed
- [ ] research documented in wiki page
- [ ] wiki page linked to tech report
</details>

### [Question And Answer Systems Implementation](#165)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Implement the Question Answer System Endpoint. Will also require a class due to amount of code needed likely.

***Value Gained:*** This helps us implement the Question Answer Systems to meet our project goals

***Acceptance Criteria***  
- [ ] endpoint created
- [ ] class created (optional)
</details>

### [Update API Comms Doc UUID Ref](#166)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** Change the references to UUID5 for UUID4 in the API comms doc.

***Value Gained:*** Needs to be changed to match the backend since UUID5 is not the correct version for our usecase.

***Acceptance Criteria***  
- [ ] Updated comms doc
</details>

### [Update API Comms Doc JSON user data file format](#167)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** Add information about users to the API comms doc

***Value Gained:*** Needs to be changed to match the backend and for better documentation.

***Acceptance Criteria***  
- [ ] Documented what data is stored for each user (files, logins, etc.)
- [ ] Documented the JSON format of the various files.
</details>

### [Fix NLTK package redownload on launch](#168)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** NLTK packages are being redownloaded on launch every time. This needs to be fixed.

***Value Gained:*** This should help the program launch faster and use fewer resources. Also helps protect against threats

***Acceptance Criteria***  
- [ ] fixed the download error
</details>

### [Fix multiple process kill issue](#169)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** There is an issue with the logging process. The periodic logger is launched in a separate thread alongside the flask thread. They are not linked so they cannot be terminated properly. This MUST be fixed.

***Value Gained:*** This will help prevent memory leaks and zombie processes.

***Acceptance Criteria***  
- [ ] fixed the multithreading issue
- [ ] Both threads launch and close together
</details>

### [Installation Step Updates](#170)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** There is an issue with the logging process. The periodic logger is launched in a separate thread alongside the flask thread. They are not linked so they cannot be terminated properly. This MUST be fixed.

***Value Gained:*** This will help prevent memory leaks and zombie processes.

***Acceptance Criteria***  
- [ ] Updated the requirements file with the proper imports and the versions required
- [ ] Updated the readme with better installation instructions
- [ ] Updated the readme with a .env sample file
- [ ] Updated the readme with suggested python version
- [ ] Created a bash script / python script for setup and installation
- [ ] SpaCy downloads included in install
- [ ] NLTK downloads included in install
- [ ] Angular setup / npm downloads in install
- [ ] Testing performed in a virtual machine or fresh computer install to verify steps are correct
</details>

### [Create Unit Tests for Backend Endpoints](#171)
<details open><summary></summary>

***Story Points:*** $`11`$  

***Issue Summary:*** A unit tests file and the relevant classes have already been created. We now need to fill in the tests for each of the backend endpoints.

***Value Gained:*** This will help ensure that the backend stays properly working and up to date

***Acceptance Criteria***  
- [ ] Auth endpoint unit tests
- [ ] Account endpoint unit tests
- [ ] File endpoint unit tests
- [ ] Proc endpoint unit tests
- [ ] No artifacts or residual data is left over after unit tests are run.
  - [ ] Setup and teardown scripts are used.
- [ ] There is a unit test that checks if the endpoint response is faster than 200ms
</details>

### [Create Backend Error Codes & Messages](#172)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Backend endpoints have error codes and error messages added. This additionally includes trying to make sure that each endpoint only has one return.

***Value Gained:*** This will help ensure that the backend performs proper error checking.

***Acceptance Criteria***  
- [ ] Auth endpoint errors
- [ ] Account endpoint errors
- [ ] File endpoint errors
- [ ] Proc endpoint errors
</details>

### [Fix Endpoint Types](#173)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Currently every endpoint is a GET request. This should not be the case since some of these make more sense as other types.

***Value Gained:*** This will help improve API consistency

***Acceptance Criteria***  
- [ ] Auth endpoint
- [ ] Account endpoint
- [ ] File endpoint
- [ ] Proc endpoint
</details>

### [Fix Plaintext Passwords & Tokens](#174)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Currently the passwords and tokens are not only messaged in plaintext, but they are also stored in plaintext. This MUST be fixed.

***Value Gained:*** This is basically required for security principles.

***Acceptance Criteria***  
- [ ] Fix password and token messaging
- [ ] Fix password and token storage
</details>

### [Create Website Launch Script](#175)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** Create a python script that can be used to launch the website

***Value Gained:*** This would help with testing the website due to requiring less time.

***Acceptance Criteria***  
- [ ] website launch script created
</details>















***
## Standby Issues
This is a list of the issues that we are blocked on and waiting on certain events in order to start. As we do not know when these events will occur, we will leave these issues out of the sprint and pull them in if needed.

### OTHER
<details open><summary></summary>

This is a list of other things that need to be done in the future.
- Send data between device and backend

</details>

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

### [OWASP Audit](#158)
<details open><summary></summary>

***Story Points:*** $`11`$  

***Issue Summary:*** Analyze the software component of the team project using the Open Web Application Security Project (OWASP) standards. The assignment link can be found [here](https://csse.msoe.us/srdsgn/owasp/). The OWASP home page can be found [here](https://owasp.org/www-project-application-security-verification-standard/). The latest stable version of the OWASP standards can be found [here](https://github.com/OWASP/ASVS/tree/v4.0.3#latest-stable-version---403).

***Business Value Gained:*** This will help us analyze the security threats associated with the software project. It additionally helps us recognize areas that we need to improve in our design.

***Rating Levels:***  
- Addressed in project design, verified to not be a concern
- Addressed in project design, not tested
- Applicable but did not address in project
- Not sure if it applies to the project
- Does not apply to project

***Acceptance Criteria:***  
- [ ] Wiki page is created for OWASP Audit
- [ ] Wiki page is added to tech report
- [ ] Wiki page is added to sidebar
- [ ] Wiki page is added to home page in wiki
- [ ] Go through each of the Level 1 (L1 checkmark) objectives at least and determine the rating (as seen above) for each
  - [ ] Section 2 L1 points reviewed
  - [ ] Section 3 L1 points reviewed
  - [ ] Section 4 L1 points reviewed
  - [ ] Section 5 L1 points reviewed
  - [ ] Section 6.2.1 reviewed
  - [ ] Sections 7.1.1, 7.1.2, and 7.4.1 reviewed
  - [ ] Section 8 L1 points reviewed
  - [ ] Section 9 L1 points reviewed
  - [ ] Section 10 L1 points reviewed
  - [ ] Section 11 L1 points reviewed
  - [ ] Section 12 L1 points reviewed
  - [ ] Section 13 L1 points reviewed
  - [ ] Section 14 L1 points reviewed
</details>




