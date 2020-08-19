from tkinter import *
from pandastable import Table, TableModel
import pandas as pd

#Viewing the database
class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            try:
                vault = pd.read_csv('vault.csv')
            except:
                create = pd.DataFrame(columns = ['SERVICE','USERNAME','PASSWORD'])
                create.to_csv('vault.csv')
                vault = pd.read_csv('vault.csv')
            vault = vault.loc[:, ~vault.columns.str.contains('^Unnamed')] 
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('1000x600+200+100')
            self.main.title('The VAULT')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            
            
            self.table = pt = Table(f, dataframe=vault,
                                    showtoolbar=False, showstatusbar= False)
            pt.show()
            return

app = TestApp()
#launch the app
app.mainloop()
