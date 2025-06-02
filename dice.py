from tkinter import *
import random

class Roll():
    def __init__(self,master):
        self.master = master
        self.master.title("Dice Roller")
        self.master.resizable(0,0)

        score = self.roll()

        self.master.rowconfigure([0,1], minsize=50)
        self.master.columnconfigure([0,1,2], minsize=50)

        self.button1 = Button(master,command=self.quit, text="Close window")
        self.button1.grid(row=0, column=0)

        self.button2 = Button(self.master, text="Reroll", command=self.roll)
        self.button2.grid(row=0, column=1)

        


    def quit(self):
        self.master.destroy()
    def roll(self):
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        self.score = self.dice1 + self.dice2

        self.label1 = Label(self.master, text =self.dice1)
        self.label1.grid(row=1,column=0)

        self.label2 = Label(self.master, text =self.dice2)
        self.label2.grid(row=1,column=1)

        self.label3 = Label(self.master, text = "Total:")
        self.label3.grid(row=2,column=0)

        self.label4 = Label(self.master, text = self.score)
        self.label4.grid(row=2,column=1)


root = Tk()
app = Roll(root)
root.mainloop()
