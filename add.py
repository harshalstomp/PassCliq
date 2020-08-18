from tkinter import *
import tkinter as tk
import tkinter.font as font
import pandas as pd


def getvals():
    try:
        vault = pd.read_csv('vault.csv')
    except:
        create = pd.DataFrame(columns = ['SERVICE','USERNAME','PASSWORD'])
        create.to_csv('vault.csv')
        vault = pd.read_csv('vault.csv')
    vault = vault.loc[:, ~vault.columns.str.contains('^Unnamed')]
    sn = service_value.get().upper()
    un = username_value.get().strip()
    pw = password_value.get()
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
    if not password_value.get() or pw.isspace()==True:
        my_labelz3.config(text='PASSWORD empty')
        c+=1
    if(c==0):
        vault = vault.append({'SERVICE':sn,'USERNAME':un,"PASSWORD":pw},ignore_index=True)
        vault.to_csv('vault.csv', index=True)
        root3.destroy()
    

root3 = Tk()
root3.geometry('350x220')

Font1 = font.Font(family='Helvetica Neue', size=10, weight='bold'  )

zz = Label(root3,text='')
zz.grid(row=1)

service_name = Label(root3, text="SERVICE NAME : ")
service_name['font'] = Font1 
username = Label(root3, text="      USERNAME : ")
username['font'] = Font1 
password = Label(root3, text="     PASSWORD : ")
password['font'] = Font1 


service_name.grid(row=2, column=2,pady=0)
username.grid(row=4, column=2,pady=0)
password.grid(row=6, column=2,pady=0)

service_value = StringVar()
username_value = StringVar()
password_value = StringVar()

service_entry = Entry(root3, textvariable=service_value,width=30)
username_entry = Entry(root3, textvariable=username_value,width=30)
password_entry = Entry(root3, textvariable=password_value,width=30)

service_entry.grid(row=2, column=3)
username_entry.grid(row=4, column=3)
password_entry.grid(row=6, column=3)

Fontz = font.Font(family='Helvetica Neue', size=8 )
my_labelz1 = Label(root3, text='', font=Fontz)
my_labelz1.grid(row=3,column=3)
my_labelz2 = Label(root3, text='', font=Fontz)
my_labelz2.grid(row=5,column=3)
my_labelz3 = Label(root3, text='', font=Fontz)
my_labelz3.grid(row=7,column=3)

submit=Button(root3,text="SUBMIT",font=Font1, command=getvals,padx=10,pady=10,bg='#2b2b2b',fg='#ffffff',activebackground='#686868',activeforeground='#ffffff').grid(row=8, column=3,padx=0,pady=10)

root3.mainloop()


