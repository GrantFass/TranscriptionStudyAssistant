[[_TOC_]]

## Overview of Issues
Machine Learning (ML) and Natural Language Processing (NLP) comprise a key component of the project. In fact, the main goals of the project rely on the outputs of the NLP models being consistent and accurate. Some of our main goals with the project rely on being able to extract topics and keywords from documents as well as generating summaries of the documents. We mainly plan on working with transcripts of lectures and speeches. This also poses an issue since some lectures and speeches can be very technical in nature. Other times, a lecture will open or close with a segment on plans for the rest of the week. Both of these can pose a problem for the NLP models. We must ensure that the generated summaries are legible and can assist with learning and studying. There is also another issue that we have encountered with our project. Much of what we are attempting to do is very high level tasks that have not been covered in school. A lot of this field is cutting edge research and very proprietary. This means that many of the advised approaches are just covered in research papers and not accompanied with code snippets. This means that we sometimes must sacrifice this theoretical performance for the actual ability to implement and or understand the models. 

## Requirements List
The issues that we have outlined above lead directly into what is required of the ML and NLP algorithms. The following is a list of requirements:
1. Must be able to extract topics and keywords from text documents and or sentences.
2. Must be able to extract summaries from text documents and or groups of sentences.
3. Must be able to implement and understand the models.
4. Must have some method of comparing the accuracy of the models.
5. Topic extraction must be able to run quickly on relatively normal hardware (not ROSIE).
6. Summarization must be able to run quickly on relatively normal hardware (not ROSIE). 

Additionally, there are further requirements for the application when we take the incoming state of the transcripts into account. This following list outlines many of the preprocessing requirements.
1. Must be able to remove punctuation
2. Must be able to convert all text to the same case
3. Must be able to expand contractions
4. Must be able to convert numbers into their word form
5. Must be able to identify possible acronyms. 
6. Must be able to remove common stop words like 'the', 'and', and 'a'.
7. Must be able to perform stemming or lemmatization.
8. Must be able to perform part of speech tagging.
9. Must be able to identify frequent word combinations through bigrams and trigrams.
10. May need to be able to identify possibly misspelled words.
11. Preprocessing steps must be able to run quickly on relatively normal hardware (not ROSIE).

Furthermore, there are also requirements for the tools used to visualize the models if applicable. Due to the wide range of possible visualizations this is a short list.
1. Visualization must aid in understanding the model.
2. Visualization must not require exorbitant amounts of compute time.

## Options List
The below section outlines many of the options. We will likely end up needing to use some of these in tandem. This means we will likely end up choosing to use multiple algorithms instead of just implementing one algorithm.

### Preprocessing Tools
***[NLTK](https://www.nltk.org/)***  
- Python Library
- Stands for Python Natural Language Toolkit
- Provides text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning
- free and open source
- must be cited in documentation
- [more sources](https://www.inf.ed.ac.uk/teaching/courses/inf2a/lecturematerials/index.html#lecture01)
- one of the best known and most used NLP libraries
- older and more focused for research
- better at chatbots, language translation, and simple question answering through pattern matching

***[SpaCy](https://spacy.io/)***  
- Python Library
- Fast and Accurate
- Good Documentation
- Good error handling and validation support. Also supports python type hints
- Very easy to download, both overall and sub-packages
- Can specify various model sizes to meet performance requirements
- Supports word vectors
- has built in visualization tools
- almost all in one
- can end up consuming a lot of memory
- very user friendly
- does automatic part of speech tagging
- very easy to build preprocessing pipeline
- [more sources](https://iq.opengenus.org/why-spacy-over-nltk/)

### Possible Summarization Models
***[Word Embeddings](https://towardsdatascience.com/machine-learning-text-processing-1d5a2d638958)***  
- Words with similar meanings have similar representations
- represents words in coordinate systems
- related words are closer together
- good at processing analogies (i.e., "man is to woman as king is to what?")
- [more sources](https://iq.opengenus.org/word-embedding/)

***Word2Vec***  
- Captures meaning and good at analogy questions
- uses vector offset methods

***GloVe***  
- Stands for Global Vectors for Word Representation
- Extension of the methods behind Word2Vec
- Learns word vectors and builds word-content matrices

***[FastText](https://iq.opengenus.org/why-spacy-over-nltk/)***  
***[Continuous Bag Of Words (C-BOW)](https://iq.opengenus.org/why-spacy-over-nltk/)***  
***[Continuous Skip-Gram](https://iq.opengenus.org/why-spacy-over-nltk/)***  
***[ELMo](https://iq.opengenus.org/why-spacy-over-nltk/)***  
***Naïve Bayes***  
***Support Vector Machines (SVM)***  
***TfidTransformers***  
- Converts text into feature vectors

***[Luhn's Heuristic Methods](https://iq.opengenus.org/compare-text-summarization-models/)***  
- Term Frequency Inverse Document Frequency (TF-IDF)
- selects words of high importance based on their frequency of occurrence.
- higher weightage to words at start of document.
- lower F1 score performance for Rogue-L
- uses the sumy library.

***[TextRank](https://www.analyticssteps.com/blogs/what-topic-modelling-nlp)***  
- graph-based extractive technique for summarizing text.
- finds most relevant sentences and keywords in text.
- sentences with highly frequent words are important.
- sentences are ranked in descending order of their scores and top sentences are included in the summary.
- python gensim library.
- Unfortunately the gensim package is depreciated due to their being no maintainers.
- Also reported to not work well as implemented in gensim.
- We would need to implement our own version based on the PageRank or LexRank algorithms
- This is a lower performance extractive text summarization method
- [more about gensim](https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/)

***[Kullback-Leibler Sum](https://iq.opengenus.org/compare-text-summarization-models/)***  
- uses Kullback-Leibler divergence statistics. Often termed relative entropy and is a type of statistical distance.
- Measures how different a probability distribution is when compared to the reference probability distribution.
- Inversely proportional to the degree of similarity between source material and generated summary.
- greedy method.
- creates summary by appending sentences as long as the divergence is decreasing.
- uses the python sumy library.

***[T5 Transformers](https://iq.opengenus.org/compare-text-summarization-models/)***  
- type of neural network architecture.
- avoids using principle of recurrence.
- works based on an attention mechanism.
- allow for more parallelization than sequential models.
- achieve high translation quality after short training time.
- can be trained on large amounts of data easily.
- developed by google AI in 2020
- input and output are always strings.
- High performance abstractive Text summarization approach.
- May need to pay to use. Fortunately there are other transformer libraries such as HuggingFace for free.
- uses python transformers, sentencepiece, and torch libraries.

***N-Grams***  
- Tries to preserve contiguous sentences of n-items from text
- expands upon bigrams and trigrams
- [examples of use](https://www.dataquest.io/blog/using-machine-learning-and-natural-language-processing-tools-for-text-analysis/)

***[Latent Dirirchlet Allocation (LDA)](https://iq.opengenus.org/topic-modelling-techniques/)***  
- Finds correlations between many documents
- Can also be run over sentences
- Determine topics related to each document.
- Topics are defined by keywords
- Assumes that documents are distributions of topics and topics are distributions of words
- Uses Variational Exception Maximization (VEM) techniques
- Seems to be one of the most popular picks
- Need to tune the number of topics based on the context and requirement.
- Has both an sklearn implementation and a gensim implementation.
- can do [extractive text summarization with LDA](https://github.com/g-deoliveira/TextSummarization)
- [more sources](https://www.analyticssteps.com/blogs/what-topic-modelling-nlp)

***[Non-Negative Matrix Factorization (NMF)](https://iq.opengenus.org/topic-modelling-techniques/)***  
- Create term-topic matrix and topic-document matrix
- made of document-term matrix after removing stopwords.

***[Latent Semantic Analysis (LSA)](https://iq.opengenus.org/topic-modelling-techniques/)***  
- Extracts relationships between different words in documents.
- Helps choose correct documents
- Mostly functions as a dimensionality reduction method.
- uses SVD and the python sumy library
- [more sources](https://iq.opengenus.org/compare-text-summarization-models/)

***[Parallel Latent Dirirchlet Allocation (PLDA)](https://iq.opengenus.org/topic-modelling-techniques/)***  
- aka Partially Labeled Dirirchlet Allocation.
- Assumes that a set of n-labels exists and each are associates with topics of the overall corpus.
- topics are represented as probabilistic distribution of corpus.
- Very quick and precise compared to above methods.

***[Pachinko Allocation Model (PAM)](https://iq.opengenus.org/topic-modelling-techniques/)***  
- Improved LDA model.
- Improvises by modeling correlation between generated topics.
- Greater power in determining semantic relationship.
- Uses Directed Acrylic Graphs (DAG).


### Possible Visualization Algorithms
***Wordcloud***  
- Just a basic word cloud.
- Bigger words occur more often in document
- Easy to see what is the most common in the document

***PyLDaVis***  
- used to visualize the output of an LDA model
- shows the different topic clusters, how much they overlap, and what keywords are in them
- also shows the numeric values assigned to keywords
- interactive

***SpaCy Visualization Tools***
- useful to visualize part of speech tagging.
- requires a SpaCy document directly.

## Evaluation Options
The Machine Learning algorithms being used in this project are mostly cutting edge. Nobody on the team has experience working with NLP tasks like this either. One of the main factors we will be using in evaluating our models is whichever is easiest to implement. After we have models implemented we can narrow down our choices based on other factors such as documentation, performance, and speed. This can be summarized in the following list:
1. Can the model be implemented?
2. Does the model have good documentation?
3. Are their examples of implementations on the site or the web?
4. Can the model be trained on a 'normal' computer?
5. How fast can the model run inferences?
6. Is the model interpretable?
7. Do we have the ability to improve performance of the model by tuning hyperparameters?
8. Is the model accurate?

## Choices & Rationale
We can roughly break up our selection needs (excluding visualization) into three categories. These categories are as follows:
1. Preprocessing and general libraries
2. Text summarization libraries.
3. Topic and Keyword extraction libraries.

Most of the above model choices are purported to work for one or more of these tasks. Unfortunately, this does not appear to be the case. Or rather, we are unable to determine how to implement some of these for their specific use cases. Take for example the LDA models. These models are supposed to be able to perform extractive text summarization according to various research papers and git repos. Unfortunately they are either convoluted in approach, not very accurate, or have no examples at all. Part of this is likely due to using the wrong tool for the job. LDA, PAM, and PLDA are all supposed to be mostly used for topic modeling, and thus do not perform well for text summarization. Conversely, models such as Word Embeddings, Word Vectors, SVMs, and Bag of Words are either used for extractive text summarization or are built in as components of higher level models. For example, the LSA model utilizes SVD. Additionally, we would like to get the most accurate text summary possible. This means that we likely need to focus more on abstractive text summarization approaches instead of extractive text summarization approaches. See [this link](https://www.machinelearningplus.com/nlp/text-summarization-approaches-nlp-example/) or [this link](https://www.activestate.com/blog/how-to-do-text-summarization-with-python/) for more about the different approaches of text summarization. Most of the [popular API choices](https://www.assemblyai.com/blog/text-summarization-nlp-5-best-apis/?utm_source=google&utm_medium=cpc&utm_campaign=text_summarization&utm_term=summarize%20text%20nlp) for text summarization utilize some form of abstractive text summarization because the extractive versions do not perform well enough. This leads directly into our choices for models.

### Pre-processing and general libraries
***SpaCy*** is our main pick for preprocessing library. This is because it is very easy to build out a pipeline to do most of it with very few method calls. Additionally it has built in part of speech tagging and visualization which we were unable to find with NLTK. The documentation for SpaCy is good and it appears to run very quickly. The output is also understandable and easily passed to other models. It also has a built in component for bigram and trigram reduction which is somewhat hard to implement manually. This is something else that NLTK does not have.

### Text summarization libraries.
***Transformers*** our our main pick for text summarization. These are abstractive models that perform very well. Many of the summaries are very legible. In our early prototyping we did notice that there was a maximum length of text to summarize on some of the models. Additionally we also noticed that these can have issues with very technical transcripts such as math lectures. This is due to trying to summarize equations and then providing those equations out of context. Because of this we may need to attempt further processing steps such as grouping sentences by their topics first or by adding in an extractive approach for sentences with equations in technical lectures. The main transformer library that we are investigating for this is ***HuggingFace Transformers***. This is a collection of various pre-trained transformers. They can run on 'normal' computers without too much issue. Their main downside is probably their size.

### Topic and Keyword extraction libraries.
***LDA*** models and their variations (***PLDA*** and ***PAM***) are our main choices for topic modeling and keyword extraction. These models are specifically designed to be able to quickly and efficiently perform topic modeling. Additionally there are libraries such as ***PyLDAVis*** that are specifically designed to work with the outputs of these models. This assists in the visualization and understanding of the results of the models.

## Prototyping
We performed a lot of prototyping for the Machine Learning models. Our prototyping mainly involved attempting to get minimally viable models created for our core applications. For topic and keyword modeling we primarily focused on the LDA models. This involved looking at tutorials for how these models were implemented and then attempting to do so ourselves. The text summarization was prototyped by attempting a couple different models. It was eventually decided that HuggingFace Transformers were the best option for text summarization. As for preprocessing we decided to build out a class with preprocessing and cleaning methods. This was originally done using only SpaCy. Later on we had to expand this preprocessor to use NLTK as well in order for the preprocessor to run faster.

Some of the issues that we used to prototype are listed below:
- #122 and #123 for Khan Academy Transfer Learning
- #94 for investigating Transformer Variations
- #82 for Prototype Transformer Text Summarizers
- #8 for investigate possible ML algorithms
- #71 for prototype LDA models & their variations
- #72 for prototyping Word2Vec
- #73 for prototyping BagOfWords
- #92 for further investigation of LDA variations
- #93 for developing a preprocessing pipeline

Some other early investigations:
- [[Investigation] Early Machine Learning Algorithm Analysis]([Investigation] Early Machine Learning Algorithm Analysis)
- [[Investigation] Voice To Text Transcription Libraries]([Investigation] Voice To Text Transcription Libraries)





