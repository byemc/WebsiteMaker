print('Loading Website Maker GUI by ByeMC')
print('Based off of Website Maker by ByeMC')
print('Website Maker v0.2-alpha.2')

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
    titlelabel.configure(text = 'Title is now' + title.get())

def headerset():
    headerlabel.configure(text = 'Header is now' + head.get())

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
titleEntered = ttk.Entry(window, width = 30, textvariable = title)
titleEntered.grid(column = 0, row = 3, sticky=tk.E)

headerlabel = ttk.Label(window, text = 'What is the header?')
headerlabel.grid(column = 0, row = 4)

head = tk.StringVar()
headEntered = ttk.Entry(window, width = 30, textvariable = head)
headEntered.grid(column = 0, row = 5, sticky=tk.E)

bodyLabel = ttk.Label(window, text = 'What is the main text?')
bodyLabel.grid(column = 0, row = 6)

body = tk.Text(window, height = 5, width = 30, bd = 2)
body.grid(column = 0, row = 7, sticky = tk.E)

button = ttk.Button(window, text = "Set filename", command = nameset)
button.grid(column= 3, row = 1)

buttonTitle = ttk.Button(window, text = "Set title", command = titleset)
buttonTitle.grid(column = 3, row = 3)

buttonHeader = ttk.Button(window, text = "Set Header", command = headerset)
buttonHeader.grid(column = 3, row = 5)

window.mainloop()
