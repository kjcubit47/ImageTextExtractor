from PIL import Image
from pytesseract import pytesseract
import tkinter as tk

# pytesseract.tesseract_cmd = "/usr/bin/tesseract"
# print(pytesseract.image_to_string(Image.open("../sampletext.png")))


class TextExtractor:
    def __init__(self):
        self.tesseract_cmd_path = "/usr/bin/tesseract"

    def extractText(self, imgPath):
        text = pytesseract.image_to_string(Image.open(imgPath))
        return text

    def selectPath(self):
        folder_selected = tk.filedialog.askdirectory()
        self.tesseract_cmd_path = folder_selected
        return folder_selected
