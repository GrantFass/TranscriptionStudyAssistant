
## Table of Contents
[[_TOC_]]

## [Sprint Goal](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/milestones/8#tab-issues)

Planning out a four week sprint so we line up with the other teams again. This will also leave us more time to finish everything off.

Hardware: Build and Assemble Device, Program Interfacing

ML: Add in Question Generation

Software: OWASP backend updates, Frontend UX updates

General: Poster & Final Report






***
## Issues From Last Sprint
This list is ordered from highest priority to lowest priority. These are the issues that have 


### [Update API Comms Doc JSON user data file format](#167)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** Right now our file upload endpoint has different behaviors based on the type of file uploaded. This should be documented in our API. This includes a section on the format of the JSON document that is uploaded for text.

***Value Gained:*** Needs to be changed to match the backend and for better documentation.

***Acceptance Criteria***  
- [ ] Documented what data is stored for each user (files, logins, etc.)
- [ ] Documented the JSON format of the various files.
</details>


### [Fix Endpoint Types](#173)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** Currently every endpoint is a GET request. This should not be the case since some of these make more sense as other types.

***Value Gained:*** This will help improve API consistency

***Acceptance Criteria***  
- [ ] Auth endpoint
- [ ] Account endpoint
- [ ] File endpoint
- [ ] Proc endpoint
</details>






***
## Overhead Issues
This list of issues deals with overhead tasks such as planning, presentations, SO objectives, and other deliverables.

### [Sprint 8 Retro](#184)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** Perform retrospective on the current sprint by going through the KSS process.

***Business Value Gained:*** Help evaluate what can be improved in the next sprint. Allocates time for this process.

***Acceptance Criteria:***  
- [ ] Sprint Retro completed.
</details>

### [SO2-3 Societal Impact](#185)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Fill out the SO Objective

***Business Value Gained:*** Required for course

***Acceptance Criteria:***  
- [ ] Grant Completed
- [ ] Angela Completed
- [ ] Nick Completed
- [ ] Teresa Completed
- [ ] Xander Completed
</details>

### [SO5-2 Timely Intervention](#186)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Fill out the SO Objective

***Business Value Gained:*** Required for course

***Acceptance Criteria:***  
- [ ] Grant Completed
- [ ] Angela Completed
- [ ] Nick Completed
- [ ] Teresa Completed
- [ ] Xander Completed
</details>

### [Collect Poster Field Notes](#187)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** Find images of other senior design posters. Document what you like and do not like about them. Include image references.

***Business Value Gained:*** Required for course

***Acceptance Criteria:***  
- [ ] Wiki page created
</details>

### [Create Poster Concept Maps and Sketches](#188)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Create sample sketches of what the poster could look like. Remember that sketches should be informal and quick. Share these with the team to gather feedback.

***Business Value Gained:*** Required for course

***Acceptance Criteria:***  
- [ ] Sketches documented in wiki page
</details>

### [Draft Poster](#189)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** A poster is required for the senior design show. Create a formal draft of this poster. Share it with the team and gather feedback.

***Business Value Gained:*** Required for course

***Acceptance Criteria:***  
- [ ] Poster is drafted
- [ ] Feedback is collected
</details>

### [Finalize Poster](#190)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** A poster is required for the senior design show. Finalize the poster based on the feedback from the draft

***Business Value Gained:*** Required for course

***Acceptance Criteria:***  
- [ ] Poster is finalized
</details>

### [Update Final Report](#191)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Update the final report with work completed this sprint

***Business Value Gained:*** Required for course

***Acceptance Criteria:***  
- [ ] Final report is updated
</details>

### [Update Software Engineering Team Components Doc](#192)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Update the document with work completed this quarter

***Business Value Gained:*** Required for course

***Acceptance Criteria:***  
- [ ] document is updated
</details>








***
## Priority Ordered List of New PBIs
This list is ordered from highest to lowest priority

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

### [Write Device Side Interfacing Code](#193)
<details open><summary></summary>

***Story Points:*** $`14`$  

***Issue Summary:*** Write interfacing code for the microphones, motors, and camera. If possible, mostly for time and ease of programming, it would be preferred if the device side code is made for interfacing. This means that we can program the bulk of the behaviors in an easier to understand language like python. 

***Value Gained:*** This is required so our custom device works

***Acceptance Criteria***  
- [ ] Interfacing code for microphones created
- [ ] Interfacing code for motors created
- [ ] Interfacing code for camera created
</details>

### [Create python side controller code for device](#194)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Write code that uses the interfacing code from the device to control it. This involves allowing for recordings to be started and stopped. It also should handle tracking of the presenter using OpenCV.

***Value Gained:*** This is required so our custom device works

***Acceptance Criteria***  
- [ ] Device control code written.
</details>

### [Fix OWASP issues in backend](#195)
<details open><summary></summary>

***Story Points:*** $`21`$  

***Issue Summary:*** The OWASP audit is going to bring up a lot of issues that we have not dealt with yet. This issue is here to allocate time to fix these issues.

***Value Gained:*** This is required so our custom device works and our backend is secure.

***Acceptance Criteria***  
- [ ] OWASP issues fixed or documented otherwise
</details>

### [Implement the timed logout in backend](#177)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** The backend should automatically logout users who are inactive for more than some interval of time. The backend already records when the last action taken by each user was through the `auth_df`. This time is updated in the validate user method that is hit for each endpoint. We can just add a check that runs when the MINIO log thread is run. This check would just compare timestamps. If any of the timestamps were more than 15 min ago those rows would be removed from the dataframe. This can be done quickly using a mask.

***Value Gained:*** This helps us preserve resources as well as improve session security.

***Acceptance Criteria***  
- [ ] Implemented timed logout.
</details>

### [Test VTT file upload](#178)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** We need to verify that our file upload works properly with VTT files.

***Value Gained:*** This helps us by confirming that the files we list we accept are actually accepted.

***Acceptance Criteria***  
- [ ] VTT file tested
- [ ] Issues fixed or documented if necessary
</details>

### [Implement Question Generation](#179)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** We want to implement a way to generate questions.

***Value Gained:*** This will let us satisfy our goal of hopefully generating questions to quiz users.

***Acceptance Criteria***  
- [ ] Question generation implemented
- [ ] Endpoint created
- [ ] Endpoint added to API doc.
</details>

### [Assemble PCB](#180)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Assemble the PCB

***Value Gained:*** Required for our custom device to work.

***Acceptance Criteria***  
- [ ] PCB is assembled
</details>

### [Frontend UX Improvements](#181)
<details open><summary></summary>

***Story Points:*** $`10`$  

***Issue Summary:*** The frontend needs to be evaluated for any potential UX improvements. This includes look and feel. These issues should then be fixed if possible.

***Value Gained:*** This will improve interaction and customer satisfaction with our site.

***Acceptance Criteria***  
- [ ] Possible UX Improvements are documented
- [ ] UX improvements are made were possible
</details>

### [Password Reset Endpoint](#182)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Implement the password reset endpoint

***Value Gained:*** This will allow users to reset their password. This is likely important for security reasons.

***Acceptance Criteria***  
- [ ] Document the responses in the API document
- [ ] Implement the endpoint in the backend
- [ ] Add at least one valid test in the backend tests (class already exists)
</details>

### [Remove Get Sentences by Keyword](#183)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** We do not have enough time to implement this endpoint. We therefore need to mark it as such.

***Value Gained:*** This removes a potential security flaw by removing an endpoint that is not implemented.

***Acceptance Criteria***  
- [ ] Marked the endpoint as not implemented in the API comms doc
- [ ] Deleted the endpoint from the backend
- [ ] Deleted the endpoint tests from the backend.
</details>

### [Model and print turret](#196)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** 3d model the turret and get it printed

***Value Gained:*** needed to be able to assemble device

***Acceptance Criteria***  
- [ ] Turret is modeled
</details>

### [Assemble Device](#197)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Put the entire device together

***Value Gained:*** needed so we can test some of it

***Acceptance Criteria***  
- [ ] Device is assembled.
</details>






















