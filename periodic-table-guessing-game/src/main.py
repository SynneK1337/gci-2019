import tkinter as tk
from table import Table
from random import randint, seed


class Window(tk.Frame, Table):
    def __init__(self, master=None):
        super().__init__(master)
        Table.__init__(self)
        self.master = master
        self.master.title = "Periodic table guessing game by SynneK1337"
        self.score = 0
        self.create_widgets()
        seed()

    def create_widgets(self):
        self.attempt = 0
        self.element = None
        while not self.element:
            self.element = self.get_by_atomic_number(randint(1, 118))
        self.score_label = tk.Label(self.master)
        self.score_label['text'] = f"Score: {self.score}"
        self.score_label.pack()
        self.prompt = tk.Label(self.master)
        self.prompt['text'] = f'Enter name of element with atomic number equal to {self.element.atomic_number}'
        self.prompt.pack()
        self.input_ = tk.Entry(self.master)

        self.input_.pack()
        self.submit = tk.Button(self.master, text='Submit')
        self.submit['command'] = self.validate_anwear
        self.submit.pack()
        self.reset_btn = tk.Button(self.master, text="Random new element", command=self.randomize)
        self.reset_btn.pack()
        self.get_anwear_btn = tk.Button(self.master, text="Get anwear", command=self.get_anwear).pack()
        self.status = tk.Label(self.master)
        self.status.pack()

    def validate_anwear(self):
        if self.attempt == 5:
            self.game_over()
        if self.element.name.lower() == self.input_.get().lower():
            self.score += 1
            self.status['text'] = "Congratulations!"
            self.score_label['text'] = f"Score: {self.score}"
            self.randomize()

        else:
            self.attempt += 1
            left_or_right = self.get_left_or_right(self.element, self.get_by_name(self.input_.get()))
            if left_or_right:
                self.status['text'] = f"""
                                      Your anwear is incorrect.
                                      Correct element is on the {left_or_right} side of element you providen.
                                      You have {5 - self.attempt} attempts left.
                                      """
            else:
                self.status['text'] = f"Your anwear is incorrect. You have {5 - self.attempt} attempts left."

    def randomize(self):
        self.attempt = 0
        self.element = None
        while not self.element:
            self.element = self.get_by_atomic_number(randint(1, 118))
        self.prompt['text'] = f'Enter name of element with atomic number equal to {self.element.atomic_number}'

    def game_over(self):
        tk._exit()

    def get_anwear(self):
        self.status['text'] = f"Correct anwear is: {self.element.name}"


if __name__ == "__main__":
    root = tk.Tk()
    window = Window(root)
    root.mainloop()