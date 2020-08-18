from tkinter import *
from pandastable import Table, TableModel
import pandas as pd



class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('1000x600+200+100')
            self.main.title('Database')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            vault = pd.read_csv('vault.csv')
            vault = vault.loc[:, ~vault.columns.str.contains('^Unnamed')] 
            self.table = pt = Table(f, dataframe=vault,
                                    showtoolbar=False, showstatusbar= False)
            pt.show()
            return

app = TestApp()
#launch the app
app.mainloop()