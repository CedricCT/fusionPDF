import os
import glob
import PyPDF2

def merge_pdfs(folder, output):
    # List of pdf files in the folder
    files = sorted(glob.glob(os.path.join(folder, '*.pdf')))

    # Creation of pdf writer
    pdf_writer = PyPDF2.PdfWriter()

    # Loop over each pdf file
    for file in files:
        pdf = PyPDF2.PdfReader(file)
        # Add all pages from the pdf to the writer
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            pdf_writer.add_page(page)

    # Writing the output file
    with open(output, 'wb') as out:
        pdf_writer.write(out)

# Using the function
merge_pdfs('pdf', 'sortie.pdf')
