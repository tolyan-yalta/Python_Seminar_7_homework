import tkinter as tk
import view
import export_data_csv
import export_data_xml
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


def start():
    task = tk.Tk()
    task.title('Домашнее задание')

    h = 160
    w = 400
    task.geometry(f"{w}x{h}+100+100")
    task.resizable(False, False)

    def press_btn_add_data():
        # Запускает виджет ввода новых данных
        # Запрашивает новые данные из модуля view
        # Запускает виджет выбора варианта сохранения данных
        # Запрашивает выбранный вариант сохранения данных
        # Передает данные в соответствующий модуль
        view.add_data_window()
        new_data = view.new_data_to_controller()
        view.choosing_save_option()
        var_save = view.variant_save_to_controller()
        if var_save == 'csv':
            export_data_csv.write_new_data_csv([new_data])
        elif var_save == 'xml':
            new_data_xml = [*new_data]
            export_data_xml.write_new_data_xml(new_data_xml)

    def programm_exit():
        task.quit()

    btn_data_csv = tk.Button(task, text='Показать телефонный справочник (csv)', command=press_btn_data_csv, font=('times new roman',14, 'bold'))
    btn_data_csv.pack(fill='x')
    btn_data_xml = tk.Button(task, text='Показать телефонный справочник (xml)', command=press_btn_data_xml, font=('times new roman',14, 'bold'))
    btn_data_xml.pack(fill='x')
    btn_add_data = tk.Button(task, text='Добавить данные в справочник', command=press_btn_add_data, font=('times new roman',14, 'bold'))
    btn_add_data.pack(fill='x')
    btn_quit = tk.Button(task, text='Выйти из программы', command=programm_exit, font=('times new roman',14, 'bold'))
    btn_quit.pack(fill='x')
    task.mainloop()


