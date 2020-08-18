from tkinter import *
import tkinter as tk
import tkinter.font as font
from pandastable import Table, TableModel
import pandas as pd
import os


def generate():
    print("HI")
    
def view():
   os.system('python view.py')
   
def add():
    #root1.destroy()
    os.system('python add.py')
    
    
    
root1 = Tk(className='Database Window')
root1.geometry('300x240')

Font1 = font.Font(family='Helvetica Neue', size=10, weight='bold'  )
viewButton = Button(root1, text='View Credentials',command=view,padx=30,pady=10,bg='#2b2b2b',fg='#ffffff',activebackground='#686868',activeforeground='#ffffff')
viewButton['font'] = Font1 
viewButton.grid(row=0,column=0,padx=40,pady=15)

addButton = Button(root1, text='Add Credentials',command=add,padx=31,pady=10,bg='#2b2b2b',fg='#ffffff',activebackground='#686868',activeforeground='#ffffff')
addButton['font'] = Font1 
addButton.grid(row=1,column=0,padx=40,pady=15)

deleteButton = Button(root1, text='Delete Credentials',command=generate,padx=28,pady=10,bg='#2b2b2b',fg='#ffffff',activebackground='#686868',activeforeground='#ffffff')
deleteButton['font'] = Font1 
deleteButton.grid(row=2,column=0,padx=40,pady=15)

exit_btn = PhotoImage(file='images/exit.png')
exit_image = Label(image = exit_btn)
exit_button = Button(root1, image = exit_btn , command=root1.destroy, borderwidth = 0)
exit_button.grid(row=2,column=1,padx=0,pady=15,sticky='s')

root1.mainloop()