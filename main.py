
from tkinter import *
from tkinter.ttk import ttk
import numpy as np
import csv
import myConfig

csvFile = myConfig.filename

class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])



with open(csvFile) as infile:
    reader = csv.reader(infile) # Create a new reader
    lst = [row for row in reader]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()

