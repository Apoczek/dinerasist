from tkinter import *
from backend import Database


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.left_frame = Frame(root)
        self.left_frame.pack(side=LEFT)
        self.right_frame = Frame(root)
        self.right_frame.pack(side=RIGHT)
        self.create_widgets()

    def get_selected_line(self, event):
        try:
            global selected_tuple
            index = self.ideas_print.curselection()[0]
            selected_tuple = self.ideas_print.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
        except IndexError:
            pass

    def random_command(self):
        self.ideas_print.delete(0, END)
        row = database.draw()
        self.ideas_print.insert(0, row)
        pass

    def all_command(self):
        self.ideas_print.delete(0, END)
        for row in database.all():
            self.ideas_print.insert(END, row)

    def add_command(self):
        database.insert(self.danie_text.get())
        self.ideas_print.delete(0, END)
        self.ideas_print.insert(END, self.danie_text.get())

    def delete_command(self):
        database.delete(selected_tuple[0])
        self.all_command()

    def create_widgets(self):

        l1 = Label(self.left_frame, text='Pomysł')
        l1.grid(row=0, column=0)

        self.ideas_print = Listbox(self.left_frame, height=5, width=40)
        self.ideas_print.grid(row=1, column=0, rowspan=3, columnspan=3)
        self.ideas_print.bind('<<ListboxSelect>>', self.get_selected_line)

        sb1 = Scrollbar(self.left_frame)
        sb1.grid(row=1, column=3, rowspan=3, sticky=N+S)

        self.ideas_print.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.ideas_print.yview)

        l2 = Label(self.left_frame, text='Składniki')
        l2.grid(row=4, column=0)

        self.ingredients_print = Listbox(self.left_frame, height=10, width=40)
        self.ingredients_print.grid(row=5, column=0, rowspan=5, columnspan=3)

        sb2 = Scrollbar(self.left_frame)
        sb2.grid(row=5, column=3, rowspan=5, sticky=N+S)

        self.ingredients_print.configure(yscrollcommand=sb2.set)
        sb2.configure(command=self.ingredients_print.yview)

        self.danie_text = StringVar()
        self.e1 = Entry(self.right_frame, textvariable=self.danie_text)
        self.e1.grid(row=0, column=0, pady=20)

        b1 = Button(self.right_frame, text='Losuj', height=3, width=12, command=self.random_command)
        b1.grid(row=2, column=0, padx=20)

        b2 = Button(self.right_frame, text='Wszystkie', width=12, command=self.all_command)
        b2.grid(row=3, column=0)

        b3 = Button(self.right_frame, text='Dodaj', width=12, command=self.add_command)
        b3.grid(row=4, column=0)

        b4 = Button(self.right_frame, text='Usuń', width=12, command=self.delete_command)
        b4.grid(row=5, column=0)

        b5 = Button(self.right_frame, text='Zamknij', width=12, command=root.destroy)
        b5.grid(row=6, column=0)


root = Tk()
root.title('Dinnerasist')
root.geometry('400x300')
app = Application(root)
database = Database()
root.mainloop()
