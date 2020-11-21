import numpy as np
import cv2
import os
import pytesseract 
from PIL import Image

path = "mm.png"

def ocr(path):
    
    # Load an color image in grayscale
    img = cv2.imread(path,1)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(image) 
    
    return text

print(ocr(path))
