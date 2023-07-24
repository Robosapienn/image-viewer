from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.iconbitmap("icon.ico")

img1 = ImageTk.PhotoImage(Image.open("images/f1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/f2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/f3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/f4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/f5.jpg"))

image_list = [img1, img2, img3, img4, img5]

global b_forward
global b_back
label = Label(root, image=img1)
label.grid(row=0, column=0, columnspan=3)


def forward(img_number):
    global label
    global b_forward
    global b_back

    label.grid_forget()
    label = Label(image=image_list[img_number - 1])
    b_forward = Button(root, text=">>", command=lambda: forward(img_number + 1))
    b_back = Button(root, text="<<", command=lambda: back(img_number - 1))

    if img_number == 5:
        b_forward = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    b_forward.grid(row=1, column=2)
    b_back.grid(row=1, column=0)


def back(img_number):
    global label
    global b_forward
    global b_back

    label.grid_forget()
    label = Label(image=image_list[img_number - 1])
    b_forward = Button(root, text=">>", command=lambda: forward(img_number + 1))
    b_back = Button(root, text="<<", command=lambda: back(img_number - 1))

    if img_number == 1:
        b_back = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    b_forward.grid(row=1, column=2)
    b_back.grid(row=1, column=0)


button_back = Button(root, text="<<", command=lambda: back(1), state=DISABLED)
button_exit = Button(root, text="Exit program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
