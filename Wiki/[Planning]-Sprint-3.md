## Table of Contents
[[_TOC_]]

## [Sprint Goal](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/milestones/3#tab-issues)
Goal: Keep Prototyping and Improving Prototypes

## Standby Issues
This is a list of the issues that we are blocked on and waiting on certain events in order to start. As we do not know when these events will occur, we will leave these issues out of the sprint and pull them in if needed.

### [Determine Interfacing Options for the Device](#97)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Look into what methods and connectors will be used for interfacing with the device. This includes looking at options for wireless and wired communication. It also includes looking at internet and non-internet forms of communication. If we will be allowing WiFi on the device we also need to determine how we will set it up. Do we need to include a small LCD display with a Dpad for navigation, do we include a touch screen, etc. Make sure to investigate the cost of the connectors that we would need to use as well as their power draw requirements. We should likely look at WiFi, Bluetooth, USB-C, USB-A, USB-B, HDMI (possibly), Ethernet (RJ-45), and others as applicable.

***Value Gained:*** This helps us get a better idea of how we will connect to the device and retrieve information from it.

***Acceptance Criteria***  
- [ ] Record findings in a wiki page
</details>

### [Analyze the results of the customer discovery survey](#6)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** look into the customer discovery survey and summarize the findings in a wiki page.

***Value Gained:*** This helps us get a better idea of what would be useful to students and instructors so we can better create our device.

***Acceptance Criteria***  
- [ ] Record findings in a wiki page
</details>

### [Link a simple ML model to the Backend](#69)
<details open><summary></summary>

***Story Points:*** $`7`$  

***Issue Summary:*** Train a really simple model then take that model and determine how to make inferences with it inside of the prototype application. See if the model can just be implemented in math directly in the application or if it needs to be run externally through web requests.

***Business Value Gained:*** This will help identify what issues will occur when trying to link a larger model to the application. This will also help us think about data format.

***Acceptance Criteria:***  
- [ ] Model can make inferences from the backend of the prototype application.
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

### [Order Materials](#84)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** This issue requires the bill of materials to be created and verified. See [Issue 83](#83)

***Business Value Gained:*** We need parts to come in as soon as possible, so ordering in a timely manner is important to building the device.

***Acceptance Criteria:***  
- [ ] The materials have been ordered and order details have been posted to the wiki  
</details>

### [Meet with Dr. Panciera (UX) to Discuss the Surveys](#80)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** This issue is set up to help refine the surveys and look into who to send them out to.

***Business Value Gained:*** This will help with ensuring the quality of the survey responses

***Acceptance Criteria:***  
- [ ] Meet with Dr. Panciera
- [ ] Discuss the survey questions
- [ ] Discuss the audience of the survey
</details>

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

### [Update The Tech Report](#95)
<details open><summary></summary>

***Story Points:*** $`10`$  

***Issue Summary:*** We have performed more research since the last time we updated the report. This information needs to be added to the report. Additionally, the report is currently hard to read. We should add dropdowns to make it more legible.

***Business Value Gained:*** This will assist in the legibility and understanding of the tech report

***Acceptance Criteria:***  
- [ ] Tech Report has new information added
- [ ] Report has formatting updated
</details>

## Issues From Last Sprint
This list is ordered from highest priority to lowest priority. These are the issues that have been carried over from the previous sprint, either due to being not completed, or out of scope.

### [Select a Camera and Supplementary Hardware](#57)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** This issue will involve selecting a camera to use for the custom device design. Any other hardware needed to operate the camera will be selected as well.

***Business Value Gained:*** A camera is necessary to gather lecture video, so we need to make a decision on the type of camera we would need to purchase and any other hardware needed to operate the selected camera.

***Acceptance Criteria:***  
- [ ] The research in the tech report, and other outside research has been used to inform the choice of hardware
- [ ] Several camera examples and the hardware needed to operate them has been outlined
- [ ] The camera and supplementary hardware examples have been ranked
- [ ] A decision has been made on the camera and other hardware we are ordering
- [ ] Justification for the decision has been documented
- [ ] The camera and other hardware has been added to the BOM  
</details>

### [Select a Motor and Supplementary Hardware](#58)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** This issue will involve selecting a motor to use for the custom device design. Any other hardware needed to operate the motor will be selected as well.

***Business Value Gained:*** A motor is necessary to adjust the camera direction for either focusing the camera on a location or for following the instructor. For this reason, we need to make a decision on the type of motor we would need to purchase and any other hardware needed to operate the selected motor.

***Acceptance Criteria:***  
- [ ] The research in the tech report, and other outside research has been used to inform the choice of hardware
- [ ] Several motor examples and the hardware needed to operate them has been outlined
- [ ] The motor and supplementary hardware examples have been ranked
- [ ] A decision has been made on the motor and other hardware we are ordering
- [ ] Justification for the decision has been documented
- [ ] The motor and other hardware has been added to the BOM  
</details>

### [Prototype QT Webassembly backend](#64)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Investigate one of the possible backend options to get a feel for it. This should involve developing some small GUI in under 5 hours. Try to get a local desktop app and a web GUI by using QT for Webassembly.

***Business Value Gained:*** This will help in determining what languages to use in the project.

***Acceptance Criteria:***  
- [ ] Prototype a small desktop GUI
- [ ] Prototype a small website GUI
- [ ] Get a feel for the language and identify concerns.
</details>

### [Prototype Angular Backend](#65)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Investigate one of the possible backend options to get a feel for it. This should involve developing some small GUI in under 5 hours. 

***Business Value Gained:*** This will help in determining what languages to use in the project.

***Acceptance Criteria:***  
- [ ] Prototype a small website GUI
- [ ] Get a feel for the language and identify concerns.
</details>

### [Decide QT vs Angular](#66)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** Make a decision about what language to use primarilly as the first choice going forward.

***Business Value Gained:*** Decide what language to continue development with

***Acceptance Criteria:***  
- [ ] Decided what language to use
- [ ] Left a comment outlining which language was decided and why.
</details>

### [Determine Other Materials Needed for the Device Design](#59)
<details open><summary></summary>

***Story Points:*** $`10`$  

***Issue Summary:*** This issue will involve outlining the other materials we will need to complete the design of the device.

***Business Value Gained:*** Other materials will be needed to get the microphone, camera, and motor to work as one system. This will allow use to create an operating device and will be the final steps in the part decision process.

***Acceptance Criteria:***  
- [ ] A decision has been made on the board design: designing a PCB or using an MCU (e.g. Arduino)
- [ ] Research has been completed on any other materials needed to work with the overall design
- [ ] The research has been documented in the wiki
- [ ] Justification for the board and part decisions has been outlined
- [ ] The other materials have been added to the BOM  
</details>

### [Prototype Backend File IO on Decided Platform](#63)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** Determine how to perform file IO in the chosen backend. The File IO should be done to the local storage system. Attempt to read and write out a JSON file. Identify any issues or concerns that are found that may impact development going forward.

***Business Value Gained:*** This issue will help determine if there will be any major problems reading and writing to the local file system that may impact development going forward.

***Acceptance Criteria:***  
- [ ] Determine how to perform file IO in the chosen backend
- [ ] Investigate options of libraries for specific file types like JSON, PDF, Txt, Docx, etc.
- [ ] Read a sample file from the local storage system
- [ ] Write the sample file back to the local storage system with some random changes made.
- [ ] Identify and list any concerns in the comment section.
</details>

### [Begin Implementing Basic Communications Between Backend and Frontend on Decided Platform](#67)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Implement some of the simple and basic communications as defined in the protocol document as a test.

***Business Value Gained:*** This will help test how hard implementing further communications will be and help with budgeting future time.

***Acceptance Criteria:***  
- [ ] One or two communications implemented
- [ ] Can send small amounts of sample data between front and backend.
</details>

### [Investigate Handwritten Character OCR](#76)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Look into how hard it will be to perform handwritten character OCR. Identify if any tools exist to help. If so test some of these on sample whiteboard text (make sure to have a drawing and some math on the image). If not then we will just embed pictures going forward instead of parsing them out. 

***Business Value Gained:*** Determine if it is possible to parse the text out from images or if we just need to embed the images themselves.

***Acceptance Criteria:***  
- [ ] Identified difficulties of handwritten character OCR
- [ ] Identified if any tools exist
- [ ] Tested tool if applicable.
</details>

### [Design the Custom Board Schematic/Block Diagram](#60)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** This issue will involve creating a schematic and block diagram for the device.

***Business Value Gained:*** We need to know how all of the materials will connect together, so a schematic and block diagram will be important for outlining the connections. This will be important to use if we are designing a PCB and when we build the device.

***Acceptance Criteria:***  
- [ ] Decisions have already been made about the parts we will be using
- [ ] A complete schematic has been created and posted to the wiki
- [ ] A complete block diagram has been created and posted to the wiki
- [ ] At least one other team member (who is not assigned to this issue) has looked over the designs and has verified the diagrams  
</details>

### [Research and Determine Project Funding](#62)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** This issue will involve looking into possible sources of funding. This will involve researching how we can get funding and what we need to do to apply for this funding.

***Business Value Gained:*** Because we are designing a custom device, we will need to purchase parts. For this reason, funding will provide us a way to pay for these parts.

***Acceptance Criteria:***  
- [ ] A list of possible funding opportunities have been outlined and placed in the wiki
- [ ] Requirements to apply to the funding opportunities have been outlined
- [ ] A decision has been made, as a team, about the direction we will go with funding  
</details>

## Overhead Issues
This list of issues deals with overhead tasks such as planning, presentations, SO objectives, and other deliverables.

### [End-Of-Quarter Presentation](#87)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** The team needs to give a presentation during week 10. This issue is a placeholder to mark the time spent on giving and practicing for the presentation

***Business Value Gained:*** Allocate time to spend on practicing as a team.

***Acceptance Criteria:***  
- [ ] Presentation practiced.
- [ ] Presentation Given
</details>

### [Software Engineering Team Components Document](#90)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** We need to fill out the software engineering team components document for class. 

***Business Value Gained:*** This requirements document helps to address how we are meeting the needs of software engineering as a team in our project. It also helps to address how we will meet future needs.

***Acceptance Criteria:***  
- [ ] Team has turned in the Software Engineering Team Components Document
- [ ] Descriptions on how the team will meet or has met requirements are provided for each of the 11 required fields.
</details>

### [Sprint 4 Planning](#86)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** Plan for the next sprint by creating stories.

***Business Value Gained:*** Helps to make decisions for next sprint and allocate time for this.

***Acceptance Criteria:***  
- [ ] Sprint issues are created.
</details>

### [Sprint 3 Retro](#85)
<details open><summary></summary>

***Story Points:*** $`1`$  

***Issue Summary:*** Perform retrospective on the current sprint by going through the KSS process.

***Business Value Gained:*** Help evaluate what can be improved in the next sprint. Allocates time for this process.

***Acceptance Criteria:***  
- [ ] Sprint Retro completed.
</details>

### [SO3-4](#89)
<details open><summary></summary>

***Story Points:*** $`10`$  

***Issue Summary:*** Every team member has been assigned this task of writing part of the tech report. We are estimating 2 hours per team member to complete this.

***Business Value Gained:*** This is a requirement for the course through MSOE. It will also help us explain our decisions in the Technology Report

***Acceptance Criteria:***  
- [ ] Team has each turned in SO3-4
</details>

## Priority Ordered List of PBIs
This list is ordered from highest to lowest priority

### [Create a Bill of Materials for Hardware Components](#83)
<details open><summary></summary>

***Story Points:*** $`2`$  

***Issue Summary:*** This issue will involve creating and finalizing the BOM. 

***Business Value Gained:*** We need to have a list of all the parts we decide to use to make ordering as easy as possible. Along with this, it will outline the overall cost of the device so we know how much funding we will need. 

***Acceptance Criteria:***  
- [ ] A BOM has been placed in the wiki and has been added to over the course of the sprint
- [ ] The BOM has been finalized and approved by at least one other team member (who is not assigned to this issue)
- [ ] Every team member has approved of the cost
</details>

### [Develop a NLP Preprocessing Pipeline](#93)
<details open><summary></summary>

***Story Points:*** $`3`$  

***Issue Summary:*** We need to develop a standardized way of preprocessing text. This will help to make sure the text that we are training on is consistent. It will also help us save time by applying the DRY principle.

***Business Value Gained:*** Helps maintain consistency with training data and helps save time due to not repeating code.

***Acceptance Criteria:***  
- [ ] Preprocessing methods or pipeline are created
- [ ] Preprocessing can handle the TED talks dataset
- [ ] Preprocessing can handle the MS Teams transcripts
</details>

### [Investigate Transformer Variations](#94)
<details open><summary></summary>

***Story Points:*** $`20`$  

***Issue Summary:*** We would like to spend more time investigating the various transformer variations. This will assist in making a decision on the exact model to use. Training and inference times will attempt to be measured with the Jupyter magic commands `%%time` and `%%timeit`. We can measure the accuracy of the summaries with the ROGUE metrics. We can then store this data in a dataframe and analyze the results. We can also use this time to improve the models and test those against the baselines as well. We may optionally want to test running over multiple related documents as well.

***Business Value Gained:*** This is a necessary step in assisting us with determining which models to use as well as creating a baseline to measure model performance against.

***Acceptance Criteria:***  
- [ ] Measured Transformer Model Performance
- [ ] Measured Transformer Model Accuracy
- [ ] Plotted Model Results
- [ ] Decided a Model.
</details>

### [Investigate LDA Variations](#92)
<details open><summary></summary>

***Story Points:*** $`10`$  

***Issue Summary:*** We would like to spend more time looking at the various LDA variations. This time will be spent determining which exact variation to use. Some of the criteria that may be looked at are performance and accuracy. We may also need to look for a metric to measure the accuracy. This issue differs from the former LDA issue as it is more focused now that we determined we are using LDA for topic modeling.

***Business Value Gained:*** This will help us identify the most performant LDA algorithms. 

***Acceptance Criteria:***  
- [ ] Investigated other LDA algorithms
- [ ] Training durations were measured
- [ ] optionally looked for a measure of accuracy
</details>

### [Update Communications API to Support Logins](#91)
<details open><summary></summary>

***Story Points:*** $`5`$  

***Issue Summary:*** We have decided that we likely want to support logins on the website or application we are building. As such, we need to integrate logins with the rest of the communication protocol so that there are not conflicts later.

***Business Value Gained:*** This will help prevent conflicts with logins later on.

***Acceptance Criteria:***  
- [ ] Current protocols are updated to support logins
- [ ] There is a way to perform the handshake for logging in
- [ ] We have given some thought to security
</details>






