import easyocr
import cv2
import os
from pdf2image import convert_from_path
import numpy as np

reader = easyocr.Reader(['en'])  # English

def extract_text_from_file(filepath):
    text = ""
    if filepath.endswith(".pdf"):
        pages = convert_from_path(filepath)
        for i, page in enumerate(pages):
            image = np.array(page)
            result = reader.readtext(image, detail=0)
            text += " ".join(result) + "\n"
    else:
        image = cv2.imread(filepath)
        result = reader.readtext(image, detail=0)
        text = " ".join(result)
    return text
