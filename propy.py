from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
import datetime

file_name = NONE

def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)

def save_as():
    now = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    out = asksaveasfile(mode = 'w', defaultextension = now + '.json')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Невозможно сохранить файл")

def open_file():
    global file_name
    inp = askopenfile(mode = 'r')
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

root = Tk()
root.title("Заметки")
root.geometry("400x400")

text = Text(root, width = 400, height = 400)
text.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)

menu_bar.add_cascade(label = "Файл", menu = file_menu)
file_menu.add_command(label = "Новый", command = new_file)
file_menu.add_command(label = "Открыть", command = open_file)
file_menu.add_command(label = "Сохранить", command = save_as)

root.config(menu = menu_bar)
root.mainloop()