from PIL import Image 
from pytesseract import pytesseract 
pytesseract.tesseract_cmd = "/usr/bin/tesseract"
print(pytesseract.image_to_string(Image.open("../sampletext.png")))