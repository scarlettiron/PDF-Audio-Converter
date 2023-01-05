import PyPDF3
import pyttsx3
import pdfplumber
from random import randint

class pdf_audio_converter:
    def __init__(self, file, save_path = './'):
        self.file = file
        self.save_path = save_path
    
    #convert pdf file to audio   
    def pdf_to_audio(self):
        
        #open pdf to be read
        with open(self.file, 'rb') as book:
            #read file
            reader = PyPDF3.PdfFileReader(book)
            #get number of pages file contains
            pages = reader.numPages
            
            
            
            
        