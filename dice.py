from tkinter import *
import random

class Roll():
    def __init__(self,master):
        self.master = master
        self.master.title("Dice Roller")
        self.master.geometry("350x200")
        self.master.resizable(0,0)
        self.runs = 0
        score = self.roll()

        bg_color = "f77f77" #light red
        style = "Arial 20"

        self.master.rowconfigure([0,1], minsize=50)
        self.master.columnconfigure([0,1,2], minsize=50)

        self.button1 = Button(master,command=self.quit, text="Close window", font =style)
        self.button1.grid(row=0, column=0, padx = 10, pady=10, sticky = W)

        self.button2 = Button(self.master, text="Reroll", command=self.roll, font =style)
        self.button2.grid(row=0, column=1, padx = 10, pady=10, sticky = E)
    def quit(self):
        self.master.destroy()
    def roll(self):
        self.runs += 1
        bg_color = "f77f77" #light red
        style = "Arial 20"

        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        if self.dice1 == 6 and self.dice2 == 6:
            self.label1 = Label(self.master, text =self.dice1, bg = "green", font = style)
            self.label1.grid(row=1,column=0, padx = 10, pady = 10)

            self.label2 = Label(self.master, text =self.dice2, bg = "green", font = style)
            self.label2.grid(row=1,column=1, padx = 10, pady=10)
        else:
            self.label1 = Label(self.master, text =self.dice1, font = style)
            self.label1.grid(row=1,column=0, padx = 10, pady = 10)

            self.label2 = Label(self.master, text =self.dice2, font = style)
            self.label2.grid(row=1,column=1, padx = 10, pady=10)

        self.label3 = Label(self.master, text = "Rolls:", font = style)
        self.label3.grid(row=2,column=0, padx = 10, pady = 10)

        self.label4 = Label(self.master, text = self.runs, font = style)
        self.label4.grid(row=2,column=1, padx = 10, pady=10)


root = Tk()
app = Roll(root)
root.mainloop()
