#You don't know what will be for dinner?
#Use this application.
#Add Your options to the database and then draw one of the by random.
#Simple and completly not necessary programm :)
#author: Artur Kosior


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
            #print(index) # for debuging
            selected_tuple = self.ideas_print.get(index)
            #print(selected_tuple) # for debuging
            row = database.show_ingredients(selected_tuple)
            self.ingredients_print.delete(0, END)
            self.ingredients_print.insert(0, row[0][0])
        except IndexError:
            pass

    def random_command(self):
        self.ideas_print.delete(0, END)
        self.ingredients_print.delete(0, END)
        row = database.draw()
        self.ideas_print.insert(0, row[0][1])
        self.ingredients_print.insert(0, row[0][2])
        pass

    def all_command(self):
        self.ideas_print.delete(0, END)
        self.ingredients_print.delete(0, END)
        for row in database.all():
            self.ideas_print.insert(END, row[1])
            #print(row) # for debuging

    def adding_window(self):
        self.new_window = Toplevel(self.master)
        self.app = Adding_window(self.new_window)

    def delete_command(self):
        database.delete(selected_tuple)
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

        # self.danie_text = StringVar()
        # self.e1 = Entry(self.right_frame, textvariable=self.danie_text)
        # self.e1.grid(row=0, column=0, pady=20)

        b1 = Button(self.right_frame, text='Losuj', height=3, width=12, command=self.random_command)
        b1.grid(row=2, column=0, padx=20)

        b2 = Button(self.right_frame, text='Wszystkie', width=12, command=self.all_command)
        b2.grid(row=3, column=0)

        b3 = Button(self.right_frame, text='Dodaj', width=12, command=self.adding_window)
        b3.grid(row=4, column=0)

        b4 = Button(self.right_frame, text='Usuń', width=12, command=self.delete_command)
        b4.grid(row=5, column=0)

        b5 = Button(self.right_frame, text='Zamknij', width=12, command=root.destroy)
        b5.grid(row=6, column=0)

class Adding_window:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.resizable(0, 0)
        self.master.title('Dodawanie pomysłu')
        self.master.geometry('300x180')
        self.create_adding_widgets()

    def add_command(self):
        database.insert(self.new_idea.get(), self.new_ingredients.get())
        self.master.destroy()

    def create_adding_widgets(self):

        l1 = Label(self.master, text='Przepis')
        l1.grid(row=0, column=0, padx=30, pady=5, sticky='ew')

        self.new_idea = StringVar()
        self.e1 = Entry(self.master, textvariable=self.new_idea)
        self.e1.grid(row=1, column=0, columnspan=3, sticky='ew', padx=30, pady=5)

        l2 = Label(self.master, text='Składniki')
        l2.grid(row=3, column=0, padx=30, pady=5, sticky='ew')

        self.new_ingredients = StringVar()
        self.e2 = Entry(self.master, textvariable=self.new_ingredients)
        self.e2.grid(row=4, column=0, columnspan=3, sticky='ew', padx=30, pady=5)

        b1=Button(self.master, text='Dodaj', width=12, command=self.add_command)
        b1.grid(row=9, column=0, padx=25, pady=10)

        b2=Button(self.master, text='Anuluj', width=12, command=self.master.destroy)
        b2.grid(row=9, column=1, padx=25, pady=10)

root = Tk()
root.resizable(0, 0)
root.title('Dinnerasist')
root.geometry('400x300')
app = Application(root)
database = Database()
root.mainloop()

