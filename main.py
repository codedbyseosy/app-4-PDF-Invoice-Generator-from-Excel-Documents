import pandas as pd #module for working with files
import glob

filepaths = glob.glob("/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-4/Invoices/*.xlsx") #get every file that ends in .xlsx

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1") #when reading from excel files
                        #for excel files we have to provide a sheet_name argument
                        #because excel docs could have multiple sheets
    print(df)