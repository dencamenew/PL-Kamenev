from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from tkinter.ttk import Combobox, Radiobutton
from tkinter import filedialog
import tkinter as tk


class FirstTask(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.txt = Label(self, text='Enter two numbers and choose \n the operation between them: \n', font=50)
        self.txt.grid(column=1, row=0)

        self.num1 = Entry(self, width=30)
        self.num2 = Entry(self, width=30)
        self.num1.grid(column=0, row=2)
        self.num1.focus()
        self.num2.grid(column=2, row=2)

        self.operations = Combobox(self, width=1)
        self.operations['values'] = ('+', '-', '*', '/')
        self.operations.grid(column=1, row=2)

        self.result = Label(self, text='', font=40)
        self.result.grid(column=1, row=5)

        self.but_to_count = Button(self, text='Count', command=self.calculate, font=10)
        self.but_to_count.grid(column=1, row=4)
        self.reset_button = Button(self, text='New', command=self.reset, width=15, font=20)
        self.reset_button.place(x=225, y=300)


    def reset(self):
        self.num1.delete(0, len(self.num1.get()))
        self.num2.delete(0, len(self.num2.get()))
        self.operations.delete(0, 2)


    def calculate(self):
        try:
            if self.operations.get() == '/':
                if self.num2.get() == '0':
                    showerror('', 'You can not division by zero')
                else:
                    self.result = Label(self, text=f'The result: {float(self.num1.get()) / float(self.num2.get())}', font=40)
                    self.result.grid(column=1, row=5)
            elif self.operations.get() == '*':
                self.result = Label(self, text=f'The result: {float(self.num1.get()) * float(self.num2.get())}', font=40)
                self.result.grid(column=1, row=5)
            elif self.operations.get() == '+':
                self.result = Label(self, text=f'The result: {float(self.num1.get()) + float(self.num2.get())}', font=40)
                self.result.grid(column=1, row=5)
            elif self.operations.get() == '-':
                self.result = Label(self, text=f'The result: {float(self.num1.get()) - float(self.num2.get())}', font=40)
                self.result.grid(column=1, row=5)
            else:
                showerror('', 'Please, choose the right sign!')
                self.reset()
        except ValueError:
            try:
                Label.destroy(self.result)
                showerror('', 'Incorrect input, please try again')
                self.reset()
            except UnboundLocalError:
                showerror('', 'Incorrect input, please try again')
                self.reset()




class SecondTask(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.sel = StringVar()

        self.check_box1 = Radiobutton(self, text='First', value='first', variable=self.sel, command=self.clicked)
        self.check_box1.place(x=30, y=50)

        self.check_box2 = Radiobutton(self, text='Second', value='second', variable=self.sel, command=self.clicked)
        self.check_box2.place(x=130, y=50)

        self.check_box3 = Radiobutton(self, text='Third', value='third', variable=self.sel, command=self.clicked)
        self.check_box3.place(x=230, y=50)

        self.txt = Label(self, text='', font=20)
        self.txt.place(x=100, y=100)


    def clicked(self):
        showinfo('',f'You choose {self.sel.get()} variant!')




class ThirdTask(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.btn1 = Button(self, text='Открыть содержимое \n файла', font=30, command=self.from_file)
        self.btn1.place(x=25, y=0)

        self.text = Text(self, width=50, height=50, wrap=WORD)
        self.text.place(x=250, y=0)

        self.btn2 = Button(self, text='Сохранить изменения', font=30, command=self.save)
        self.btn2.place(x=25, y=75)

        self.btn3 = Button(self, text='Стереть', font=30, command=self.delete_all)
        self.btn3.place(x=25, y=125)


    def delete_all(self):
        self.text.delete('1.0', END)


    def from_file(self):
        file = open(filedialog.askopenfilename()).read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', file)


    def save(self):
        f = open(filedialog.askopenfilename(), 'w')
        for i in self.text.get('1.0', 'end'):
            f.write(i)




class Main_window:
    def __init__(self):

        self.window = tk.Tk()
        self.window.title('pr11-oop')
        self.window.geometry("700x500")

        self.tabs_container = ttk.Notebook(self.window, width=1000, height=700)
        tab1 = FirstTask(self.tabs_container)
        tab2 = SecondTask(self.tabs_container)
        tab3 = ThirdTask(self.tabs_container)

        self.tabs_container.add(tab1, text="First task")
        self.tabs_container.add(tab2, text="Second task")
        self.tabs_container.add(tab3, text="Third task")

        self.tabs_container.grid(row=1, column=1)




program = Main_window()
program.window.mainloop()