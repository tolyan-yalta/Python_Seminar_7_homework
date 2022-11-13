import xml.etree.ElementTree as et

doc = et.parse('data.xml')
root = doc.getroot()

root = et.parse('data.xml').getroot()

# for acnt in root:
#     for subelem in acnt:
#         print(subelem.text)

# x = tuple([acnt.text  for acnt in root])

    

# print(tuple([i.text  for i in et.parse('data.xml').getroot()[0]]))

def parse_xml():
    # data = [tuple([i.text  for i in et.parse('data.xml').getroot()[0]])]
    data = [tuple([i.text  for i in et.parse('data.xml').getroot()[j]]) for j in range(len(root))]
    return data