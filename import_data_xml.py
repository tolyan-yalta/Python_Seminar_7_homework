import xml.etree.ElementTree as ET

def parse_xml():
    # Чтение данных из файла в формате xml
    with open('data.xml', 'r'):
        data = [tuple([i.text  for i in ET.parse('data.xml').getroot()[j]]) 
                for j in range(len(ET.parse('data.xml').getroot()))]
    return data
