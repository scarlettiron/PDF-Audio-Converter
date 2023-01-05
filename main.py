import PyPDF3
import pyttsx3
import pdfplumber
from random import randint
from playsound import playsound
import speech_recognition as sr

class pdf_audio_converter:
    def __init__(self, file_path, save_path = './', text=None):
        self.file_path = file_path
        self.save_path = save_path
        self.text = text
        self.audio_engine = pyttsx3.init()
    
    #convert pdf file to cleaned text  
    def pdf_to_text(self):
        
        final_text = ""
        
        #open pdf to be read
        with open(self.file_path, 'rb') as book:
            #read file
            reader = PyPDF3.PdfFileReader(book)
            #get number of pages file contains
            pages = reader.numPages
            
            with pdfplumber.open(self.file_path) as pdf:

                for i in range(pages):
                    page = pdf.pages[i]
                    #extract text from pdf
                    text = page.extract_text()
                    #clean text
                    text.strip().replace('\n', ' ')
                    final_text += text
                    self.text = final_text
                    
                pdf.close()
            book.close()
        
        return self
    
    #for saving cleaned text as an audio file
    #requires pdf to text to be run first
    def save_pdf_as_audio(self):
        file_key = randint(0, 10000)
        file_name = f"pdf_audio_{file_key}.mp3"
        file_path = f"{self.save_path}{file_name}"

        self.audio_engine.save_to_file(self.text, file_path)
        self.audio_engine.runAndWait()
        return
        
    #for playing cleaned text as audio
    #requires pdf to text to beb run first   
    def play_text_audio(self):
        if not self.text:
            raise Exception('Text needed')
    
        self.audio_engine.say(self.text)
        self.audio_engine.runAndWait()
        self.audio_engine.stop()
        return
    
    #for playing audio from self.file_path
    def play_audio(self):
        playsound(self.file_path)
        return
    
    #for converting speech to text
    def speech_to_text(self):
        r = sr.Recognizer()
        final_text = None
        
        with sr.AudioFile(self.file_path) as audio:
            data = r.record(audio)
            text = r.recognize_google(data)
            final_text = text
        
        #create naming vars
        file_key = randint(0, 10000)
        file_name = f"audio_text_{file_key}.txt"
        
        with open(file_name, 'w') as txt:
            txt.writelines([final_text])
            txt.close()
        
        return
                
#for local testing
if __name__ == "__main__":
    #pdf's
    #action = pdf_audio_converter('./AWS-Certified-Cloud-Practitioner_Exam-Guide.pdf')
    #audio's
    action = pdf_audio_converter('pdf_audio_2757.mp3')
    
    action.play_audio()
                    
            
            
            
        