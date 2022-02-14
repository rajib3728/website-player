from cProfile import label
from tkinter import *
from PIL import Image,ImageTk
import webbrowser
def click1():
    root1.destroy()
    import Qr_generator
def click2():
    root1.destroy()
    import Web_blocker
def web():
    webbrowser.open("https://sites.google.com/view/the-earth-infomation/home")    
root1=Tk()
root1.geometry("1600x900")
root1.title("Website player")
photo = PhotoImage(file = "logo.png")
root1.iconphoto(False,photo)
f0=Frame(root1,bg="midnight blue",width=1600,height=140)
f0.place(x=0,y=0)
l1=Label(f0,text="WEBSITE PLAYER",font=("Times", 30,"bold"),bg="midnight blue",fg="yellow")
l1.place(x=630,y=57)
btn=Button(f0,text="Visit our website",bg="black" ,fg="yellow",command=web)
btn.place(x=1400,y=5)
f1=Frame(root1,width=500,height=500,bg="grey",highlightbackground="black", highlightthickness=2)
f1.place(x=200,y=150)
l2=Label(f1,text="Qr code generator",font=("Times", 20),bg="grey")
l2.place(x=150,y=50)
btn1=Button(f1,text="Click here!",fg="yellow",bg="black",command=click1)
btn1.place(x=220,y=100)
bg=ImageTk.PhotoImage(file="img1.jpg")
bglb=Label(f1,image=bg,bg="grey")
bglb.place(x=150,y=130,width=200,height=200)
can1=Canvas(f1,width=400,height=100,bg="grey",highlightbackground="grey")
can1.place(x=50,y=340)
can1.create_text(190,40,text='''This is a qr code gernerator tool.Please provide 
one url then select scale then press submit.''',fill="black")
f2=Frame(root1,height=500,width=500,bg="grey",highlightbackground="black", highlightthickness=2)
f2.place(x=820,y=150)
l3=Label(f2,text="Website blocker",font=("Times", 20),bg="grey")
l3.place(x=150,y=50)
btn2=Button(f2,text="Click here!",fg="yellow",bg="black",command=click2)
btn2.place(x=220,y=100)
bg1=ImageTk.PhotoImage(file="img2.jpg")
bglb1=Label(f2,image=bg1,bg="grey")
bglb1.place(x=150,y=130,width=200,height=200)
l4=Label(f2,text='''copy and paste one url you want
to block and for unblock give same address ''',bg="grey")
l4.place(x=130,y=350)
f3=Frame(root1,bg="black",width=1600,height=200)
f3.place(x=0,y=720)
l5=Label(f3,text=''' If website blockker does not work follow this step:
open:  C:\\Windows\\System32\\drivers\\etc\\
Now right click on hosts file >> Properties >> Security >> Edit >> Provide Full control to user you are using''',fg="white",bg="black")
l5.place(x=450,y=2)
root1.mainloop()