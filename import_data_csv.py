import csv

def read_data_csv():
    # Чтение данных из файла в формате csv
    with open('data.csv', 'r', newline='', encoding='utf-8') as f:
        data = [tuple(row) for row in csv.reader(f)]
    return data
            
