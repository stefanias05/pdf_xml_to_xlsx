import pandas as pd
import PyPDF2
import openpyxl 

def pdf_file(path):
    with open(path, 'rb') as file:
        doc_pdf = PyPDF2.PdfReader(file)
        info = " "
        for pag in range(len(doc_pdf.pages)):
            info += doc_pdf.pages[pag].extract_text()
        
    return info
    

def formating(pdf_text):
    pages = pdf_text.split('\n')
    info_text = []
    for pag in pages:
        information = pag.split(" ")
        if len(information) == 4:
            cod, denumire, pret_unitar, cantitate = information
            info_text.append({
                'cod': cod,
                'denumire': denumire,
                'pret_unitar': pret_unitar,
                'cantitate': cantitate
                })
    return info_text


pdf_text = pdf_file(r"C:\Users\soare\Desktop\AD_AUTO_TOTAL_SRL.PDF")
pdf_data = formating(pdf_text)
# print(type(pdf_data))
df = pd.DataFrame(pdf_data)
# print(type(df))
df.to_excel('pdf.xlsx', index=False)
    
