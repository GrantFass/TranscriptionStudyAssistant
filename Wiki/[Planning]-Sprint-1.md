# Sprint Goal
***Fill out the Tech Report***

## Sub-Goals
- Perform an investigation of the OWL device.
- Send out an email to instructors to ask for transcripts
- Perform a customer discovery survey
  - CS / SE department
  - CACEM department
  - Math department
  - Teachers from other schools if applicable
  - Students
    - could ask in person in social spaces
    - could ask in the MSOE discord
  - Survey: QR code survey.
    - could ask just students in general, not just from MSOE
- Investigate semantic analysis algorithms, Schank's story computers algorithm, text analysis algorithms, NLP algorithms, etc.
- Determine the target platform, what frameworks, what databases, what languages, etc. (add to tech report)
- Investigate how to link machine learning models and other pieces of software like the core app.
- Identify security concerns.
- [Low Priority] Mock up some GUI wireframes.
- Outline and Refine hardware requirements and components.

# Priority Ordered List of PBIs
This list is ordered from highest priority to lowest priority

## [Investigate the OWL Device](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/issues/1)
### Story Points: $`5`$
### Value Gained:
This will help give insight into how to design our own device so it is not as similar and has obvious benefits. Would help realize what problems we may run into when building our own solution.
### Subtasks:
- [ ] Reach out to Dr. Durant for hands on access with the device.
- [ ] Determine the cost of the device.
- [ ] Identify what features the device has.
- [ ] Identify benefits from the device over just a laptop at the front of the room. (i.e., sound quality, video quality, etc.)
- [ ] Identify benefits from the device in audio quality when compared to a desktop microphone like a blue yeti.
  - Test different ranges of sound and at different distances. Perhaps record measurements in decibels and frequency.

## [Collect and Prepare Transcripts](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/issues/2)
### Story Points: $`30`$
### Value Gained:
This helps build the required data for the machine learning models.
### Subtasks:
- [ ] Send email to faculty asking for transcripts and potentially videos from online classes
- [ ] Ask professors if you can record class sections that you are in for more data.
- [ ] Ask instructors what the goals of a specific lecture were.
- [ ] Skim transcripts to identify more goals of the lectures.
- [ ] Export each transcript and concepts of the transcript, to json.
- [ ] Investigate if there are any existing datasets like this, even if they are loosely related NLP databases.

## [Determine Software Infrastructure](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/issues/3)
### Story Points: $`15`$
### Value Gained:
This will help identify pros and cons of our possible software stack and help to determine what to use.
### Subtasks:
- [ ] Investigate possible target platforms such as windows apps, web apps, mobile apps, etc.
- [ ] Investigate what database solutions would be useful.
- [ ] Investigate what frameworks would be useful.
- [ ] Investigate possible languages.
- [ ] Evaluate and identify security concerns.
- [ ] Investigate what languages link well with machine learning models.

## [Perform a Customer Discovery Survey of Teachers](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/issues/4)
### Story Points: $`10`$
### Value Gained:
This helps build the required data for the machine learning models.
### Subtasks:
- [ ] Determine what questions to ask the teachers
- [ ] Reach out and meet with teachers of CS / SE department
- [ ] Reach out and meet with teachers of CACEM department
- [ ] Reach out and meet with teachers of Math department
- [ ] Reach out to teachers of other schools and / or departments if applicable

## [Perform a Customer Discovery Survey of Students](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/issues/5)
### Story Points: $`5`$
### Value Gained:
Identify student needs and concerns to help make something that will help them learn better.
### Subtasks:
- [ ] Determine what questions to ask students and build an online survey of some sort. Try to use non-NLP questions.
- [ ] Reach out to students on campus.
- [ ] Reach out to department head and see if they could send the survey out. May require asking other department heads and or student life on campus. Doctor Sohoni may have more information.
- [ ] Consider the benefits of collecting responses over discord.

## [Analyze the results of the customer discovery survey](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/issues/6)
### Story Points: $`5`$
### Value Gained:
This needs to be done so we know what the results of the survey are.
### Subtasks:
- [ ] read through and collate results.

## [Mock-up Possible GUI Design & Wireframes](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/issues/7)
### Story Points: $`5`$
### Value Gained:
This will help by thinking of what functions will be possible in the final product and how the user may interact with those functions.
### Subtasks:
- [ ] Identify what functions the program will have.
- [ ] Come up with ways to interact with those functions.
- [ ] Design possible wireframes for the gui.

## [Investigate Possible ML Algorithms](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/issues/8)
### Story Points: $`10`$
### Value Gained:
This is required so we know what models we may end up using as well as what sort of hardware limitations will be in place based on the models.
### Subtasks:
- [ ] Look into Schnack's Story Computers and other story analysis models
- [ ] Look into semantic analysis algorithms
- [ ] Look into NLP models
- [ ] make sure to look into training compute requirements, inference compute requirements, and model storage requirements such as number of parameters.
- [ ] Determine pros and cons of different NLP models and approaches.

## [Refine Hardware Design Decisions](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/issues/9)
### Story Points: $`30`$
### Value Gained:
This is required to determine how to build the hardware device and if it is affordable.
### Subtasks:
- [ ] Outline and Refine Possible Hardware Requirements & Components.
- [ ] Determine how to package the product.
- [ ] Determine if existing devices work such as webcams and desk microphones
- [ ] Determine if we need to build a device.
- [ ] Determine if we need to design our own PCB for it or if we can use Proto-Board.
- [ ] Determine how a built device would be interfaced with via code.
- [ ] Determine how a built device would be interfaced with via hardware.
- [ ] Identify other hardware requirements such as data transfer rates, cpu speed, and other minimum hardware specs.
- [ ] Identify expected cost of the device to make and prototype.
- [ ] Identify what improvements would be made over existing devices.
- [ ] Identify possible supply chain issues with parts (digikey vs. black key sites).

