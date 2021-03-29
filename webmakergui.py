print('Loading Website Maker GUI by ByeMC')
print('Based off of Website Maker by ByeMC')
print('Website Maker is in Early Alpha 0.2')

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
 
window.title("Website Maker GUI")
window.minsize(600,400)



def titleset():
    label.configure(text= 'Title is set to ' + title.get())
 
label = ttk.Label(window, text = "Type your webpage's title here:")
label.grid(column = 0, row = 0)
 
 
 
 
title = tk.StringVar()
titleEntered = ttk.Entry(window, width = 30, align = right, textvariable = title)
titleEntered.grid(column = 0, row = 1)
html = ttk.Label(window, text = ".html")
html.grid(column = 1, row = 1)
 
 
button = ttk.Button(window, text = "Set Title", command = titleset)
button.grid(column= 0, row = 2)
 
window.mainloop()