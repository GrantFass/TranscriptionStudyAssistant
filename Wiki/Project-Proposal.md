# Primary Project: Transcription Study Assistant
## Project Description
### Projected Client, Customer, or End User
Teachers and students.
### Project Stakeholder
N/A.
### Problem Being Solved
This project aims to create a tool that will assist in taking transcripts of courses and breaking them down to help students study as well as helping instructors identify what key concepts a lecture covered. This tool aims to aid all students and educators, but is intended to assist neurodivergent students facing sensory overload. The following are some of the possible goals and stretch goals for the project:
- Collect transcripts of courses.
- Identify what topics were covered in the transcript.
- Identify any overarching ideas or the main takeaways of lectures.
- Order and present the topics covered in the transcript by duration.
- [Stretch] Extract questions and answers from the transcript.
- Break the transcripts into notes under the topics covered.
- [Stretch] Possibly allow to work on small sections of text such as essays or short answer questions.
- Possibly try to build flash cards surrounding content from the lecture.
- Possibly try to build quizzes surrounding content from the lecture.
- [Stretch] Allow instructor feedback on the accuracy of the generated handouts, flash cards, and quizzes.
### Possible Software Component
- Use ML and AI to extract the topics from the transcripts.
- Use ML and AI to extract overarching lesson themes/emphasized topics.
- Use ML and AI to link notes to topics.
- Use the topics and notes to build flash cards.
- Use the topics and notes to build quizzes.
- Build a windows application to display the transcripts, topics, notes, quizzes, etc.
- [Stretch] Possibly add an android app version?
- [Stretch] allow for instructor feedback in the app.
- [Stretch] Possibly allow for linking multiple transcripts together as well as their ideas and notes.
  - [Stretch] scan all directory transcripts.
### Possible Hardware Component
- Video camera that can record lecture notes written/displayed on the board and include them in the generated handouts.
  - look into extracting the text in the video and adding in timestamps.
  - 2 options:
    - single camera for the classroom.
      - possibly broadcast capabilities for remotely sending the transcripts somewhere.
      - would need 180 degree camera or adjustable position.
      - 2 medium res cameras or one high resolution one.
      - look at existing solutions as well as the software required such as the OWL.
      - need some way to check the video feed in case adjustment is needed.
    - portable device
      - would want a camera that can track footage on different parts of the board.
      - take snapshots at certain times.
      - would want a couple buttons on the device to control it (dpad with center button).
      - small screen of some sort for output. (text only display possibly).
      - local memory for storing the footage.
      - possibly enough compute for video analysis built in.
      - could add a microphone to generate the transcript as well.
      - where would the device be placed.
      - need some way to offload the footage and information (wireless or wired connection).
- microphone system to take in lecture audio as clearly as possible. Probably a directional microphone array.
### Other Components
- Need to build out data of lecture transcripts and their core concepts. This involves collecting course transcripts then going through them and identifying their core concepts. This also involves annotating questions and the answers to those questions. Will also involve looking for pre-existing datasets. This should be under [milestone 1](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/milestones/1#tab-issues) as [issue 2](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/issues/2)

### Appropriateness for a Culminating Experience in Engineering
#### How are Engineering Standards and Constraints in Effect
Engineering standards and constraints are in effect. We are working with a multitude of constraints for the project. Some of them are listed below:
- We must develop a hardware product that has similar performance to the OWL device
- The developed device must be significantly cheaper than the OWL device
- The developed device should be able to record and or take pictures of the board
- the pictures and or video must be clear and legible
- The audio must be clear and or legible
- The software application must be easy to use
- The software application must have a remote frontend, able to run on another machine from the backend
- The software frontend must securely communicate with the backend
- The application should have little to no vulnerability to some of the major attacks defined by OWASP.
- The Machine Learning model must extract topics and keywords from text
- Topics and keywords must make sense based on the context of the document
- The Machine learning model must extract summaries from text
- the summaries must make sense and be based on the text
- the summaries must be short enough to be counted as a summary
- The machine learning models must run quickly as to not take up a lot of processing time.
- Another key constraint is that we cannot access most official standards like the ISOs without paying hundreds of dollars.

The project also takes into account some engineering standards. These are technical documents that define established norms and or requirements, defining methods, processes, and practices. Because our project is not funded or sponsored by any company, our standards are ones that we selected ourselves. This section had some complications due to many of the standards such as ISO standards not being able to be read until bought. 

The following is a list of some of the more formal standards that we are attempting to follow:
- [HVEC H265 Video Encoding RFC](https://www.rfc-editor.org/rfc/rfc7798.html) or from the [ITU](https://www.itu.int/rec/T-REC-H.265)
- [Internet Audio Codecs RFC](https://www.rfc-editor.org/rfc/rfc6366) mostly useful for describing delay metrics.
- [OPUS Interactive Audio Codec](https://opus-codec.org/) or as [RFC](https://www.rfc-editor.org/rfc/rfc6716)
- [Audio and Video Conferences RFC](https://www.rfc-editor.org/info/std65)
- [Video Transcripts W3](https://www.w3.org/WAI/media/av/transcripts/)
- [Transcription Formats](https://www.rev.com/blog/resources/transcript-file-formats-guide-to-different-transcription-formats)
- [HTTP3 Websocket Protocol RFC](https://www.rfc-editor.org/info/rfc9220)
- [Time Protocols RFC](https://www.rfc-editor.org/rfc/rfc868.html)
- [UUID RFC](https://www.rfc-editor.org/rfc/rfc4122.html)
- [Internet Authentication Information RFC](https://www.rfc-editor.org/rfc/rfc1704.html)

The following is a list of some of the more informal standards that we are attempting to follow:
- [General Standards Overview](https://people.duke.edu/~goodw010/Wiki/hwswstds.html)
- [Some Informal Hardware Interface Standards](https://informerguru.com/hardware-interfaces-in-computer-system/)
- [NEMA American National Standard for Electric Power Systems and Equipment - Voltage Ratings](https://www.nema.org/docs/default-source/standards-document-library/ansi-c84-1-2020-contents-and-scope8cb6b1da-0402-4cde-a8ad-83177d02ae0f.pdf?sfvrsn=cb66d1e6_3)
- [Standard Website Login](https://blog.loginradius.com/identity/what-is-standard-login/)
- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [Data Storage Standards Summary](https://www.enterprisestorageforum.com/management/7-essential-compliance-regulations-for-data-storage-systems/)
- We could not find any standards for natural language processing


#### How is this Based on Knowledge and Skills from Earlier Course Work
Much of what we are attempting in this project is based off skills from our earlier course work. For example, the Hardware team is practicing what they learned in their classes about designing PCBs and how to choose appropriate hardware components. The Software team is practicing how to develop an application and identify constraints along the way that will impact the application. This also involves designing a user interface, planning modes of operation, and planning communication. The Machine Learning team is practicing what was learned during course work, and expanding into areas we did not cover in course work. The ML team is using the data collection, data cleaning, and researching practices from course work and then expanding to apply this to natural language processing which was not covered in course work.

## Project Technologies
This section will be filled in with more detail upon the completion of the [Technology Report](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/Technology-Report).
### Projected Hardware Requirements
- A microphone to accurately record lectures and other audio.
- A video camera to record lecture notes on whiteboards.
- Attempt to build a cheaper version of the OWL that is more focused on note taking.
  - mobile module that is not built into the room and could be placed at front and center in the room or on the podium at the front.
  - Test lapel microphones.
### Projected Software Requirements
- May need to learn another GUI language if android app is wanted (QT C++ or QT Python probably)
- Python language for ML
- OCR and Tesseract along with handwriting processing / other image processing software.
- Driver code for the hardware
- Database software such as MongoDB / MySQL / DynamoDB
- Backend Language C++ / Java / NodeJS
- Location of ML algorithm running: AWS / other cloud software options / local server / local device.
- Frontend Language JavaFX / QT C++ / Web (ie HTML / CSS / React / Agile ) / QT Python
- Audio processing software
- Unit testing software: squish?
### Projected Assistance Needed To Learn Required Hardware & Software
- self:
  - Research sources and other sources of information. ie who to ask.
  - Catch up meetings / meetings to understand what the code is doing (code reviews?)
  - teach others / provide and share info.
  - Possibly search for YouTube tutorials.

### Estimated Budget
#### Hardware Budget
- Unknown. Depends on ideas for hardware and their feasibility. 
#### Software Licenses Budget
- possible cost if transcription / voice to text software is required.
- $0. Probably do not need any software licenses at this time
#### Software Server Budget
- $0. Probably do not need any servers at this time. Grant has a few spare computers that could function as a server for testing if needed
#### Software Web Hosting Budget
- $0. Not planning a web app for now. May change depending on goals of the project
#### Software Paid Developer Accounts Budget
- $0. Should not need any paid dev accounts
#### Marketing Materials Budget
- $0. Should not need any marketing for now
#### Other
- $0. No other anticipated expenses at this time
#### Total
- $Unknown. Depends on hardware budget

## Preliminary Development Plan
### Pre-Sprint 1
#### Goal
*prepare for the first sprint*
#### Main Work Required
- [x] determine primary project idea
- [x] determine secondary project idea
- [ ] complete the project proposal
- [ ] complete the week 2 status report
### Sprint 1
#### Sprint Goal
*Start data collection and preprocessing, build wireframes, minimally viable product requirements, and construct the software framework.*
#### Main Work Required
- [ ] Begin building up the sample data
  - [ ] Collect transcripts and other pieces of text
  - [ ] Read through the transcripts and try to pull out what the core concepts are
  - [ ] Figure out how to highlight questions in the text
  - [ ] See if grouping the text by word occurrence or word length is helpful at all
  - [ ] Investigate if any existing datasets exist.
- [ ] Investigate semantic analysis algorithms
- [ ] Investigate Schank's story computers as they may be helpful in understanding text
- [ ] Investigate text analysis tools
- [ ] Determine what Languages and Frameworks are required
- [ ] Determine the low and high-fidelity designs for the computer application 
- [ ] Determine and setup a microphone system for audio recording
### Sprint 2
#### Sprint Goal
*Finish collecting enough sample data to begin training some models*
#### Main Work Required
- [ ] Continue data collection
- [ ] Investigate what models show promise for text analysis
- [ ] Use the core concepts from the sample dataset to do something with the app
- [ ] Create a skeleton software framework
- [ ] Spikes for research on aiding students with neurodivergent needs
- [ ] *TODO*
### Sprint 3
#### Sprint Goal
*Begin training and comparing models.*
#### Main Work Required
- [ ] Begin training models
- [ ] Determine which models are more accurate and which are less accurate
- [ ] Attempt to determine how to improve models
- [ ] Begin getting core concepts back as a result of models
- [ ] Start integrating the core concepts from the model results into the app
- [ ] Deciding the database architecture/management
- [ ] Achieve a minimally viable product for the compute application user interface
- [ ] *TODO*
### Sprint 4
#### Sprint Goal
*?*
#### Main Work Required
- [ ] Begin getting back sentence / text groupings based on transcripts
- [ ] Creating a database
- [ ] Achieve a minimally viable product that connects the UI to the database
### Sprint 5
#### Sprint Goal
*Work towards correcting data collection for transcripts. Load data into software that generates note cards, work sheets, and other defined study materials.* 
#### Main Work Required
- [ ] Clean up and improve the returned text groupings and core concepts from models
- [ ] Achieve a minimally viable software product
- [ ] Communicate with the database to load in information for note cards
- [ ] Communicate with the database to load in information for work sheets
### Sprint 6
#### Sprint Goal
*Get part of a working version of the project deployed in some form of classroom environment for testing*
#### Main Work Required
- [ ] Record findings on actual test cases
- [ ] Measure accuracy of the transcripts collected
- [ ] Write tests
### Sprint 7
#### Sprint Goal
*?*
#### Main Work Required
- [ ] make improvements based on the test case findings
- [ ] Work on tests
### Sprint 8
#### Sprint Goal
*Finish up and polish the project*
#### Main Work Required
- [ ] Final clean up and improvements
- [ ] Production ready project


# Secondary Project: Webcam Gesture Control
## Project Description
### Projected Client, Customer, or End User
People who want touch-free ways of interacting with technology, which is relevant with Covid and other diseases. People who want to try new technology. People who operate in areas where devices need to be sealed. More complex interaction. Companies looking to minimize exposure risk through the reduction of contact with surfaces.

### Project Stakeholder
None

### Problem Being Solved
This problem aims to assist in the operation of computers in environments where it is not feasible to type on a keyboard. Examples of such environments could be sterile rooms or locations with a lot of particulate. In these cases it would help to prolong the life of the device and reduce contagion by being able to operate the computer through gesture controls. The goal of this project, is therefore, to allow for the full control of the operating system and inputs of a computer using only gesture controls.
### Possible Software Component
- reading the gestures from the video feed
- interpreting the gestures
- controlling the operating system as a result of gestures
- allowing for inputs as the result of gestures
- may want to expand for multiple operating systems
### Possible Hardware Component
- may need a custom camera or other such hardware to be able to read depth on the video feed.

## Project Technologies
### Projected Hardware Requirements
- camera for depth reading.
- Investigate using use of normal webcam or xbox kinect
### Projected Software Requirements
- Use ML and AI to recognize gestures
- Driver code for the custom camera
- Software to bridge gesture interpretation and the OS
### Projected Assistance Needed To Learn Required Hardware & Software
- None

### Estimated Budget
#### Hardware Budget
- Max $300 for cameras. (possibly more budget depending on how much compute is needed for gestures. do not want to send gestures remote for privacy reasons)
- Possible budget for processing the video locally to ensure privacy.
#### Software Licenses Budget
- May need a software for camera depth reading (research needed)
- may need software for security (research needed)
#### Software Server Budget
- $0 (Should run on any pc)
#### Software Web Hosting Budget
- $0 (should not need a web app for privacy reasons)
#### Software Paid Developer Accounts Budget
- $0 (probably do not need any accounts)
#### Marketing Materials Budget
- $0 (probably do not need any marketing)
#### Other
- $0 (no additional expenses foreseen at this time)
#### Total
- $300+ depending on cameras, compute requirements, and any security solutions
