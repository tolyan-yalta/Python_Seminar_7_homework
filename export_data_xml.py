import xml.etree.ElementTree as ET

def indent(elem, level=0):
    # Форматирование отступов и переносов строк для записи в файл
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def write_new_data_xml(data):
    # Запись данных в формате xml
    with open('data.xml', 'a+'):
        tree = ET.parse('data.xml')
        root = tree.getroot()

        attrib = {}
        element = root.makeelement('Account', attrib)
        root.append(element)

        ET.SubElement(element, 'Famaly').text = data[0] 
        ET.SubElement(element, 'Name').text = data[1] 
        ET.SubElement(element, 'Last_name').text = data[2] 
        ET.SubElement(element, 'Telephon').text = data[3] 
        ET.SubElement(element, 'E_mail').text = data[4] 

        indent(root)

        tree.write('data.xml', encoding='UTF-8')

