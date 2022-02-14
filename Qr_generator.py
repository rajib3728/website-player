from tkinter import *
import tkinter
from turtle import bgcolor
import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image,ImageTk
def submit():
    if w.get()=="":
        messagebox.showerror("Error","Please provide url!")
    else:
        # String which represents the QR code
        s = w.get()
        k=slider.get()
        # Generate QR code
        url = pyqrcode.create(s)
        # Create and save the png file naming "myqr.png"
        url.png('Your website qrcode.png', scale = k)
        messagebox.showinfo("Information","Qr code sucessfull!")
root=Tk()
root.title("Qr Code generator")
root.geometry("350x400")
photo = PhotoImage(file = "logo.png")
root.iconphoto(False,photo)
l1=Label(root,text="Enter website Link or paste")
l1.place(x=30,y=100)
w=ttk.Entry(root,font=("Times New Roman",15,"bold"))
w.place(x=30,y=130,width=270)
l2=Label(root,text="Enter scale:")
l2.place(x=30,y=190)
slider = Scale(
    root,
    from_=0,
    to=10,
    orient='horizontal',
    length=200,
    tickinterval=1,

)
slider.place(x=100,y=170)
btn1=Button(root,text="Submit",command=submit,bg="black",fg="yellow")
btn1.place(x=130,y=240)
root.mainloop()
