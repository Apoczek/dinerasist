from tkinter import *
from backend import Database

def get_selected_line(event):
    try:
        global selected_tuple
        index = ideas_print.curselection()[0]
        print(index)
        selected_tuple = ideas_print.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
    except IndexError:
        pass

def random_command():
    ideas_print.delete(0, END)
    row = database.draw()
    ideas_print.insert(0, row)
    pass

def all_command():
    ideas_print.delete(0, END)
    for row in database.all():
        ideas_print.insert(END, row)

def add_command():
    database.insert(danie_text.get())
    ideas_print.delete(0, END)
    ideas_print.insert(END, danie_text.get())

def delete_command():
    database.delete(selected_tuple[0])
    all_command()

root = Tk()
root.title('Dinnerasist')
root.geometry('400x300')
database = Database()

left_frame = Frame(root)
left_frame.pack(side=LEFT)
right_frame = Frame(root)
right_frame.pack(side=RIGHT)

l1 = Label(left_frame, text='Pomysł')
l1.grid(row=0, column=0)

ideas_print = Listbox(left_frame, height=5, width=40)
ideas_print.grid(row=1, column=0, rowspan=3, columnspan=3)
ideas_print.bind('<<ListboxSelect>>', get_selected_line)

sb1 = Scrollbar(left_frame)
sb1.grid(row=1, column=3, rowspan=3, sticky=N+S)

ideas_print.configure(yscrollcommand=sb1.set)
sb1.configure(command=ideas_print.yview)

l2 = Label(left_frame, text='Składniki')
l2.grid(row=4, column=0)

ingredients_print = Listbox(left_frame, height=10, width=40)
ingredients_print.grid(row=5, column=0, rowspan=5, columnspan=3)

sb2 = Scrollbar(left_frame)
sb2.grid(row=5, column=3, rowspan=5, sticky=N+S)

danie_text = StringVar()
e1 = Entry(right_frame, textvariable=danie_text)
e1.grid(row=0, column=0, pady=20)

b1 = Button(right_frame, text='Losuj', height=3, width=12, command=random_command)
b1.grid(row=2, column=0, padx=20)

b2 = Button(right_frame, text='Wszystkie', width=12, command=all_command)
b2.grid(row=3, column=0)

b3 = Button(right_frame, text='Dodaj', width=12, command=add_command)
b3.grid(row=4, column=0)

b4 = Button(right_frame, text='Usuń', width=12, command=delete_command)
b4.grid(row=5, column=0)

b5 = Button(right_frame, text='Zamknij', width=12, command=root.destroy)
b5.grid(row=6, column=0)

root.mainloop()
