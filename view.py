import tkinter as tk
from tkinter import ttk
import export_data_csv

def main_window(data):
    # Запускается основное окно телефонного справочника
    global win
    # global group_3
    # global data_temp
    # global headline
    win = tk.Tk()
    win.title('Телефонный справочник')

    h = 500
    w = 750
    sw = win.winfo_screenwidth()
    x = int((sw - w) / 2)
    sh = win.winfo_screenheight()
    y = int((sh - h) / 2)
    win.geometry(f"{w}x{h}+{x}+{y}")
    win.resizable(False, False)

    group_1 = create_frame_group_1()
    group_1.pack(anchor='nw', fill='x')

    group_2 = create_frame_group_2(data)
    group_2.pack(anchor='nw', fill='x')

    win.mainloop()

def create_frame_group_1():
    # Запускается панель с кнопками: Добавить, Изменить, Удалить, Найти и Выйти
    # global group_1
    # global btn_add
    # global btn_change
    # global btn_delete
    # global btn_search
    # global btn_quit
    
    group_1 = tk.Frame(win, borderwidth=1, relief="raised")
    btn_add = tk.Button(group_1, text='Добавить', command=0, font=('times new roman',14, 'bold')).pack(side="left")
    btn_change = tk.Button(group_1, text='Изменить', command=0, font=('times new roman',14, 'bold')).pack(side="left", after=btn_add)
    btn_delete = tk.Button(group_1, text='Удалить', command=0, font=('times new roman',14, 'bold')).pack(side="left", after=btn_change)
    btn_search = tk.Button(group_1, text='Найти', command=0, font=('times new roman',14, 'bold')).pack(side="left", after=btn_delete)
    btn_destroy = tk.Button(group_1, text='Закрыть', command=win.destroy, font=('times new roman',14, 'bold')).pack(side="left", after=btn_search)
    return group_1
    
def create_frame_group_2(data):
    # Запускается таблица с данными
    # global group_2
    group_2 = tk.Frame(win, borderwidth=1, relief="raised")
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("mystyle.Treeview", background="grey90", font=('times new roman',12, 'bold')) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", background="grey70", font=('times new roman',14, 'bold')) # Modify the font of the headings
    table = ttk.Treeview(group_2 ,columns=("family", "name", "last_name", "telephone", "e_mail"), show="headings", style="mystyle.Treeview")
    table.pack(fill="both", expand=1)
    table.heading("family", text="Фамилия")
    table.heading("name", text="Имя")
    table.heading("last_name", text="Отчество")
    table.heading("telephone", text="Телефон")
    table.heading("e_mail", text="E-mail")
    table.column("family", width=150)
    table.column("name", width=150)
    table.column("last_name", width=150)
    table.column("telephone", anchor="center", width=150)
    table.column("e_mail", anchor="center", width=150)

    for person in data:
        table.insert("", 'end', values=person)
    return group_2

# win2 = None
new_data_csv = None

def add_data_window():
    # Запускается окно добавления данных
    win2 = tk.Tk()
    win2.title('Добавление в телефонный справочник')

    h = 500
    w = 1000
    sw = win2.winfo_screenwidth()
    x = int((sw - w) / 2)
    sh = win2.winfo_screenheight()
    y = int((sh - h) / 2)
    win2.geometry(f"{w}x{h}+{x}+{y}")
    win2.resizable(False, False)

    def get_new_data_csv():
        global new_data_csv
        new_data_csv = (entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get(), entry_5.get())
        win2.destroy()

    group_3 = tk.Frame(win2, borderwidth=1, relief="raised")
    group_3.pack(anchor='nw', fill='x')

    entry_1 = ttk.Entry(group_3, font=('times new roman',14, 'bold'))
    entry_1.pack(side="left", anchor='nw', padx=8, pady= 8)
    entry_2 = ttk.Entry(group_3, font=('times new roman',14, 'bold'))
    entry_2.pack(side="left", anchor='nw', padx=8, pady= 8)
    entry_3 = ttk.Entry(group_3, font=('times new roman',14, 'bold'))
    entry_3.pack(side="left", anchor='nw', padx=8, pady= 8)
    entry_4 = ttk.Entry(group_3, font=('times new roman',14, 'bold'))
    entry_4.pack(side="left", anchor='nw', padx=8, pady= 8)
    entry_5 = ttk.Entry(group_3, font=('times new roman',14, 'bold'))
    entry_5.pack(side="left", anchor='nw', padx=8, pady= 8)

    group_4 = tk.Frame(win2, borderwidth=1, relief="raised")
    group_4.pack(anchor='nw', fill='x')

    btn_save_csv = tk.Button(group_4, text='Сохранить в csv', command=get_new_data_csv, font=('times new roman',14, 'bold')).pack(side="left")

    btn_destroy = tk.Button(group_4, text='Закрыть', command=win2.destroy, font=('times new roman',14, 'bold'))
    btn_destroy.pack(side="left", after=btn_save_csv)
    win2.mainloop()

def new_data_csv_to_controller():
    global new_data_csv
    return new_data_csv


