from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import torchaudio

class Transcriber:

    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # Tell to run model on GPU if available
        self.checkpoint = 'openai/whisper-tiny'
        self.model = WhisperForConditionalGeneration.from_pretrained(self.checkpoint)
        self.model.to(self.device)
        self.processor = WhisperProcessor.from_pretrained(self.checkpoint)
        
        self.sample_rate = self.processor.feature_extractor.sampling_rate
        self.segment_length_seconds = 30
        self.segment_length_samples = self.segment_length_seconds * self.sample_rate
        
    def transcribe(self, audio):
        # Load the audio file with torchaudio
        waveform, sr = torchaudio.load(audio)
        waveform = torchaudio.transforms.Resample(sr, self.sample_rate)(waveform)
        
        # Split the audio file into segments
        num_segments = waveform.size(1) // self.segment_length_samples
        segments = torch.split(waveform, self.segment_length_samples, dim=1)
        
        # Iterate over the segments and transcribe each one
        transcript = ""
        for segment in segments:
            
            # Handle multi-channel vs mono audio
            if segment.shape[0] > 1:
                segment = torch.mean(segment, dim=0, keepdim=False)
            else:
                segment = segment.squeeze(0)
            
            input_ids = self.processor(segment, sampling_rate=self.sample_rate, return_tensors='pt').input_features.to(self.device)
            output_ids = self.model.generate(inputs=input_ids, max_length=512)
            transcription = self.processor.batch_decode(output_ids, skip_special_tokens=True)[0]
            transcript += transcription
            
        return transcript.strip()
        