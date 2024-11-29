from tkinter import *
import json
from tkinter.messagebox import showerror
from xml.sax.saxutils import escape
import requests
from bs4 import BeautifulSoup



class Main:
    def __init__(self):
        self.win = Tk()
        self.win.title('Practice 11')
        self.win.geometry('700x700')
        self.name = Entry(self.win, width=15)
        self.name.focus()
        self.name.pack()

        def save():
            url = f"https://api.github.com/users/{Find_Name(self.name.get()).get_name()}"

            user_data = requests.get(url).json()

            try:
                dic = {
                    'company': user_data['company'],
                    'created_at': user_data['created_at'],
                    'email': user_data['email'],
                    'id': user_data['id'],
                    'name': user_data['name'],
                    'url': user_data['url']
                }

                json_ans = json.dumps(dic, indent=3)

                self.text.delete('1.0', 'end')
                self.text.insert('1.0', json_ans)
            except KeyError:
                showerror('', "Does't exist")


        button = Button(self.win, text="Show info", command=save)
        button.pack()

        self.text = Text(self.win, width=50, height=50, wrap=WORD)
        self.text.pack()

class Find_Name:
    def __init__(self, user_input):
        self.user_input = user_input
        self.name_by_names = {}
        self.name_by_numbers = {}


    def creat_dict(self):
        url = 'https://habr.com/ru/articles/453444/'

        response = requests.get(url)

        bs = BeautifulSoup(response.text, "html.parser")
        c = 1
        for i in bs.find_all('a', class_="")[1:]:
            b = str(i.text)
            if "github.com/" in b:
                self.name_by_numbers[c] = b[b.rfind('/') + 1:]
                c += 1

        all_rep = bs.find_all('b')
        for i, j in enumerate(all_rep, 1):
            self.name_by_names[j.text] = self.name_by_numbers[i]


    def get_name(self):
        self.creat_dict()
        try:
            if self.user_input.isnumeric():
                return self.name_by_numbers[int(self.user_input)]
            else:
                return self.name_by_names[self.user_input]
        except KeyError:
            showerror('', "Doesn't exist!")


prog = Main()
prog.win.mainloop()