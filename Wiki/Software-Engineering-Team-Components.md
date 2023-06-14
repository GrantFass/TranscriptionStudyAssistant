## Table of Contents
[[_TOC_]]

## Requirements - Definition and analysis including selecting at least one stakeholder. You will need to become familiar with the domain.

This project aims to create a tool that will assist with studying. It can help with recording lectures, summarizing transcripts, and even extracting keywords from those transcripts. We are creating a hardware device simmilar to the [Meeting Owl 3](https://owllabs.com/products/meeting-owl-3). We are attempting to create our device for about $\frac{1}{8}$ the cost of the Meeting Owl 3 device. This device will be able to record lectures through video and audio. It should also be able to track presenters as they walk around. The meeting audio could then be turned into a transcript using a popular software such as Microsoft Teams. We are planning to add in-app support for this in the future as well. The transcripts could then be uploaded to our app for processing. The processing extracts topics, keywords, and summaries from the text. We are investigating building out a question and answer system as well. Some of the projects key domains are as follows:
- Embedded Systems Creation and Analysis
- 3d Modeling and Assembly of Design
- Software Application Creation
- Web Server Creation 
- Data and Communications Security
- Text Summarization using Natural Language Processing and Transformers
- Topic Modeling using Natural Language Processing and Latent Dirirchlet Allocation
- Question Extraction using transformer text masking, vector analysis, and more

Stakeholders:
- We are our own project stakeholders as we do not have any corporate sponsors.
- Instructors and students may also be considered stakeholders because the outcome of this project will impact them. The goal of our product is to improve the classroom environment by providing a device that supports an instructor with their lectures and students with their notetaking/studying. Even though they are not personally funding our project, they do benefit from our project being successfully completed.

## Software Architecture and Modeling - It should involve some interesting elements of software system design, including thoughtful exploration of the architecture to support iterations.

One of our main goals on the software side of this project was to make sure that all of our work was documented and repeatable. This helps to make sure that our code base can be expanded and improved in the future. This also helps to plan out and anticipate changes that may be needed before programming is started. We had a few modeling and prototpying issues that assisted us with this process. The [Technology Report](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/Technology%20Report) documents a lot of the research that we completed before building and integrating subsystems. Additionally the backend of the application was planned out in the [[Documentation] API Communication Protocol](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/%5BDocumentation%5D%20API%20Communication%20Protocol). This API document outlines every endpoint in the backend. This includes expected communication, format, and values. We also planned out what some of the frontend could look like in the [[Frontend] Possible GUI Designs](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/%5BFrontend%5D%20Possible%20GUI%20Designs) page. The hardware team did some sketches of form factor as well. These can be found in the [[Justification] Custom Device Form Factor](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/%5BJustification%5D%20Custom%20Device%20Form%20Factor) page.

## Design - Strategies employed, such as the use of patterns and allowances for evolution of the product.

In order to quickly develop software we are employing a strategy of planning out as much of the project as possible before beginning development. There are two key examples of this plan in effect as it applies to the software side of the project. The first example is the [Technology Report](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/Technology%20Report) and the second example is the software [[Documentation] API Communication Protocol](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/%5BDocumentation%5D%20API%20Communication%20Protocol) document. The hardware team is also going through a simmilar process by planning out as much of the device as they can. The machine learning team perhaps has the least amount of planning outside of the tech report. Instead the machine learning team has much more investigation to perform.

The [Technology Report](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/Technology%20Report) allowed us to investigate various aspects of the software application at a high level. We then documented all of our research. This document allowed us to easily compare and make decisions regarding what type of application we would like to create as well as what languages we would like to use. We were also able to investigate and make a decision to design the application so that there is a distinct frontend and backend. Designing the application so that most of the operation is done in the backend and communicated to the frontend allows us to avoid repeating code as well as designing the system for security. This also lets us quickly add more methods to the backend to support new operations as well as allowing for testing. This allows for an expandable software solution. 

The [[Documentation] API Communication Protocol](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/%5BDocumentation%5D%20API%20Communication%20Protocol) document allowed us to plan exactly how the messages will be formatted and sent between the software application frontend and the application backend. This concrete plan also helped us plan what features the application would support. Having distinct endpoints for each operation also lets us easily expand what operations we can support by just adding another endpoint. The well defined communication protocol allows for quick drafting of the backend endpoints to send sample messages. This helps with the development of the frontend. The protocol document also allows us to quickly check what operations are supported. This helps with determining if new operations conflict or overlap with existing operations.

The hardware team has worked on comparing and prototyping various device components. They have been determining how these components work together and what conflicts they may cause. There was a low lead time on the parts that we ordered for the device. This means that we already have most of the parts we need to assemble the device. We have also created simple 3d models of some of the components to assist with modeling the shell of the device for printing.

The machine learning team has been iterating and investigating new models. This involves performing operations, such as grid search, to help improve model performance. We also ended up scraping data from Khan Academy to assist with training some of our LDA topic models that we are using for keyword analysis. Using this iterative approach to our models lets us quckly determine which works best in our specific enviornment and use cases.

## Testing - Building it to be testable and testing it. How good is the automation of the testing and was it considered from the beginning?

As of the second quarter we still have few testing practices in place. This is mostly due to our implementation running behind where it should be. Most of our current testing is being performed manually on an as needed basis. This involves tools such as [Postman](https://www.postman.com/downloads/) for the backend. THe backend is currently being implemented using as much of the DRY principle as possible. Additionally, all of the backend endpoints expected inputs and functionality are already documented in the [[Documentation] API Communication Protocol](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/%5BDocumentation%5D%20API%20Communication%20Protocol). This means that creating unit tests should be relatively expedient. It also means that testing one method should result in fairly high code coverage during testing. Testing in the backend also means that we do not have to worry about the GUI either. The machine learning team is somewhat testing models as they train them over time. The hardware team is also testing components that they purchased for the device.

One possible method of future communication testing would be a message simulator. This would be a separate application that recieved communications and sent back sample responses. Each message could then be passed through JSON schema validation to ensure that all data was present and properly validated. This is more useful for testing backend endpoints without building out entire frontends. Due to the scale of our development this is no longer necessary or feasible from a time perspective though.

The hardware team started out by running some tests for microphones and comparing their performance against the OWL device as a baseline. We also ran tests against the camera of the OWL device and recorded data to use as a baseline for future hardware testing. This testing is recorded in the  [Investigate the OWL Device](#1) issue. The hardware team is currently investigating the camera, and motors. They have already partially investigated the microphones and found that we need an amplifier to assist with their operation.

The machine learning models are mostly being tested on a visual basis by comparing the input and the output manually. This is because we are working with unsupervised data. That means that the data does not have any sort of 'ground truth' recorded with it, so we have nothing to compare to. This mainly has resulted in us training models and comparing their output against what we expect them to output.

## Security and Privacy - How are you addressing security and privacy? Are you using best practices?

We are attempting to address security and privacy in our design. This has been one of our core concerns from the start of the project as we will be dealing with audio and video recordings. This concern has been present throughout our technology investigation to our design. Some of the decisions it influenced was what type of application we would like to support, where data processing was performed, the connection and interfacing options of the hardware device, and the ability to login to the software. 

We are currently working on making sure that the data that we communicate between the frontend and the backend is communicated securely and can only be accessed by the proper user that is logged in to the application. We are also planning on implementing various connection methods for our hardware device so that we can allow the user to choose how they connect to the device. Additionally we are thinking about physical switches on the device to disable the microphones, cameras, and possibly all wireless and or internet communications. This allows users to ensure that the device is not broadcasting anything when it is not supposed to be in use. 

We are also looking at various methods of securely storing the data required for the NLP algorithm such as storing the text only on the users PC or browser and just having the backend do processing on this text. Additionally, we are planning on designing and testing our program against some of the attacks from the OWASP top ten to help ensure the security of our application. We will also plan on running tests against other metrics and security suites once we have more of the device designed.

## Tools - Good use of development, testing, and management tools (including GitLab).

We currently are using GitLab and its wiki for the majority of our management of the project. We are using it to store all of our code, information, and investigations. Additionally, we are using Microsoft Teams to communicate and coordinate our work when we are unable to meet in person. As for development tools we are using a multitude of different software depending on what we are working on. Some of the tools we are using and or plan to use are as follows:
- Notable and Obsidian for editing markdown documents
- Jupyter Notebooks and Visual Studio Code for modifying notebook files
- QT Creator for testing QT C++ code during prototyping
- ~~Node-Red for building a quick and dirty JSON communication simulator with schema validation~~
- Microsoft One Note for creating simple drawings and sketches such as the device drawings
- Microsoft Teams for communicating both among the students and with the instructor
- GitLab for storing code and information, including the wiki
- Autodesk Inventor, Solidworks, and/or OnShape to create a 3d model of the device and export it to a stl file
- Cura 3d slicing software set to work with Ender 3 Pro printers with special GCODE arguments to support a BLTOUCH automatic bed leveling sensor running custom firmware. This is used to print the shell of our device
- Other various IDEs for designing prototypes of our software application
- [JSON Compare Website](https://jsoncompare.com/#!/simple/fullscreen/) for unwrapping JSON and expanding it to a multiline format which is easier to read.
- MSOE Canvas and Dr. Taylor's website for specifications
- Other webpages as needed for investigation and examples such as DigiKey, Geeks4Geeks, and TowardDataScience.
- ~~Possibly Froglogic Squish if we find the need to create integration tests for our GUI. May not end up using as it may require a licensing fee.~~
- ~~Possibly MySQL or other databases if we decide we need to use a database. We are trying to avoid remotely storing data though for security, storage, and cost reasons.~~
- MINIO object store
- Other tools as needed.

## Experimentation and Prototyping - Applied to unknown technology to improve knowledge and reduce risks. As the architecture is developed and key mechanisms are determined, what risks arise and how will you address them in the development process?

We are using a lot of unknown and unfamiliar technology for our project. Every component of our project involves something that is unfamiliar in some way shape and form. This learning about new ideas is one of the core parts of our project. Each of our three teams is working on something unfammiliar.

The hardware team is performing a lot of investigation into components that they are not familiar with such as motors, cameras, and microphones. One of the key risks for the hardware team is getting all of the hardware to work together in tandem without causing any interference or power draw issues. We are planning on addressing this through prototyping various options while researching as much information as possible during the design phase. We then plan on testing the device as much as possible to make sure that there are no major issues. 

The software team is also working with unknown technology. One of the examples of unknown technology is the language being used in our application. Our two primary picks for the application were angular and QT C++ with Webhooks. Both of these were new to our software team and required investigation. This involved learning how they operate and building prototypes. A key risk with this is making sure that the software team gets a good feel for, and understanding of, the language during the prototyping phase as this language will be used for the rest of the project. We addressed this by building expansive prototypes and making sure that enough time was allocated so the team can get a good feel for the language in use. This resulted in choosing Angular as our frontend language of choice. Another unfamiliar software aspect is building security into the application. This is a very critical component of our project. As such we are planning on allocating as much time as we can for integrating security by following tutorials and learning about common vulnerabilities. One of the sets of vulnerabilities we plan on addressing is the OWASP top ten which details common security issues and vulnerabilities for applications while detailing how to solve some of them. 

The machine learning team is working entirely with unknown technology. The team is unfamiliar with natural language processing tasks as it was not covered in the curriculum at MSOE. Additionally, much of this field is cutting edge graduate level research. This means that many research papers must be read to try and get an understanding of how to approach our problems with topic modeling, text summarization, and question extraction. Some of the risks include improper budgeting of time, misunderstanding how the models work, not implementing secure versions of the model, and improperly storing data. Unfortunately not all of these risks can be mitigated at this time. We are trying to avoid improperly storing data by not storing any data and training as much as we can on publicly available data sets. We are trying to avoid implementing insecure versions of the model by using standard models where possible and investigating how they work to attempt to understand and identify security flaws. We are also trying to understand how the models work by following implementation tutorials and reading associated research papers about the models.

## Third Party Components - Demonstrate your skill in discovering and employing third party components.

We are not fully sure what sorts of third party components we will be using in our project yet. One of the key considerations when choosing a third party component is understanding what it is doing and how. This is important so that we do not introduce security and or privacy vulnerabilities into our device and application. 

The hardware team is attempting to avoid this risk by ordering parts from trusted suppliers such as DigiKey where possible. They are also trying to mitigate vulnerabilities by researching all of the parts they plan on ordering in depth. This involves looking at pinout details, voltages, and more. Some times this may include looking at reviews for more popular components on forums and other sites as well.

The software team is trying to avoid this by implementing most of the application without third party libraries unless methods are overly complex and can be performed quicker with a third party library. An example of this case would be using a library to read data from a pdf file if we determine we would like to support that file type. By implementing most of the application ourselves we can ensure the quality of the code and make sure it is properly run through unit tests. We can also run better evaluations for the security of the methods. The Python backend for the application is using some libraries, but they are widely used and trusted libraries.

The machine learning team is probably the most at risk for vulnerabilities in libraries as they are the most likely to use external libraries and components. This can be avoided by using industry standards and standards taught in class where possible such as Pandas, Numpy, Seaborn, and SciKitLearn. Unfortunatly the NLP tasks cannot be easily implemented with these libraries alone and require other external libraries. Some of the other external libraries are Gensim, HuggingFace, SpaCy, NLTK, wordcloud, and PYLDAvis. Many of these are imported into the application for the prototyping phase. We are trying to mitigate risk of external libraries through two main strategies. The first is to use popular and documented libraries that are referred to in both research papers and articles. Secondly we are going to try and parse down our imports as much as possible for our actual product to leave as few open libraries and ports as possible. For example, if we only need the LDA class out of GENSIM then we should just import that instead of importing all of GENSIM. This has the added benefit of making the memory and storage usage smaller.

## Documentation - This takes many forms including continuous documentation such as, notes associated with tasks that our updated regularly, weekly reviews, sprint reviews, and other artifacts such as a technology report, discussions of where you achieved specific course outcomes, project presentations, poster, and final report.

Much of the project has been spent on documentation so far. This is mainly due to the investigative nature of most of the tasks we are attempting to accomplish. This documentation primarly lives under the [Technology Report](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/Technology%20Report) which is located in the team wiki on the GitLab repo. This document includes specific examples, prototypes, and alternatives for nearly every choce that we have made during the prject. The software portion of the project additionally has the [[Documentation] API Communication Protocol](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/%5BDocumentation%5D%20API%20Communication%20Protocol). This documents how the backend of the application is expected to operate.

We also perform weekly documentation of our progress. This includes where our time was spent, what meetings we attended, and what was said in thos meetings. These are located under the weekly status reports. We also document what issues will be in each sprint and the outcomes of each sprint. These are the Sprint Planning and Sprint Retrospective documents.

The last piece of documentation that we have is the preference polls that we sent out using Qualatrics. These documents were created in order to help poll students and instructors at MSOE. The main goal of this polling was to determine if our device would meet the needs of students and instructors on campus.It also helps to identifiy what areas of our device may need improvments.

## Managing Risks - Strategies employed to manage risk.

We follow a few main strategies for managing risk. The first step is always to identify what risks may be possible. This is primarily done through reading documentation and papers that detail what risks may be possible. In-depth tests of prototypes are also going to be performed to identify risks and the methods to manage those risks. Additionally some members of the team took an Information Security class which helps give a better understanding of what risks may be possible. Our first strategy is to make sure we are securing what we can and leaving as few openings as possible. This includes only importing what is necessary, segmenting operations onto different machines, not storing information we do not need, and more. The second strategy it to perform a risk and security analysis once the product is closer to completion. This involves going through security tutorials and guides and following their advice such as the OWASP top ten.

## Standards Used - Identify industry standards used in the project.

We are attempting to follow industry standards where possible. Some of these are defined standards with required documentation, others are more theoretical standards. Unfortunately, it costs a lot of money to get access to standard specification documents like ISOs so we are trying to follow what we can without buying any of these. An example is the NEMA power and voltage specification document which specifies what power ranges our device should support. Other standards that we are trying to follow include our use of language. We attempted to determine what languages are common in industry and narrowed down our choices to Angular and QT C++ so that we can try to use a more standardized language. 

The ML team is trying to follow standards for libraries by comparing against research papers and tutorials. Examples include using standard libraries from class such as Numpy, Pandas, Seaborn, and SKLearn, and also using NLP standards such as Gensim, HuggingFace, NLTK, and SpaCy. Our hardware team is attempting to follow standards based on class knowledge and other external research along with documentation from sites like DigiKey and McMasterCarr. Additionally the team is trying to follow standards found online such as the OWASP top ten, website login standards, data storage standards, and hardware interfacing standards.

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

There are also some additional standards listed under their relevant sections in the [[Documentation] API Communication Protocol](https://gitlab.com/msoe.edu/sdl/y23-senior-design/24-transcription-study-assistant/-/wikis/%5BDocumentation%5D%20API%20Communication%20Protocol).





























