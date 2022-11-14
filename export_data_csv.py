import csv

def write_new_data_csv(new_data_csv):
    # Запись данных в формате csv
    with open('data.csv', 'a', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerows(new_data_csv)


