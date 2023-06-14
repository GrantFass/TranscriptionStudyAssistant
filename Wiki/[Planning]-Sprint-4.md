## Table of Contents
[[_TOC_]]

## [Sprint Goal](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/milestones/4#tab-issues)

Hardware: Have main electrical components ordered, have 3d model of base shell, and have custom board designed.
ML: Collect the transcript dataset, and touch up preprocessing
Software: Finish prototyping and finish planning for main software device.






***
## Issues From Last Sprint
This list is ordered from highest priority to lowest priority. These are the issues that have been carried over from the previous sprint, either due to being not completed, or out of scope.

### [Update Communications API to Support Logins](#91)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** We have decided that we likely want to support logins on the website or application we are building. As such, we need to integrate logins with the rest of the communication protocol so that there are not conflicts later. We also need to finish defining the RESTful API endpoints to unblock #67. This issue does not include meeting with other team members to review the protocol. This will be done in another issue.

***Business Value Gained:*** This will help prevent conflicts with logins later on.

***Acceptance Criteria:***  
- [ ] Current protocols are updated to support logins
- [ ] There is a way to perform the handshake for logging in
- [ ] We have given some thought to security
</details>

### [Decide QT vs Angular](#66)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** Make a decision about what language to use primarilly as the first choice going forward.

***Business Value Gained:*** Decide what language to continue development with

***Acceptance Criteria:***  
- [ ] Decided what language to use
- [ ] Left a comment outlining which language was decided and why.
</details>

### [Investigate LDA Variations](#92)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** We would like to spend more time looking at the various LDA variations. This time will be spent determining which exact variation to use. Some of the criteria that may be looked at are performance and accuracy. We may also need to look for a metric to measure the accuracy. This issue differs from the former LDA issue as it is more focused now that we determined we are using LDA for topic modeling.

***Business Value Gained:*** This will help us identify the most performant LDA algorithms. 

***Acceptance Criteria:***  
- [ ] Investigated other LDA algorithms
- [ ] Training durations were measured
- [ ] optionally looked for a measure of accuracy
</details>




***
## Overhead Issues
This list of issues deals with overhead tasks such as planning, presentations, SO objectives, and other deliverables.

### [Sprint 5 Planning](#100)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Plan for the next sprint by creating stories.

***Business Value Gained:*** Helps to make decisions for next sprint and allocate time for this.

***Acceptance Criteria:***  
- [ ] Sprint issues are created.
</details>

### [Sprint 4 Retro](#101)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Perform retrospective on the current sprint by going through the KSS process.

***Business Value Gained:*** Help evaluate what can be improved in the next sprint. Allocates time for this process.

***Acceptance Criteria:***  
- [ ] Sprint Retro completed.
</details>

### [Pilot the Surveys](#114)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Pilot the surveys with at least 1 instructor and 1 student before sending them out

***Business Value Gained:*** Help determine any remaining issues or confusion with the surveys

***Acceptance Criteria:***  
- [ ] Pilot survey with instructor
- [ ] Pilot survey with student
- [ ] Make necessary changes
</details>





***
## Priority Ordered List of New PBIs
This list is ordered from highest to lowest priority

### [Review Communications API](#102)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** This issue involves two or more people meeting to look through the [communications API protocol document](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/%5BDocumentation%5D%20API%20Communication%20Protocol) and make necessary changes. Because it is a meeting of people the points are higher to accommodate this. Expecting about a 2 hour meeting,

***Business Value Gained:*** This lets us review the communications document with the relevant parties to make sure everything looks accurate. Reviewing in this manner should help identify any security risks or other issues.

***Acceptance Criteria:***  
- [ ] Met with a team member to review the document
- [ ] Discussed the endpoints
- [ ] Made necessary changes.
</details>

### [Order Materials](#84)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** This issue requires the bill of materials to be created and verified. See (#83)

***Business Value Gained:*** We need parts to come in as soon as possible, so ordering in a timely manner is important to building the device.

***Acceptance Criteria:***  
- [ ] The materials have been ordered and order details have been posted to the wiki  
</details>

### [Design the Custom Board Schematic/Block Diagram](#60)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** This issue will involve creating a schematic and block diagram for the device. This does not include reviewing the device with another team member. That is a separate issue.

***Business Value Gained:*** We need to know how all of the materials will connect together, so a schematic and block diagram will be important for outlining the connections. This will be important to use if we are designing a PCB and when we build the device.

***Acceptance Criteria:***  
- [ ] Decisions have already been made about the parts we will be using
- [ ] A complete schematic has been created and posted to the wiki
- [ ] A complete block diagram has been created and posted to the wiki
</details>

### [Review Custom Board Schematic](#103)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** This issue involves two or more people meeting to look through the custom board schematic #60 and make necessary changes. Because it is a meeting of people the points are higher to accommodate this. Expecting about a 2 hour meeting,

***Business Value Gained:*** This lets us review the custom board schematic with the relevant parties to make sure everything looks accurate. Reviewing in this manner should help identify any security risks or other issues.

***Acceptance Criteria:***  
- [ ] Met with a team member to review the schematic
- [ ] Reviewed the wiki pages
- [ ] Identified and made necessary changes
- [ ] At least one other team member (who is not assigned to this issue) has looked over the designs and has verified the diagrams  
</details>

### [Create PCB Layout](#115)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** This issue handles the design of the custom PCB for the device. This issue will involve selecting and placing footprints, routing, and ensuring the design is suitable for ordering. This issue does not include meeting with another team member to review the design. That is handled in #116.

***Business Value Gained:*** All of our components need to be connected so designing a custom PCB will allow us to do this. This will also allow us to design a board that works best for our device.

***Acceptance Criteria:***  
- [ ] Footprints for parts have been placed
- [ ] The routing is complete
- [ ] A Design Rules Check is completed and all errors/warnings have been resolved
</details>

### [Build Database of Khan Academy Transcripts](#108)
<details open><summary></summary>

***Story Points:*** $`10`$  

***Issue Summary:*** This issue involves building a database of transcripts from the khan academy videos and their summaries. We should also track video duration, genera, titles, and links if possible. Due to the nature of this issue we should first investigate Kaggle to see if something already exists. We may want to also consider sending a email to Khan Academy to ask for the data directly instead of hammering their API. If neither of these work then we should Use Beautiful Soup and possibly something like Selenium to crawl their web pages and build the dataset ourselves. We would want to make sure that we have a rate limit of 1 request per second or less to make sure we do not cause them API issues. 

***Business Value Gained:*** This will help us build a dataset of transcripts and their summaries that we can use to help train and evaluate some of our models.

***Acceptance Criteria:***  
- [ ] Check if dataset exists on kaggle or anywhere else
- [ ] See if we could get some of the data from Khan Academy Directly
- [ ] Use beautiful soup and other necessary processes to build data manually
</details>

### [Add Acronym Evaluation to the Preprocessing Pipeline](#106)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** The goal of this issue is to identify common short segments in the text that are in all caps. Perhaps these may have commas or parentheses on either side. The first occurrence in the text may also have the words it relates to defined nearby. We should be able to identify what may be a possible acronym in the text and return a dictionary of these. Another option would possibly be replacing all of the acronyms with their long form counterparts or vice versa.

***Business Value Gained:*** Being able to determine what may be acronyms may be important for the preprocessing pipeline and pulling out topics for LDA.

***Acceptance Criteria:***  
- [ ] Identify acronyms in the text based on surrounding context
- [ ] Be able to create a list of acronyms in the text
</details>

### [Create 3D Models of Device Base Shell Components](#109)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** The main goal of this issue is to create 3d models for the shell of the base. This lets us print the base segments by exporting the files as a .stl later. The models should be created in soldworks or inventor. Inventor being preferred. The shell segments should likely be connected using screws and Heat Set Nuts in pre-sized holes. This will help to ensure structural stability as well as reducing assembly time and cost. The base shell model should have space for all of the main electronics and the motor for rotation to fit. This includes the power and interfacing ports. It may also contain the microphone if we are going with a unidirectional microphone. Determine if we need something like an Electrical Slip Ring

***Business Value Gained:*** This lets us model the base of the device so we can print and assemble it later.

***Acceptance Criteria:***  
- [ ] Create 3d models of the components of the shell for the base of the device
- [ ] Model is created in Solidworks or preferably Autodesk Inventor
- [ ] The models are uploaded to the repo (not their stl versions)
- [ ] The model has locations to mount electronics and motors in
- [ ] There are external ports for power and interfacing
- [ ] There is something for the turntable or rotating part of the device to sit on
- [ ] This should be doable with 2 models or at most 3.
- [ ] The models are designed to fit together with ability to print and assemble in mind
</details>

### [Create 3D Models of Electrical Components](#111)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** This issue requires making simple 3d models with holes in the proper locations and roughly the right size for all of the electrical components such as motors, circuit boards, interfacing connectors, power connectors, etc.

***Business Value Gained:*** This lets us compare the sizes of the electrical components and build an assembly of the device.

***Acceptance Criteria:***  
- [ ] Create a 3d model of the electronics for the device
- [ ] Model is created in Solidworks or preferably Autodesk Inventor
- [ ] The models are uploaded to the repo (not their stl versions)
</details>

### [Review Wiring Diagram](#118)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** The wiring diagram, found in the wiki page [here](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/Wiring%20Design), needs to be reviewed by the team. 

***Value Gained:*** The diagram needs to be reviewed by the hardware team to make sure everything is connected correctly. Along with this, having someone else on the team review this diagram will make sure we are all on the same page with the design.  

***Acceptance Criteria***  
- [ ] The wiring diagram has been reviewed by the hardware team
- [ ] The wiring diagram has been reviewed by another member of the team (not on the hardware team)
- [ ] A link to the diagram wiki page has been added to the Technology Report
</details>


***
## Standby Issues
This is a list of the issues that we are blocked on and waiting on certain events in order to start. As we do not know when these events will occur, we will leave these issues out of the sprint and pull them in if needed.

### [Create Node-Red Simulator For Communication Testing](#96)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** This issue is set up to help create a simulator for the communications to aid in development.

***Business Value Gained:*** This will help with developing the commands and testing they are correct.

***Acceptance Criteria:***  
- [ ] Implement JSON Schema validation
- [ ] Implement the commands
- [ ] Send sample responses
- [ ] Open the port on router so page can be accessed. Make sure it is secure / ip limited.
</details>

### [Begin Implementing Basic Communications Between Backend and Frontend on Decided Platform](#67)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Implement the API communications protocol endpoints as a RESTful API in the backend. This issue is blocked by #91 as the Communications Protocol needs to be mostly defined first. For now this issue only includes setting up the endpoints and potentially sending back a sample message. As of now the actual functionality of each function does not need to be implemented.

***Business Value Gained:*** This lets us implement our backend endpoints. It also lets us test connections to those endpoints to make sure they are setup correctly. 

***Acceptance Criteria:***  
- [ ] RESTful API endpoints implemented according to the [communications API protocol document](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/%5BDocumentation%5D%20API%20Communication%20Protocol).
- [ ] Actual Implementation of functionality of the endpoints is minimal
- [ ] Endpoints send back some sample response to verify the endpoint works.
</details>

### [Link a simple ML model to the Backend](#69)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Train a really simple model then take that model and determine how to make inferences with it inside of the prototype application. See if the model can just be implemented in math directly in the application or if it needs to be run externally through web requests.

***Business Value Gained:*** This will help identify what issues will occur when trying to link a larger model to the application. This will also help us think about data format.

***Acceptance Criteria:***  
- [ ] Model can make inferences from the backend of the prototype application.
</details>

### [Perform Hyperparameter Tuning for Transformers](#104)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Create a pipeline to grid search a relevant hyperparameter space for the transformers. Possibly investigate multiple transformer types. This will require comparing the summaries with the text. A Khan Academy dataset may be useful for this. This search process should probably be run on the DGX nodes of ROSIE using slurm batch run. Perhaps send an email to Dr. Retert to make sure that there are no scheduled downtimes or big projects coming up that would be interrupted. Doing this over a break would likely be a good option.

***Business Value Gained:*** This lets us train our transformers to get the best possible performance.

***Acceptance Criteria:***  
- [ ] Contact Dr. Retert to verify we will not be causing interuptions to important tasks
- [ ] Create a grid search space
- [ ] Parrelize the grid search where possible
- [ ] Launch a SLURM batch job to execute the grid search
</details>

### [Perform Hyperparameter Tuning for LDA](#105)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Create a grid search space to iterate over the relevant hyperparameter space for the LDA models. Possibly investigate their variations. This will require finding some metric to evaluate their performance. Launch this as a SLURM batch job.

***Business Value Gained:*** This lets us train our LDA models to get the best possible performance.

***Acceptance Criteria:***  
- [ ] Contact Dr. Retert to verify we will not be causing interuptions to important tasks
- [ ] Create a grid search space
- [ ] Parrelize the grid search where possible
- [ ] Launch a SLURM batch job to execute the grid search
</details>

### [Add Greek Symbol and Math Equation Identification to the Preprocessing Pipeline](#107)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** The goal of this issue is to identify what may be an equation of some sort in the text. This may be designated by greek letters. We should then be able to pull out all of the equations in order to a dictionary. We could substitute the first equation in the text with the word equation1. This will help with the summarizer running over equations and mangling them.

***Business Value Gained:*** This will help improve how well our summarizer model handeles equations. It would also help in making equations in the flashcards.

***Acceptance Criteria:***  
- [ ] Identify equations in the text based on surrounding context
- [ ] Substitute equations for text where possible
- [ ] Be able to return a dictionary of equations
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

### [Review PCB Layout](#116)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** This issue involves two or more people meeting to look through the PCB Layout #115 and make necessary changes. Because it is a meeting of people the points are higher to accommodate this. Expecting about a 2 hour meeting,

***Business Value Gained:*** This lets us review the PCB Layout with the relevant parties to make sure everything looks accurate. Reviewing in this manner should help identify any security risks or other issues.

***Acceptance Criteria:***  
- [ ] Met with a team member to review the layout
- [ ] Reviewed the wiki pages
- [ ] Identified and made necessary changes
- [ ] At least one other team member (who is not assigned to this issue) has looked over the designs and has verified the diagrams  
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

### [Update The Tech Report](#95)
<details open><summary></summary>

***Story Points:*** $`10`$  

***Issue Summary:*** We have performed more research since the last time we updated the report. This information needs to be added to the report. Additionally, the report is currently hard to read. We should add dropdowns to make it more legible.

***Business Value Gained:*** This will assist in the legibility and understanding of the tech report

***Acceptance Criteria:***  
- [ ] Tech Report has new information added
- [ ] Report has formatting updated
</details>





