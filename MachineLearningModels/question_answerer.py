from transformers import AutoModelWithLMHead, AutoTokenizer, pipeline
import torch

class QuestionAnswerer:
    
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # Tell to run models on GPU if available
        self.extractive_model = pipeline('question-answering', model='distilbert-base-cased-distilled-squad', device=self.device)
        self.abstractive_model = AutoModelWithLMHead.from_pretrained("tuner007/t5_abs_qa")
        self.abstractive_model.to(self.device)
        self.abstractive_tokenizer = AutoTokenizer.from_pretrained("tuner007/t5_abs_qa")
        
    def ask(self, question, context):
        # Get answer, indices, and score from extractive model
        answer = self.extractive_model(question=question, context=context)
        
        # Get answer from abstractive model
        formatted_text = "context: %s <question for context: %s </s>" % (context,question)
        features = self.abstractive_tokenizer([formatted_text], return_tensors='pt')
        output_ids = self.abstractive_model.generate(input_ids=features['input_ids'].to(self.device), attention_mask=features['attention_mask'].to(self.device))
        abstractive_ans = self.abstractive_tokenizer.decode(output_ids[0], skip_special_tokens=True)
        
        # Put answers from both models into single dictionary
        answer['extractive_answer'] = answer.pop('answer')
        answer['abstractive_answer'] = abstractive_ans
        
        return answer
