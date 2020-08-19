from tkinter import *
import tkinter as tk
import tkinter.font as font
from pandastable import Table, TableModel
import pandas as pd
import os

#Calling the delete.py script
def delete():
   os.system('python del.py')

#Calling the view.py script    
def view():
   os.system('python view.py')

#Calling the add.py script   
def add():
    os.system('python add.py')
    
#Creating and positioning the window
root1 = Tk(className='Database Window')
root1.geometry('300x240')
root1.resizable(False,False)
windowWidth = root1.winfo_reqwidth()
windowHeight = root1.winfo_reqheight()
positionRight = int(root1.winfo_screenwidth()/2 - windowWidth/2)-120
positionDown = int(root1.winfo_screenheight()/2 - windowHeight/2)-75
root1.geometry("+{}+{}".format(positionRight, positionDown))

#View Database button
Font1 = font.Font(family='Helvetica Neue', size=10, weight='bold'  )
viewButton = Button(root1, text='View Credentials',command=view,padx=30,pady=10,bg='#2b2b2b',fg='#ffffff',activebackground='#686868',activeforeground='#ffffff')
viewButton['font'] = Font1 
viewButton.grid(row=0,column=0,padx=40,pady=15)

#Add credentials button
addButton = Button(root1, text='Add Credentials',command=add,padx=31,pady=10,bg='#2b2b2b',fg='#ffffff',activebackground='#686868',activeforeground='#ffffff')
addButton['font'] = Font1 
addButton.grid(row=1,column=0,padx=40,pady=15)

#Deleting the credentials
deleteButton = Button(root1, text='Delete Credentials',command=delete,padx=28,pady=10,bg='#2b2b2b',fg='#ffffff',activebackground='#686868',activeforeground='#ffffff')
deleteButton['font'] = Font1 
deleteButton.grid(row=2,column=0,padx=40,pady=15)

#Exit button
exit_btn = PhotoImage(file='images/exit.png')
exit_image = Label(image = exit_btn)
exit_button = Button(root1, image = exit_btn , command=root1.destroy, borderwidth = 0)
exit_button.grid(row=2,column=1,padx=0,pady=15,sticky='s')

root1.mainloop()
