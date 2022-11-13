import tkinter as tk
import view
import export_data_csv
import import_data_csv
import import_data_xml



def press_btn_data_csv():
    # Считывает данные из файла csv и отправляет на вывод в окно
    data = import_data_csv.read_data_csv()
    view.main_window(data)

def press_btn_data_xml():
    # Считывает данные из файла xml и отправляет на вывод в окно
    data = import_data_xml.parse_xml()
    view.main_window(data)


# def start():
task = tk.Tk()
task.title('Домашнее задание')

h = 400
w = 400
task.geometry(f"{w}x{h}+100+100")
task.resizable(False, False)

def press_btn_add_data():
    view.add_data_window()
    new_data_csv = view.new_data_csv_to_controller()
    # print([new_data_csv])
    export_data_csv.write_new_data_csv([new_data_csv])


def programm_exit():
    task.quit()

btn_data_csv = tk.Button(task, text='Показать телефонный справочник (csv)', command=press_btn_data_csv, font=('times new roman',14, 'bold')).pack(fill='x')
btn_data_xml = tk.Button(task, text='Показать телефонный справочник (xml)', command=press_btn_data_xml, font=('times new roman',14, 'bold')).pack(fill='x')

btn_add_data = tk.Button(task, text='Добавить данные в справочник', command=press_btn_add_data, font=('times new roman',14, 'bold')).pack(fill='x')
btn_quit = tk.Button(task, text='Выйти из программы', command=programm_exit, font=('times new roman',14, 'bold')).pack(fill='x')
task.mainloop()


