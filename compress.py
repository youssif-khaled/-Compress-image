import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


def upload_file():
    global img, filename, picture
    f_types = [('Jpg Files', '*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    picture = Image.open(filename)

    img = ImageTk.PhotoImage(file=filename)
    b2 = tk.Button(my_w, image=img)  # using Button
    b2.grid(row=7, column=2)


def compress():
    file_name = 'image-1-compressed.jpg'
    picture.save("Compressed_"+file_name, quality=10)


def Resize():
    new_image = picture.resize((200, 200))
    new_image.save('image_200.jpg')


def Rotate():

    image_rot_90 = picture.rotate(90)
    image_rot_90.save('image_rot_90.jpg')

    image_rot_180 = picture.rotate(180)
    image_rot_180.save('image_rot_180.jpg')


def Transform():

    greyscale_image = picture.convert('L')
    greyscale_image.save('greyscale_image.jpg')


my_w = tk.Tk()

my_w.geometry("400x300")
# Size of the window
my_w.config(bg='black')
my_w.title('imageProcessing')
my_font1 = ('times', 18, 'bold')

l1 = tk.Label(my_w, text='Add Photo',
              width=100, font=my_font1)
l1.grid(row=1, column=3)

btn1 = tk.Button(my_w, text="Upload", width=10, height=1,
                 bg='blue', fg='white', font=my_font1, command=upload_file)
btn2 = tk.Button(my_w, text="Compress", width=10, height=1,
                 bg='red', fg='white', font=my_font1, command=compress)
btn3 = tk.Button(my_w, text="Resize", width=10, height=1,
                 bg='yellow', fg='white', font=my_font1, command=Resize)
btn4 = tk.Button(my_w, text="Rotate", width=10, height=1,
                 bg='green', fg='white', font=my_font1, command=Rotate)
btn5 = tk.Button(my_w, text="Transform", width=10, height=1,
                 bg='white', fg='red', font=my_font1, command=Transform)
btn1.grid(row=2, column=1)
btn2.grid(row=3, column=1)
btn3.grid(row=4, column=1)
btn4.grid(row=5, column=1)
btn5.grid(row=6, column=1)
my_w.mainloop()
