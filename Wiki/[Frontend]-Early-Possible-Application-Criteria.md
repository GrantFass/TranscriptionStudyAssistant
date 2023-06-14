View Criteria
- want to support widescreen and ultra-widescreen.
- Should be able to scale to other resolutions
- Should be able to operate in vertical or horizontal.
Possible Features
- Settings menu cog
  - font options
  - font size options
  - theme options
- Hamburger Menu
  - To hide the options possibly? may not be necessary as it increases the number of clicks to actions.
- Text Input:
  - Should be able to upload singular text files
  - Should be able to upload a folder of text files
  - Possibly allow upload of other formats such as JSON, doc, docx, or pdf (look for libraries like Commons CSV)
    - JSON should be the format for documents we have already processed probably.
  - Should be able to just paste text directly into the software somewhere
  - Should have the option to add a filtering tag to the imported documents.
- Video/Audio Input:
  - Should be able to upload video MPV4 File of Lecture
  - Should be able to upload MPV3 File of Lecture
  - Should be able to convert the lecture's audio to text (there should be APIs to do this)
  - Allow a toggle option to take images from video of the board
- Processing:
  - Check that the file to be processed does not already exist in the output directory (levenshtein distance). If so create a warning and ask for overwrite perms.
- Output:
  - View of transcript
    - Allow for Ctrl+F of document
  - Process the text document. The results of the ML model should be stored to a JSON file.
    - do we want to store the document text as well?
    - make sure to store the processing tag
    - set the filename to the same as the input file but as a .json instead of a .txt
    - Summarize the core lesson concepts
- Notes
  - Build notes from the transcripts and include the images
  - [ocr / handwriting scanner](https://towardsdatascience.com/https-medium-com-rachelwiles-have-we-solved-the-problem-of-handwriting-recognition-712e279f373b)
  - Full markdown editor support?
- Quizzes / flashcards
  - Option to quiz on just one text file
  - Probably want minimum length for the text file
  - questions should be related to the topics in the file
  - Option to quiz on any files with a specific filtering tag
  - Option to quiz on all files
  - allow the modification of cards / questions

![image](/uploads/115320b0af712e2fbb4cae0c4def515b/image.png) Import window example

actually we probably do not need an export option on the sidebar at all since the output files would automatically be exported after they are processed...

We may need a sidebar option for a timer if processing locally takes a lot of time.

We may end up keeping the output sidebar option in order to output generated quizzes if we want... It may be easier to keep the quizzes in application (if export they would be as pdf? or just a txt file?)

settings menu should have an option to browse local files directly?

there should be a help / about menu. Possibly launch a shortened version of this on application startup?

may want separate tabs for flash cards and for quizzes? or just show flashcards in the app and export the questions as quizzes?