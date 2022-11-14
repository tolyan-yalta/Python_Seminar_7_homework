import tkinter as tk
from tkinter import ttk

new_data = None
variant_save = None

def main_window(data):
    # Запускается основное окно телефонного справочника
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

    group_1 = tk.Frame(win, borderwidth=1, relief="raised")
    group_1.pack(anchor='nw', fill='x')
    btn_add = tk.Button(group_1, text='Добавить', command=0, font=('times new roman', 14, 'bold'))
    btn_add.pack(side="left")
    btn_change = tk.Button(group_1, text='Изменить', command=0, font=('times new roman', 14, 'bold'))
    btn_change.pack(side="left", after=btn_add)
    btn_delete = tk.Button(group_1, text='Удалить', command=0, font=('times new roman', 14, 'bold'))
    btn_delete.pack(side="left", after=btn_change)
    btn_search = tk.Button(group_1, text='Найти', command=0, font=('times new roman', 14, 'bold'))
    btn_search.pack(side="left", after=btn_delete)
    btn_destroy = tk.Button(group_1, text='Закрыть', command=win.destroy, font=('times new roman', 14, 'bold'))
    btn_destroy.pack(side="left", after=btn_search)

    group_2 = tk.Frame(win, borderwidth=1, relief="raised")
    group_2.pack(anchor='nw', fill='both', expand=True)
    table = ttk.Treeview(group_2, columns=("family", "name", "last_name", "telephone", "e_mail"), show="headings")
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

    win.mainloop()

def add_data_window():
    # Запускается окно добавления данных
    global variant_save
    variant_save = None
    win2 = tk.Tk()
    win2.title('Добавление в телефонный справочник')

    h = 120
    w = 1100
    sw = win2.winfo_screenwidth()
    x = int((sw - w) / 2)
    sh = win2.winfo_screenheight()
    y = int((sh - h) / 2)
    win2.geometry(f"{w}x{h}+{x}+{y}")
    win2.resizable(False, False)

    def get_new_data():
        global new_data
        new_data = (entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get(), entry_5.get())
        win2.destroy()

    group_3_1 = tk.Frame(win2, borderwidth=1, relief="raised")
    group_3_1.pack(anchor='nw', fill='x')
    lbl_famaly = tk.Label(group_3_1, text='Фамилия', font=('times new roman', 14, 'bold'))
    lbl_famaly.pack(ipadx=75, side="left")
    lbl_name = tk.Label(group_3_1, text='Имя', font=('times new roman', 14, 'bold'))
    lbl_name.pack(ipadx=75,side="left")
    lbl_last_name = tk.Label(group_3_1, text='Отчество', font=('times new roman', 14, 'bold'))
    lbl_last_name.pack(ipadx=75,side="left")
    lbl_telephone = tk.Label(group_3_1, text='Телефон', font=('times new roman', 14, 'bold'))
    lbl_telephone.pack(ipadx=70,side="left")
    lbl_e_mail = tk.Label(group_3_1, text='E-mail', font=('times new roman', 14, 'bold'))
    lbl_e_mail.pack(ipadx=70,side="left")

    group_3 = tk.Frame(win2, borderwidth=1, relief="raised")
    group_3.pack(anchor='nw', fill='x')
    entry_1 = ttk.Entry(group_3, font=('times new roman', 14, 'bold'))
    entry_1.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_2 = ttk.Entry(group_3, font=('times new roman', 14, 'bold'))
    entry_2.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_3 = ttk.Entry(group_3, font=('times new roman', 14, 'bold'))
    entry_3.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_4 = ttk.Entry(group_3, font=('times new roman', 14, 'bold'))
    entry_4.pack(side="left", anchor='nw', padx=8, pady=8)
    entry_5 = ttk.Entry(group_3, font=('times new roman', 14, 'bold'))
    entry_5.pack(side="left", anchor='nw', padx=8, pady=8)

    group_4 = tk.Frame(win2, borderwidth=1, relief="raised")
    group_4.pack(anchor='nw', fill='x')
    btn_save = tk.Button(group_4, text='Сохранить', command=get_new_data, font=('times new roman', 14, 'bold'))
    btn_save.pack(side="left")
    btn_destroy = tk.Button(group_4, text='Закрыть', command=win2.destroy, font=('times new roman', 14, 'bold'))
    btn_destroy.pack(side="left", after=btn_save)

    win2.mainloop()

def new_data_to_controller():
    global new_data
    return new_data

def choosing_save_option():
    # Запускается окно выбора варианта сохранения
    win3 = tk.Tk()
    win3.title('Варианты сохранения')

    h = 40
    w = 500
    sw = win3.winfo_screenwidth()
    x = int((sw - w) / 2)
    sh = win3.winfo_screenheight()
    y = int((sh - h) / 2)
    win3.geometry(f"{w}x{h}+{x}+{y}")
    win3.resizable(False, False)

    global variant_save

    def variant_csv():
        global variant_save
        variant_save = 'csv'
        win3.destroy()

    def variant_xml():
        global variant_save
        variant_save = 'xml'
        win3.destroy()

    btn_save_csv = tk.Button(win3, text='Сохранить в csv', command=variant_csv, font=('times new roman', 14, 'bold'))
    btn_save_csv.pack(side="left")
    btn_save_xml = tk.Button(win3, text='Сохранить в xml', command=variant_xml, font=('times new roman', 14, 'bold'))
    btn_save_xml.pack(side="left")
    btn_destroy = tk.Button(win3, text='Отменить', command=win3.destroy, font=('times new roman', 14, 'bold'))
    btn_destroy.pack(fill='x')

    win3.mainloop()

def variant_save_to_controller():
    global variant_save
    return variant_save

