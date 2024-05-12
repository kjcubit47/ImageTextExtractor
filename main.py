import tkinter as tk
from tkinter import filedialog
from typing import Text
from PIL import Image
from pytesseract import pytesseract
from PIL import Image, ImageTk

import TextExtractor

extractor = TextExtractor.TextExtractor()


def open_image():
    file_path = filedialog.askopenfilename(
        title="Open Image File",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")],
    )
    if file_path:
        text = extractor.extractText(file_path)
        display_image(file_path)


def display_image(file_path):
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.photo = photo
    status_label.config(text=f"Image loaded: {file_path}")


root = tk.Tk()
root.title("Extract Text from Image")
path_button = tk.Button(
    root, text="Select Path to Tesseract", command=extractor.selectPath
)
path_button.pack(padx=20, pady=10)

# text_widget = tk.Text(root, wrap=tk.WORD, height=15, width=35)
open_button = tk.Button(root, text="Select Image", command=open_image)
open_button.pack(padx=20, pady=10)
image_label = tk.Label(root)
image_label.pack(padx=20, pady=20)
status_label = tk.Label(root, text="", padx=20, pady=10)
status_label.pack()


root.mainloop()
