#!/bin/env python
from codeforces import Codeforces
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.nickname = tk.Entry(self.master)
        self.nickname.grid(row=0, column=0)
        self.submit = tk.Button(self.master)
        self.submit.grid(row=0, column=1)
        self.submit['text'] = "Search"
        self.submit['command'] = self.print_info

    def print_info(self):
        data = Codeforces().get_user_info(self.nickname.get())
        tk.Label(self.master, text='Current rating: ').grid(row=1, column=0)
        tk.Label(self.master, text='Current rank: ').grid(row=2, column=0)
        tk.Label(self.master, text='Max rating: ').grid(row=3, column=0)
        tk.Label(self.master, text='Max rank: ').grid(row=4, column=0)

        tk.Label(self.master, text=data['rating']).grid(row=1, column=1)
        tk.Label(self.master, text=data['rank']).grid(row=2, column=1)
        tk.Label(self.master, text=data['maxRating']).grid(row=3, column=1)
        tk.Label(self.master, text=data['maxRank']).grid(row=4, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
