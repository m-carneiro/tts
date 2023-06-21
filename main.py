import time

import PyPDF2
from art import *
from cli_args_system import Args
from gtts import gTTS

print(text2art("PDF to MP3"))

args = Args(convert_numbers=False)
text_cleaned = ""
text_list = []
language = "pt-br"

file_location = args.flag_str("file", "f", "File location")

pdf_reader = PyPDF2.PdfReader(open(file_location, "rb"))

for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text()
    text_cleaned = text.replace("\n", "")
    text_list.append(text_cleaned)

file_name = file_location.split("/")[-1].split(".")[0]

print("Recording ...")
time.sleep(15)

recorder = gTTS(text=",".join(text_list),
                lang=language).save(f"{file_name}.mp3")
print("Done!")
