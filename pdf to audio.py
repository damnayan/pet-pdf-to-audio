import pyttsx3
import PyPDF2
from tkinter.filedialog import *

pdfReader = PyPDF2.PdfReader(open("goggins.pdf", "rb"))
speaker = pyttsx3.init()

all_text = ""
for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', '')
    all_text += clean_text  

speaker.save_to_file(all_text, ' story.mp3')
speaker.runAndWait()

speaker.stop()
    