from tkinter import *
import tkinter as tk
import tkinter.font as font
import random
import pyperclip as pc
import os
### These fuctions are to generate the password.
def create_str(str_length):
    
    rem = []
    for i in range(str_length):
        rem.append(str(random.choice('abcdefghjkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ1346789')))
    return rem

def create_lower(str_length):
    low = []
    for i in range(str_length):
        low.append(str(random.choice('abcdefghjkmnopqrstuvwxyz')))
    return low

def create_cap(str_length):
    caps=[]
    for i in range(str_length):
        caps.append(str(random.choice('ABCDEFGHJKLMNPQRSTUVWXYZ')))
    return caps

def create_num(num_length):
    digits = []
    for i in range(num_length):
        digits.append(str(random.choice([1,3,4,6,7,8,9])))

    return digits

def create_special_chars(special_length):
    stringSpecial = []
    for i in range(special_length):
        stringSpecial.append(random.choice("!$%&*+,-.:;=?@^_~"))
    return stringSpecial

def generate_password():
    pf =  create_lower(3) + create_cap(1)
    pl = create_str(3) +create_num(2) + create_special_chars(2) + create_cap(1) 

    random.shuffle(pf)
    random.shuffle(pl)
    global password1
    password1 = pf+pl
    password1 = ''.join(password1)
    return password1
    
def generate():
    p = generate_password()
    my_label.config(text=p)
    my_label2.config(text = '')

def copy():
    pc.copy(password1)
    my_label2.config(text = 'Copied!')
    
def pwdb():
    os.system('python pwdb.py')
    
#GUI CODE

global password
root = Tk(className='PassKit-Password Generator and Keeper ')
root.geometry('300x260')

passFont1 = font.Font(family='Helvetica', size=15 )
my_label = Label(root, text='------------')
my_label.grid(row=0,column=0,padx=20,pady=50)
my_label['font'] = passFont1

copy_btn = PhotoImage(file='images/copy.png')
copy_image = Label(image = copy_btn)
#copy_image.grid(row=0,column=1,padx=0,pady=0)

copy_button = Button(root, image = copy_btn , command=copy, borderwidth = 0)
copy_button.grid(row=0,column=1,padx=0,pady=0)

Font2 = font.Font(family='Helvetica Neue', size=8 )
my_label2 = Label(root, text='')
my_label2.grid(row=0,column=2)
my_label2['font'] = Font2

passFont = font.Font(family='Helvetica Neue', size=10, weight='bold'  )
passButton = Button(root, text='Generate Password',command=generate,padx=30,pady=10,bg='#2b2b2b',fg='#ffffff',activebackground='#686868',activeforeground='#ffffff')
passButton['font'] = passFont 
passButton.grid(row=1,column=0,padx=20,pady=0,sticky='n')

dbButton = Button(root, text='Password database',command=pwdb,padx=30,pady=10,bg='#2b2b2b',fg='#ffffff',activebackground='#686868',activeforeground='#ffffff')
dbButton['font'] = passFont 
dbButton.grid(row=2,column=0,padx=20,pady=10,sticky='n')

exit_btn = PhotoImage(file='images/exit.png')
exit_image = Label(image = exit_btn)
exit_button = Button(root, image = exit_btn , command=root.destroy, borderwidth = 0)
exit_button.grid(row=2,column=2,padx=0,pady=10,sticky='sw')

root.mainloop()






