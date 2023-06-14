from transformers import BartTokenizer, BartForConditionalGeneration
import torch
import nltk

class TransformerPredict:
    
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # Tell to run model on GPU if available
        self.model = BartForConditionalGeneration.from_pretrained('kajan1/bart-large-cnn-khan')
        self.model.to(self.device)
        self.tokenizer = BartTokenizer.from_pretrained('kajan1/bart-large-cnn-khan')
        
    """Uses chunking to split document by sentences and regroup into chunks that are < max model input
       Summarizes each chunk, concatentaes separated by newlines, and returns the summaries as one string
    
        Args:
            text (str): The text to be summarized
            min_len (int): The minimum length of the output
            max_len (int): The maximum length of the output
            beams (int): Number of beams to use with beam search decoding
            sample (bool): Whether the model uses sampling in decoding
    """
    def summarize(self, text, min_len=0, max_len=128, beams=1, sample=False):
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
                
        #Generate and decode summaries for each chunk
        res = ""
        for i in [self.tokenizer(c, return_tensors='pt') for c in chunks]:
            summary_ids = self.model.generate(i["input_ids"].to(self.device), num_beams=beams, \
                                         min_length=min_len, max_length=max_len, \
                                         do_sample=sample)
            summary = self.tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
            res += summary + "\n"
        return res[:-1]