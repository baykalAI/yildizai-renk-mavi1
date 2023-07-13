import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os
import subprocess

def select_image():
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    image = image.convert("RGB")  
    image.save('1.jpg')
    result = subprocess.run(['python3', 'gender_age.py', '-i', '1.jpg'], stdout=subprocess.PIPE)
    result_label.config(text=str(result.stdout))

root = tk.Tk()
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack()
result_label = tk.Label(root)
result_label.pack()
root.mainloop()
