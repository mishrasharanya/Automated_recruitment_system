from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
a=Tk()
var=IntVar()
checkvar1=IntVar()
checkvar2=IntVar()
checkvar3=IntVar()
def sel():
    selection='you selected the option'+ str(var.get())
    label.config(text=selection)
def yoo():
    e=Tk()
    e.geometry("300x200")
    l6=Label(e, text="You are done Thanks for applying")
    l6.grid(row=0,column=7)
def done1():
    file = filedialog.askopenfilename()
    if(file):
        my_str.set(file)
        fob=open(file,'r')
        


def done2():
    file = filedialog.askopenfilename()
    if(file):
        my_str.set(file)
        fob=open(file,'r')
def done3():

    file = filedialog.askopenfilename()
    if(file):
        my_str.set(file)
        fob=open(file,'r')
'''
def apply3():
    g=Tk()
    g.geometry("800x800")
    l4=Label(g, text="Select post")
    l4.grid(row=0,column=0,padx=20,pady=30)
    l5=Label(g, text="Assistant professor (salary:100000,Collage:Anna University,Qualification:Phd holder in computer science)")
    l5.grid(row=1,column=0,padx=20,pady=30)
    b3=Button(g,text="Next",command=processok)
    b3.grid(row=2,column=0,padx=20,pady=30)
    l6=Label(g, text="professor (salary:65000,Collage:Anna University,Qualification:Btech holder in computer science with atleat 80% marks)")
    l6.grid(row=3,column=0,padx=20,pady=30)
    b3=Button(g,text="Next",command=processok)
    b3.grid(row=4,column=0,padx=20,pady=30)
    l7=Label(g, text="Clerk (salary:35000,Collage:Anna University,Qualification:Passed 12th with atleat 80% marks)")
    l7.grid(row=5,column=0,padx=20,pady=30)
    b4=Button(g,text="Next",command=processok)
    b4.grid(row=6,column=0,padx=20,pady=30)
    b5=Button(g,text="Exit",command=processcancel)
    b5.grid(row=7,column=4,padx=20,pady=30)

def apply2():
    
    f=Tk()
    f.geometry("800x800")
    l4=Label(f, text="Select post")
    l4.grid(row=0,column=0,padx=20,pady=30)
    l5=Label(f, text="Assistant professor (salary:100000,Collage:Delhi Technological University,Qualification:Phd holder in computer science)")
    l5.grid(row=1,column=0,padx=20,pady=30)
    b3=Button(f,text="Next",command=processok)
    b3.grid(row=2,column=0,padx=20,pady=30)
    l6=Label(f, text="professor (salary:65000,Collage:Delhi Technological University,Qualification:Btech holder in computer science with atleat 80% marks)")
    l6.grid(row=3,column=0,padx=20,pady=30)
    b3=Button(f,text="Next",command=processok)
    b3.grid(row=4,column=0,padx=20,pady=30)
    l7=Label(f, text="Clerk (salary:35000,Collage:Delhi Technological University,Qualification:Passed 12th with atleat 80% marks)")
    l7.grid(row=5,column=0,padx=20,pady=30)
    b4=Button(f,text="Next",command=processok)
    b4.grid(row=6,column=0,padx=20,pady=30)
    b5=Button(f,text="Exit",command=processcancel)
    b5.grid(row=7,column=4,padx=20,pady=30)
'''
def apply():
    c=Tk()
    c.geometry("800x800")
    l4=Label(c, text="SELECT COMPANY")
    l4.grid(row=0,column=0,padx=20,pady=30)
    l5=Label(c, text="ZONIRY")
    l5.grid(row=1,column=0,padx=20,pady=30)
    b3=Button(c,text="Next",command=processok1)
    b3.grid(row=2,column=0,padx=20,pady=30)
    l6=Label(c, text="XEANCO")
    l6.grid(row=3,column=0,padx=20,pady=30)
    b3=Button(c,text="Next",command=processok2)
    b3.grid(row=4,column=0,padx=20,pady=30)
    l7=Label(c, text="TROSICA")
    l7.grid(row=5,column=0,padx=20,pady=30)
    b4=Button(c,text="Next",command=processok3)
    b4.grid(row=6,column=0,padx=20,pady=30)
    b5=Button(c,text="Exit",command=processcancel)
    b5.grid(row=7,column=4,padx=20,pady=30)
def processok1():
    top=Tk()
    a="ZONIRY"
    top.geometry("1000x900")
    l8=Label(top, text="ZONIRY RECRUITMENT FOR APPLICATION DEVELOPMENT")
    l8.grid(row=0,column=0,padx=20,pady=30)
    l9=Label(top, text="UPLOAD RESUME")
    l9.grid(row=1,column=0,padx=20,pady=30)
    b1=Button(top,text="UPLOAD",command=done1)
    b1.grid(row=2,column=3,padx=20,pady=30)
    '''
    l10=Label(top, text="Mechanical")
    l10.grid(row=3,column=0,padx=20,pady=30)
    b1=Button(top,text="Apply",command=yoo)
    b1.grid(row=4,column=3,padx=20,pady=30)
    l11=Label(top, text='Civil')
    l11.grid(row=5,column=0,padx=20,pady=30)
    b1=Button(top,text="Apply",command=yoo)
    b1.grid(row=6,column=3,padx=20,pady=30)
    b2=Button(top,text="Exit",command=processcancel)
    b2.grid(row=7,column=5,padx=20,pady=30)
    '''
    label=Label(top)
    label.grid(row=7,column=4)
def processok2():
    top=Tk()
    b="XEANCO"
    top.geometry("1000x900")
    l8=Label(top, text="XEANCO RECRUITMENT FOR WEB DEVELOPMENT")
    l8.grid(row=0,column=0,padx=20,pady=30)
    l9=Label(top, text="UPLOAD RESUME")
    l9.grid(row=1,column=0,padx=20,pady=30)
    b1=Button(top,text="UPLOAD",command=done2)
    b1.grid(row=2,column=3,padx=20,pady=30)
def processok3():
    top=Tk()
    c="TROSICA"
    top.geometry("1000x900")
    l8=Label(top, text="TROSICA RECRUITMENT FOR MOBILE ENGINEERING")
    l8.grid(row=0,column=0,padx=20,pady=30)
    l9=Label(top, text="UPLOAD RESUME")
    l9.grid(row=1,column=0,padx=20,pady=30)
    b1=Button(top,text="UPLOAD",command=done3)
    b1.grid(row=2,column=3,padx=20,pady=30)
def processcancel():
    b=Tk()
    b.geometry("300x200")
    l3=Label(b, text="Thank you for using our window")
    l3.grid(row=0,column=3)
a.title("JOB RECRUITMENT")
a.geometry("900x800")
#l2=Label(a, text="Select location")
#l2.grid(row=0,column=0,padx=20,pady=30)
l3=Label(a, text='BANGALORE')
l3.grid(row=1,column=0,padx=20,pady=30)
b1=Button(a,text="Next",command=apply)
b1.grid(row=2,column=3,padx=20,pady=30)
#l4=Label(a, text='Delhi')
#l4.grid(row=3,column=0,padx=20,pady=30)
#b1=Button(a,text="Next",command=apply2)
#b1.grid(row=4,column=3,padx=20,pady=30)
#l5=Label(a, text='Chennai')
#l5.grid(row=5,column=0,padx=20,pady=30)
#b1=Button(a,text="Next",command=apply3)
#b1.grid(row=6,column=3,padx=20,pady=30)
#b2=Button(a,text="Exit",command=processcancel)
#b2.grid(row=7,column=4,padx=20,pady=30)
label=Label(a)
label.grid(row=7,column=4)
a.mainloop()























