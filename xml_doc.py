import xml.etree.ElementTree as ET
# from openpyxl
import pandas as pd

def xml_file(path):
    element_tree = ET.parse(path)
    root = element_tree.getroot()
    data = []
    for info in root.findall('.//cac:Item'):
        cod = info.find['.//cbc:ID'].text
        pret_unitar = info.find('.//cbc:TaxableAmount').text
        cantitate = info.find('.//cbc:InvoicedQuantity').text
        denumire = info.find('.//cbc:Name').text
    data.append({
        'cod': cod,
        'denumire': denumire,
        'pret_unitar': pret_unitar,
        'cantitate': cantitate
    })
    
    return data



xml_doc = xml_file(r'C:\Users\soare\Desktop\4196436573.xml')
df = pd.DataFrame(xml_doc)
df.to_excel('xml.xlsx', index = False)

