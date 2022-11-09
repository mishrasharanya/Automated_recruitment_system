from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
import math
import string
import sys
a=Tk()
var=IntVar()
checkvar1=IntVar()
checkvar2=IntVar()
checkvar3=IntVar()
my_str = tk.StringVar()
my_str.set("")



def sel():
    e=Tk()
    e.geometry("300x200")
    l6=Label(e, text='CONGRATULATIONS, YOU ARE SHORTLISTED FOR THE INTERVIEW ROUND')
    l6.grid(row=0,column=7)
def yoo():
    e=Tk()
    e.geometry("300x200")
    l6=Label(e, text="THANK YOU FOR APPLYING, BETTER LUCK NEXT TIME!!")
    l6.grid(row=0,column=7)




def read_file(filename):
	
	try:
		with open(filename, 'r') as f:
			data = f.read()
		return data
	
	except IOError:
		print("Error opening or reading input file: ", filename)
		sys.exit()
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase," "*len(string.punctuation)+string.ascii_lowercase)
# splitting the text lines into words
# translation table is a global variable
# mapping upper case to lower case and
# punctuation to spaces
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
									" "*len(string.punctuation)+string.ascii_lowercase)
	
# returns a list of the words
# in the file
def get_words_from_line_list(text):
	
	text = text.translate(translation_table)
	word_list = text.split()
	
	return word_list


# counts frequency of each word
# returns a dictionary which maps
# the words to their frequency.
def count_frequency(word_list):
	
	D = {}
	
	for new_word in word_list:
		
		if new_word in D:
			D[new_word] = D[new_word] + 1
			
		else:
			D[new_word] = 1
			
	return D

# returns dictionary of (word, frequency)
# pairs from the previous dictionary.
def word_frequencies_for_file(filename):
	
	line_list = read_file(filename)
	word_list = get_words_from_line_list(line_list)
	freq_mapping = count_frequency(word_list)

	print("File", filename, ":", )
	print(len(line_list), "lines, ", )
	print(len(word_list), "words, ", )
	print(len(freq_mapping), "distinct words")

	return freq_mapping


# returns the dot product of two documents
def dotProduct(D1, D2):
	Sum = 0.0
	
	for key in D1:
		
		if key in D2:
			Sum += (D1[key] * D2[key])
			
	return Sum

# returns the angle in radians
# between document vectors
def vector_angle(D1, D2):
	numerator = dotProduct(D1, D2)
	denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))
	
	return math.acos(numerator / denominator)


def documentSimilarity(filename_1, filename_2):
	
# filename_1 = sys.argv[1]
# filename_2 = sys.argv[2]
	sorted_word_list_1 = word_frequencies_for_file(filename_1)
	sorted_word_list_2 = word_frequencies_for_file(filename_2)
	distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
	
	if(distance>0.35):
            yoo()
	else:
            sel()
            



    
def done1():
    file1 = filedialog.askopenfilename()
    #file2 = filedialog.askopenfilename()
    if(file1):
        #my_str.set(file1)
        #my_str.set(file2)
        #fob=open(file1,'r')
        documentSimilarity("zon.txt","com_zon.txt" )
        


def done2():
    file1 = filedialog.askopenfilename()
    #file2 = filedialog.askopenfilename()
    if(file1):
        #my_str.set(file1)
        #my_str.set(file2)
        #fob=open(file1,'r')
        documentSimilarity("zon.txt","com_xea.txt" )
def done3():

    file1 = filedialog.askopenfilename()
    #file2 = filedialog.askopenfilename()
    if(file1):
        #my_str.set(file1)
        #my_str.set(file2)
        #fob=open(file1,'r')
        documentSimilarity("zon.txt","com_tros.txt" )

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
l3=Label(a, text='BANGALORE')
l3.grid(row=1,column=0,padx=20,pady=30)
b1=Button(a,text="Next",command=apply)
b1.grid(row=2,column=3,padx=20,pady=30)
label=Label(a)
label.grid(row=7,column=4)
a.mainloop()























