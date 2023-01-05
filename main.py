import PyPDF3
import pyttsx3
import pdfplumber
from random import randint

class pdf_audio_converter:
    def __init__(self, file_path, save_path = './', text=None):
        self.file_path = file_path
        self.save_path = save_path
        self.text = text
        self.audio_engine = pyttsx3.init()
    
    #convert pdf file to audio   
    def pdf_to_audio(self):
        
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

                    
                    
            
            
            
        