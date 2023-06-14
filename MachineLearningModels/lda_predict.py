import gensim
import pickle
import os

class LDAPredict:

    def __init__(self):
        self.model_path = os.path.join(os.path.dirname(__file__), 'models/lda/lda.model')
        self.dictionary_path = os.path.join(os.path.dirname(__file__), 'models/lda/lda_dictionary.pkl')
        with open(self.dictionary_path, 'rb') as f:
            self.words = pickle.load(f)
        self.model = gensim.models.ldamodel.LdaModel.load(self.model_path)
        
    def get_topics(self, text):
        bow = self.words.doc2bow(text.split())
        topics = self.model[bow]
        topics.sort(key=lambda x: x[1], reverse=True)
        
        result = []
        for topic in topics:
            result.append(
                {
                    "prevalence":str(topic[1]), # str for json.dumps()
                    "keywords":list(list(zip(*self.model.show_topic(topic[0])))[0])
                }
            )
            
        return result
      