import pandas as pd #module for working with files
import glob
from fpdf import FPDF
from pathlib import Path

#glob is used to return all file paths that match a specific pattern
filepaths = glob.glob("/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-4/Invoices/*.xlsx") #get every file that ends in .xlsx

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1") #when reading from excel files
                        #for excel files we have to provide a sheet_name argument
                        #because excel docs could have multiple sheets
    #print(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4") #1 pdf per invoice
    pdf.add_page()

    filename = Path(filepath).stem #toextract a part of the file path
    #print(filename)
    invoice_nr = filename.split("-")[0]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"invoice nr.{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")
