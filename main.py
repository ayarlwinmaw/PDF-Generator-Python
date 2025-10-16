from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='Letter')
pdf.set_auto_page_break(False)

# import csv file
df = pd.read_csv("topics.csv")

lined_pages = input("Do you want to be lined (y/n)?: ")


# For page numbers
page_no = 0
for index,row in df.iterrows():
    # Header
    pdf.add_page()
    page_no += 1
    pdf.set_font(family='Arial', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=100, h=12, txt=f"{index + 1}-{row['Topic']}",
             align='L', ln=1)
    pdf.line(10, 21, 205, 21)

    # Set the footer

    # lined or blank
    if lined_pages == "y":
        for y in range(20, 298, 10):
            pdf.line(10, y, 205, y)
    pdf.ln(240)

    pdf.set_font(family="Times", style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=00, h=10, txt=f"Page {page_no}", align='R', ln=1)

    # inner pages
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        page_no += 1

        # lined or blank
        if lined_pages == "y":
            pdf.line(10, 21, 205, 21)
            for y in range(20, 298, 10):
                pdf.line(10, y, 205, y)

        pdf.ln(250)

        # Footer page numbers

        pdf.set_font(family="Times", style='I', size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=00, h=10, txt=f"Page {page_no}", align='R', ln=1)

pdf.output('output.pdf', 'F')