[[_TOC_]]

## Hardware
The main goal of the hardware team is to construct a custom device. This device must be able to record audio and video. It should also be able to track the motion of the instructor or presenter. It should also be able to integrate with common platforms such as Microsoft Teams. We are mainly focusing on building our own device for two reasons. The first reason is the cost of simmilar units. An example is the [Meeting Owl 3](https://owllabs.com/products/meeting-owl-3) which is upwards of $1000. The second reason is to gain experience in the process of developing hardware devices with audio and video capabilities.

The goal of creating a custom device resulted in a number of concerns at the start of the project. These concerns, as well as how they were addressed, are listed below:
- Budget 
  - Individual parts were actually quite cheap. Biggest expense is the time for development.
  - See [Bill of Materials](Project BOM)
- Supply-Chain & Delayed Shipping
  - Ended up being a non-issue. Parts shipped in 2-3 weeks mostly. Ended up arriving a sprint after we placed the order basically.
- Budget vs. Quality Balance
  - Also a non-issue. Ended up investigating multiple parts and picking what we thought was best.
  - See [[Justification] Building Our Own Device]([Justification] Building Our Own Device)
- Building Our Own Device vs. Buying One
  - Ended up deciding to build our own device. Decision was made mostly for cost and experience reasons.
  - See [[Justification] Building Our Own Device]([Justification] Building Our Own Device)
- Completion Time
  - This is still an active concern for the project. Building our own device is very involved. We are doing our best to complete everything in a timely manner.

## Software
The main goal of the software team is to construct a web application and backend. The backend must serve responses to requests sent from the frontend. The backend should be implemented with REST endpoints and documented in an API. The backend should be able to serve responses to machine learning type queries such as summarization and topic modeling.

The goal of creating a website resulted in a number of concerns at the start of the project. These concerns, as well as how they were addressed, are listed below:
- Website vs Thick App
  - Decided to go with a website as it was more relevant.
  - See [[Justification] Application Type]([Justification] Application Type)
- Picking Proper Frontend Language
  - Decided to use Angular
  - See [[Justification] Frontend Language]([Justification] Frontend Language)
- Picking Proper Backend Language
  - Decided to use Python
  - See [[Justification] Backend Language]([Justification] Backend Language)
- Data Storage
  - Decided to use an object store called MINIO
  - See [[Justification] Data Storage]([Justification] Data Storage)
- Unit Tests
  - Still has not been fully decided> This is because we have not reached this stage of implementation yet.

## Machine Learning
The main goal of the machine learning team is to support the primary functions of the software application. This means that the machine learning team must handle text summarization, topic modeling, keyword modeling, voice to text transcription, and question extraction.

The machine learning goals outlined above resulted in a lot of concerns at the start of the project. These concerns all stemmed from the difficulty of these tasks as well as our inexperience. The concerns, as well as how they were addressed, are listed below:
- Text Cleaning & Preprocessing
  - Had to figure out what this entailed, what it meant, and where it would be used.
  - Created a working preprocessing script that has been evolving over time to fit the application needs.
  - See [[Justification] Text Preprocessing]([Justification] Text Preprocessing)
- Text Summarization
  - Had to determine how to perform text summarization.
  - Had to choose between abstractive and extractive text summarization.
  - Ended up performing extractive text summarization using transformers.
  - See [[Justification] Text Summarization]([Justification] Text Summarization)
- Keyword Modeling
  - Had to figure out what the domain of topic modeling entailed and why only keywords could be returned.
  - Ended up implementing using Latent Dirchlet Allocation.
  - See [[Justification] Keyword Modeling]([Justification] Keyword Modeling)
- Topic Modeling
  - Had to determine a method of matching documents or sentences with predefined topic labels. Originally thought we could do this using LDA. This was determined to not work since LDA only does keyword modeling.
  - Started investigation on an approach using graphical machine learning.
- Question & Answer Formation & Extraction
  - For research, see [[Investigation] Question Answering Research]([Investigation] Question Answering Research)
- Sentence Importance Extraction
  - Planned to implement this using abstractive text summarization classes from GENSIM. We determined that these classes are depreciated so we would need to recreate it ourselves.

## Datasets
This project needs a good amount of sample data to practice with. This data is also used to train some of the machine learning models. The collected datasets are outlined below:

- Khan Academy Dataset
  - Collected by using Beautiful Soup to scrape their lessons and lectures.
  - This is a supervised dataset because we can use some of the features as labels.
- Ted Talks Dataset
  - This dataset was found online through [kaggle](https://www.kaggle.com/datasets/rounakbanik/ted-talks).
  - This is an unlabeled and thus unsupervised dataset.
- MOOC lecture Dataset
  - This is a dataset of word embeddings and topic vectors.
  - This dataset was found online through [kaggle](https://www.kaggle.com/datasets/saurabhshahane/mooc-lecture-dataset).
  - We have not used this dataset for much other than preliminary investigations for now.
- MSOE Lecture Transcripts
  - These are collected manually from some of the classes held over Microsoft Teams at MSOE. These are in a vtt file format. We primarily used these to make sure the preprocessing pipeline can handle vtt files.




























