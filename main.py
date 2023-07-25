from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.iconbitmap("icon.ico")

img1 = Image.open("images/f1.jpg")
img1 = img1.resize((400, 400))
img1 = ImageTk.PhotoImage(img1)
img2 = Image.open("images/f2.jpg")
img2 = img2.resize((400, 400))
img2 = ImageTk.PhotoImage(img2)
img3 = Image.open("images/f3.jpg")
img3 = img3.resize((400, 400))
img3 = ImageTk.PhotoImage(img3)
img4 = Image.open("images/f4.jpg")
img4 = img4.resize((400, 400))
img4 = ImageTk.PhotoImage(img4)
img5 = Image.open("images/f5.jpg")
img5 = img5.resize((400, 400))
img5 = ImageTk.PhotoImage(img5)

image_list = [img1, img2, img3, img4, img5]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)

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

    status = Label(root, text=f"Image {img_number} of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


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

    status = Label(root, text=f"Image {img_number} of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=lambda: back(1), state=DISABLED)
button_exit = Button(root, text="Exit program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
