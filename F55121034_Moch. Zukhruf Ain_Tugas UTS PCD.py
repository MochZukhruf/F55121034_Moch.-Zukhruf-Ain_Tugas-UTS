import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter
import numpy as np
import cv2

window = tk.Tk()
window.title('UTS PCD F55121034-Moch. Zukhruf Ain')
window.geometry('1100x600')

def open_image():
    # Membuka dialog untuk memilih gambar
    path = filedialog.askopenfilename()
    if path:
        # Membuka gambar menggunakan PIL
        image = Image.open(path)
        # Menampilkan gambar ke dalam GUI
        img_resized = image.resize((200, 200), resample=Image.LANCZOS)
        global tampil
        tampil = ImageTk.PhotoImage(img_resized)
        gambar = tk.Label(frame1, image=tampil)
        gambar.grid(column=0, row=2)
        # Metode Median filter
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
        blur = cv2.medianBlur(img, 5)
        result_img = Image.fromarray(blur)
        # Hasil Metode median filter
        img_resized1 = result_img.resize((200, 200), resample=Image.LANCZOS)
        result_tk = ImageTk.PhotoImage(img_resized1)
        gambar1 = tk.Label(frame1, image=result_tk)
        gambar1.image = result_tk
        gambar1.grid(column=1, row=2)


        # Metode Perbaikan Citra - Color Stretching
        img_yuv = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
        y, u, v = cv2.split(img_yuv)
        y_min, y_max = np.percentile(y, (5, 95))
        y = np.uint8(np.clip((y - y_min) * 255.0 / (y_max - y_min), 0, 255))
        img_yuv = cv2.merge((y, u, v))
        img_stretched = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)

        result_img2 = Image.fromarray(img_stretched)
        # # Hasil Metode Perbaikan Citra - Color Stretching
        img_resized2 = result_img2.resize((200, 200), resample=Image.LANCZOS)
        result_tk2 = ImageTk.PhotoImage(img_resized2)
        gambar2 = tk.Label(frame1, image=result_tk2)
        gambar2.image = result_tk2
        gambar2.grid(column=2, row=2)


frame1 = Frame(window, width=500, highlightbackground='black', highlightthicknes=2)
frame1.columnconfigure(0, weight = 1)
frame1.columnconfigure(1, weight = 1)
frame1.columnconfigure(2, weight = 1)

label1 = Label(frame1, text="Perbaikan Citra :")
label1.grid(column = 0, row=0, padx = 10, pady=10)
label2 = Label(frame1, text="Original Image")
label2.grid(column = 0, row=1, padx = 10, pady=20)
label3 = Label(frame1, text="Metode Perbaikan 1 (Median Filtering)")
label3.grid(column = 1, row=1, padx = 10, pady=20)
label4 = Label(frame1, text="Metode Perbaikan 2 (Metode Color Stretching)")
label4.grid(column = 2, row=1, padx = 10, pady=20)

button1=Button(frame1, text="Select an image", command = open_image)
button1.grid(column=0, row = 3)

frame1.grid(column = 0, row=0,padx = 60, ipadx=200, ipady=100)

frame2 = Frame(window, width=500, highlightbackground='black', highlightthicknes=2)

frame2.columnconfigure(0, weight = 1)
frame2.columnconfigure(1, weight = 1)
frame2.columnconfigure(2, weight = 1)
frame2.grid(column = 0, row=1,pady=10, padx = 0, ipadx=200, ipady=10)


label5 = Label(frame2, text="Creator :")
label5.grid(column = 0, row=0, padx = 10, pady=10)
label6 = Label(frame2, text="Nama : Moch. Zukhruf Ain")
label6.grid(column = 0, row=1, padx = 10, pady=20)
label7 = Label(frame2, text="NIM : F55121034")
label7.grid(column = 1, row=1, padx = 10, pady=20)
label8 = Label(frame2, text="Kelas : A")
label8.grid(column = 2, row=1, padx = 10, pady=20)

window.mainloop()