print('Loading Website Maker GUI by ByeMC')
print('Based off of Website Maker by ByeMC')
print('Website Maker is in Early Alpha 0.2')

import tkinter as tk
from tkinter import ttk 
import tkinter.messagebox
import time

window = tk.Tk()
 
window.title("Website Maker GUI")
window.minsize(250, 300)


import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Website Maker Console - v0.2-alpha")

def nameset():
    filename = name.get() + '.html'
    label.configure(text = 'filename is set to ' + filename)
    time.sleep(1)
    label.configure(text = 'Checking File...')
    time.sleep(0.5)
    try:
        with open(filename, 'rt') as savecheck:
            overwrite = tkinter.messagebox.askquestion('Error - Website Builder','This file already exists, overwrite?')
            if overwrite == 'yes':
                print('Okay, whatever you say')
                savecheck.close()
            else:
                print('Exiting...')
                import sys
                sys.exit()
    except FileNotFoundError:
         label.configure(text = 'FileNotFound, continuing')
 
def titleset():
    titlefull = title.get()

label = ttk.Label(window, text = "What is the filename of your Webpage?")
label.grid(column = 0, row = 0)
 
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 30, textvariable = name)
nameEntered.grid(column = 0, row = 1, sticky=tk.E)
html = ttk.Label(window, text = ".html")
html.grid(column = 1, row = 1)

titlelabel = ttk.Label(window, text = "What is the title of your Webpage?")
titlelabel.grid(column = 0, row = 2)

title = tk.StringVar()
titleEntered = ttk.Entry(window, width = 30, textvariable = name)
titleEntered.grid(column = 0, row = 3, sticky=tk.E)

headerlabel = ttk.Label(window, text = 'What is the header?')
headerlabel.grid(column = 0, row = 4)

button = ttk.Button(window, text = "Set filename", command = nameset)
button.grid(column= 0, row = 10)
 
window.mainloop()
