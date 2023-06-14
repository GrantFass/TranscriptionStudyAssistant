# prep work
- normalization
  - convert all next to the same case, remove punctuation, expand contractions, convert numbers to words, etc.
  - May need to do spell checking
- stemming
  - eliminating suffixes, prefixes, infixes, circumfixes, etc
- Lemmatization
 - capture canonical forms based on a words lemma.
 - harder to implement than stemmers
- remove stop words
  - remove words that contribute little to meaning of text like "the", "and", "a".
- part of speech tagging?

[topic modeling and nlp link](https://iq.opengenus.org/topic-modelling-techniques/)

[similarity metrics](https://medium.com/swlh/similarity-queries-and-text-summarization-in-nlp-50ef4cf04f7b)

[Pulling questions from text using SPACY](https://stackoverflow.com/questions/67991549/how-to-extract-questions-from-text-using-spacy)

[question answer systems](https://stackoverflow.com/questions/37171540/answers-extraction-from-an-unstructured-text)

[named entity recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)

[Question Answer Pair extraction paper](https://arxiv.org/pdf/2102.12128.pdf)

[paper on summarization metrics from MIT](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00373/100686/SummEval-Re-evaluating-Summarization-Evaluation)

[text summarization link](https://iq.opengenus.org/compare-text-summarization-models/)

| EVALUATION METRIC |   LSA  | TEXTRANK |   T5   | KL-SUM | LUHN'S METHOD |
|:-----------------:|:------:|:--------:|:------:|:------:|:-------------:|
| ROUGE-1 Precision | 0.6527 |  0.4637  | 0.4615 | 0.4776 |     0.1829    |
|   ROUGE-1 Recall  | 0.6438 |  0.4383  | 0.4109 | 0.4383 |     0.2054    |
|  ROUGE-1 F-Score  | 0.6482 |  0.4507  | 0.4347 | 0.4571 |     0.1935    |
| ROUGE-2 Precision | 0.4772 |  0.2967  | 0.3086 | 0.2873 |     0.0086    |
|   ROUGE-2 Recall  | 0.4719 |  0.3033  | 0.2808 | 0.2808 |     0.0112    |
|  ROUGE-2 F-Score  | 0.4745 |  0.2999  | 0.2941 | 0.2840 |     0.0097    |
| ROUGE-L Precision | 0.6388 |  0.4492  | 0.4615 | 0.4626 |     0.1585    |
|   ROUGE-L Recall  | 0.6301 |  0.4246  | 0.4109 | 0.4246 |     0.1780    |
|  ROUGE-L F-Score  | 0.6344 |  0.4366  | 0.4347 | 0.4428 |     0.1677    |

# [NTLK](https://www.nltk.org/)
- Python natural language toolkit
- provides text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning.
- free and open source
- Need to cite them in documentation.
- [more sources](https://www.inf.ed.ac.uk/teaching/courses/inf2a/lecturematerials/index.html#lecture01)
- one of the best known and most used NLP libraries

# [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Python library.
- Pull data from HTML and XML files

# Bag of Words
- used for feature extraction
- list unique words in text document
- represent each sentence or document as vector of words (1 for present, 0 for absent)
- can also do word counts
- Term Frequency or Inverse Document Frequency techniques.
- Distorts word order and ignores context and meaning.

# Word Embedding with Word2Vec or Glove
- words that have the same meaning have a similar representation
- represents words in coordinate system. Related words are placed closer together.
- Word2Vec captures meaning and good at analogy questions. Uses vector offset methods
  - May be useful for building questions later
- GLOVE: Global Vectors for Word Representation. extension of word2vec method. learns word vectors. builds word-context matrix.

# Classical Approaches
- such as Naïve Bayes or SVMs
- lower accuracy
- much faster training time
- good for spam filtering
- probably not as good for clustering.
- TfidTransformer
  - convert text into feature vectors
- n-grams
  - tries to preserve contiguous sequences of n-items from text.
- Levenshtein distance
  - word / string similarity measure

# Visualization tool
- wordcloud python package.

# [blog post quote](https://blog.pangeanic.com/ai-will-read-text-to-discover-information-for-you):
"""NLP engines with models that can read and summarize long bodies of text, extracting key concepts, recognizing and identifying people who might be mentioned, and identifying patterns and structures that human readers might miss."""

# [AWS article on text analysis](https://aws.amazon.com/what-is/text-analysis/)
- "Conditional random fields (CRFs): This is a machine learning method that extracts text by evaluating specific patterns or phrases. It is more refined and flexible than REGEX."
- "Topic modeling methods identify and group related keywords that occur in an unstructured text into a topic or theme. These methods can read multiple text documents and sort them into themes based on the frequency of various words in the document. Topic modeling methods give context for further analysis of the documents."
- "PII redaction automatically detects and removes personally identifiable information"
- [AWS NLP service](https://aws.amazon.com/comprehend/)

# [Another NLP resource](https://towardsdatascience.com/machine-learning-text-processing-1d5a2d638958)
- gives some good examples on how to use NTLK.

# [some key terms explained](https://www.kdnuggets.com/2017/02/natural-language-processing-key-terms-explained.html)
- "Information retrieval is the process of accessing and retrieving the most appropriate information from text based on a particular query, using context-based indexing or metadata. One of the most famous examples of information retrieval would be Google Search."

# [MIT AI system about concepts across video, audio, and text](https://news.mit.edu/2022/ai-video-audio-text-connections-0504)

# [Example Sentiment Analysis](https://www.dataquest.io/blog/using-machine-learning-and-natural-language-processing-tools-for-text-analysis/)
- uses pattern.en.sentiment package for sentiment analysis
- rake package from ntlk for keyword extraction
- gensim corpora package for topic modeling
- k-means clustering 
- sentence clustering with ntlk
- n-grams from ntlk for clustering
- concordance for checking how specific words are used in text.
- how to build a query answering model

# [Sentiment Analysis Algorithms and Applications: A Survey](https://www.sciencedirect.com/science/article/pii/S2090447914000550)

# Topic Modeling:
"""Topic modeling algorithms are a closely related technology to concept extraction. Topic models differ from concept extraction in that they are more expressive and attempt to infer a statistical model of the generation process of the text (Blei and Lafferty, 2009). This model is then used to cluster words into topics. The clustering is considered to be a soft clustering—that is, words can probabilistically appear in multiple topics."""
- learn correlation between topics
- aggregate vector representing contribution of each topic in document (used to compare documents).
- text summarization is a use case for topic modeling
- [link](analyticsvidhya.com/blog/2021/05/topic-modelling-in-natural-language-processing/)
- unsupervised ML approach
- scans documents and finds word and phrase patterns in them.
- automatically clusters word groupings and related expressions.
- does not need categorized data.
- probably useful for pulling out the topics / keywords of a text but not summarizing?
- extract needed attributes from bag of words.
- [possible models](https://www.analyticssteps.com/blogs/what-topic-modelling-nlp)
- LDA (Latent Dirirchlet Allocation) model
 - find correlations between many documents
 - uses VEM (Variational Exception Maximization) technique
 - usually picks the top few words from a bag of words
- NMF (Non Negative Matrix Factorization)
- LSA (Latent Semantic Analysis)
- Parallel Latent Dirichlet Allocation
- Pachinko Allocation Model (PAM)
- Topic Classification is the supervised version
- [toward data science article](https://towardsdatascience.com/nlp-topic-modeling-to-identify-clusters-ca207244d04f)

# Concept Extraction
- grouping of words and phrases into semantically similar groups
- can be done with SVD?
- STATISTICA Text Miner

# Concept Extraction Links
- [science direct. mostly about STATISTICA text miner. a bit about concept extraction.](https://www.sciencedirect.com/topics/mathematics/concept-extraction)
- [github](https://github.com/topics/concept-extraction)
- [Information Extraction](https://www.analyticsvidhya.com/blog/2020/06/nlp-project-information-extraction/)