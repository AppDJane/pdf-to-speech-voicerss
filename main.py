########################################################################################################################
#
#
# Author: AppDJane
#
# Date: May 5th, 2021
#
# Content:
# This is a program that takes a PDF file, identifies the text and converts the text to speech.
# Effectively creating a free audiobook. AI text-to-speech has come so far. They can sound more lifelike than a real audiobook.
#
#
# The following Text-To-Speech (TTS) API is used:
#
# http://www.voicerss.org/api/
#
########################################################################################################################

# ----------------------------------------------- IMPORTS ------------------------------------------------- #

# to read PDF file and create text input for API
import PyPDF2

# to call API and get .wav file
import requests

# to get environmental data
import os

# -------------------------------------------------- CONSTANTS ------------------------------------------------------- #

API_KEY = os.environ.get('API_KEY')  # set your own API Key
VOICERS_ENDPOINT = "http://api.voicerss.org/?"

# --------------------------------------------------- VARIABLES ------------------------------------------------------ #

TTS_params = {
    'key': API_KEY,
    'src': 'hello world.',
    'hl': 'en-au',
    'v': 'Zoe',
    'c': 'wav'
}

# -------------------------------------------------- READ PDF FILE ---------------------------------------------------- #

filepath = input("Please enter location of the file to be converted to speech: ")

# creating a pdf file object
pdfFileObj = open(filepath, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
text_to_speech = pageObj.extractText()

# closing the pdf file object
pdfFileObj.close()


TTS_params['src'] = text_to_speech

# --------------------------------------------------- API REQUEST ---------------------------------------------------- #



response = requests.get(VOICERS_ENDPOINT, params=TTS_params)
print(response.status_code)
#print(response.content)

if response.status_code == 200:
    output_file = input("How would you like to call your output file? ")
    output_file = output_file + ".wav"
    f = open(output_file, "wb")
    try:
        f.write(response.content)
    except IOError:
        print("Error")
    finally:
        f.close()
