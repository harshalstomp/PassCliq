from tkinter import *
import tkinter as tk
import tkinter.font as font
import pandas as pd
import csv

#Deleting the credentials
def getvals1():
    try:
        vault = pd.read_csv('vault.csv')
    except:
        create = pd.DataFrame(columns = ['SERVICE','USERNAME','PASSWORD'])
        create.to_csv('vault.csv')
        vault = pd.read_csv('vault.csv')
    vault = vault.loc[:, ~vault.columns.str.contains('^Unnamed')]
    sn = service_value.get().upper()
    un = username_value.get()
    my_labelz1.config(text='')
    my_labelz2.config(text='')
    my_labelz3.config(text='')
    c=0
    if not service_value.get() or sn.isspace()==True:
        my_labelz1.config(text='SERVICE NAME empty')
        c +=1
    if not username_value.get() or un.isspace()==True:
        my_labelz2.config(text='USERNAME empty')
        c+=1
    if c==0:
        v1 = vault[((vault.SERVICE== sn) & (vault.USERNAME==un))]
        v1 = v1.index.values
        if (len(v1)==0):
            my_labelz3.config(text='CREDENTIALS NOT FOUND')
        else:
            my_labelz3.config(text='CREDENTIALS DELETED')
        vault = vault.drop(v1)
        vault.to_csv('vault.csv', index=True)
    

#Creating and positioning the window
root2 = Tk()
root2.geometry('350x200')
root2.resizable(False,False)
windowWidth = root2.winfo_reqwidth()
windowHeight = root2.winfo_reqheight()
positionRight = int(root2.winfo_screenwidth()/2 - windowWidth/2)-120
positionDown = int(root2.winfo_screenheight()/2 - windowHeight/2)-75
root2.geometry("+{}+{}".format(positionRight, positionDown))

Font1 = font.Font(family='Helvetica Neue', size=10, weight='bold'  )

zz = Label(root2,text='')
zz.grid(row=1)

#Service_name Entry
service_name = Label(root2, text="SERVICE NAME : ")
service_name['font'] = Font1 
#Username Entry
username = Label(root2, text="      USERNAME : ")
username['font'] = Font1 

service_name.grid(row=2, column=2)
username.grid(row=4, column=2)

service_value = StringVar()
username_value = StringVar()

service_entry = Entry(root2, textvariable=service_value,width=30)
username_entry = Entry(root2, textvariable=username_value,width=30)

service_entry.grid(row=2, column=3)
username_entry.grid(row=4, column=3)

#SUbmit Button
submit=Button(root2,text="DELETE",font=Font1, command=getvals1,padx=10,pady=10,bg='#2b2b2b',fg='#ffffff',activebackground='#686868',activeforeground='#ffffff').grid(row=6, column=3,padx=0,pady=10)

Fontz = font.Font(family='Helvetica Neue', size=8 )
my_labelz1 = Label(root2, text='', font=Fontz)
my_labelz1.grid(row=3,column=3)
my_labelz2 = Label(root2, text='', font=Fontz)
my_labelz2.grid(row=5,column=3)
my_labelz3 = Label(root2, text='', font=Fontz)
my_labelz3.grid(row=7,column=3)

root2.mainloop()
