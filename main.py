import pandas as pd #module for working with files
import glob
from fpdf import FPDF
from pathlib import Path

# glob is used to return all file paths that match a specific pattern
filepaths = glob.glob("/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-4/Invoices/*.xlsx") #get every file that ends in .xlsx

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4") #1 pdf per invoice
    pdf.add_page()

    # Extract the name of the file w/o the date
    filename = Path(filepath).stem #to extract a part of the file path
    #print(filename)
    invoice_nr = filename.split("-")[0]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"invoice nr.{invoice_nr}", ln=1) # ln creates a breakline
    

    # Extract the name of the file that includes the date
    date = filename.split("-")[1]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1") #when reading from excel files
                        #for excel files we have to provide a sheet_name argument
                        #because excel docs could have multiple sheets
    
    # Add a header
    columns = list(df.columns) # columns is a propeerty of a dataframe tha gives us a list of the columns in said dataframe/file
                               # we convert it to a list because it is an index object
    columns = [item.replace("-", " ").title() for item in columns] # list comprehension to remove "_"
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=40, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
    
    # Add rows to a table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
    
   