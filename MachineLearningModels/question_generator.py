from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import nltk

class QuestionGenerator:
    
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # Tell to run model on GPU if available
        self.model = T5ForConditionalGeneration.from_pretrained('allenai/t5-small-squad2-question-generation')
        self.model.to(self.device)
        self.tokenizer = T5Tokenizer.from_pretrained('allenai/t5-small-squad2-question-generation')
        
    """Uses chunking to split document by sentences and regroup into chunks that are < max model input
       Generates questions on each chunk and returns all questions as a list of str
    
        Args:
            text (str): The text to have questions generated about
    """
    def generate(self, text):
        #Split document into sentences
        sentences = nltk.tokenize.sent_tokenize(text)
        length = 0
        chunk = ""
        chunks = []

        #Aggregate sentences into chunks that are < model_max_length
        for i, sen in enumerate(sentences):
            combined_length = len(self.tokenizer.tokenize(sen)) + length
            if combined_length <= self.tokenizer.max_len_single_sentence:
                chunk += sen + " "
                length = combined_length
                if i == len(sentences) - 1:
                    chunks.append(chunk.strip())          
            else:
                chunks.append(chunk.strip())
                chunk = sen + " "
                length = len(self.tokenizer.tokenize(sen))
                
        #Generate and decode questions for each chunk
        questions = []
        for chunk in chunks:
            input_ids = self.tokenizer.encode(chunk, return_tensors='pt')
            res = self.model.generate(input_ids.to(self.device))
            output = self.tokenizer.batch_decode(res, skip_special_tokens=True)[0]
            questions.append(output)
        
        return questions