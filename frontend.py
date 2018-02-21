from tkinter import *

root = Tk()
root.title('Dinnerasist')
root.geometry('400x300')

left_frame = Frame(root)
left_frame.pack(side=LEFT)
right_frame = Frame(root)
right_frame.pack(side=RIGHT)

l1 = Label(left_frame, text='Pomysł')
l1.grid(row=0, column=0)

ideas_print = Listbox(left_frame, height=5, width=40)
ideas_print.grid(row=1, column=0, rowspan=3, columnspan=3)

sb1 = Scrollbar(left_frame)
sb1.grid(row=1, column=3, rowspan=3, sticky=N+S)

l2 = Label(left_frame, text='Składniki')
l2.grid(row=4, column=0)

ingrediets_print = Listbox(left_frame, height=10, width=40)
ingrediets_print.grid(row=5, column=0, rowspan=5, columnspan=3)

sb2 = Scrollbar(left_frame)
sb2.grid(row=5, column=3, rowspan=5, sticky=N+S)

b1 = Button(right_frame, text='Losuj', height=3, width=12,)
b1.grid(row=1, column=5, padx=20)

b2 = Button(right_frame, text='Wszystkie', width=12,)
b2.grid(row=3, column=5)

b3 = Button(right_frame, text='Dodaj', width=12,)
b3.grid(row=4, column=5)

b4 = Button(right_frame, text='Usuń', width=12,)
b4.grid(row=5, column=5)

b5 = Button(right_frame, text='Zamknij', width=12,)
b5.grid(row=6, column=5)

root.mainloop()
