import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    lottery_number = ""
    # TODO 1) Get 6 random numbers to put on your lottery ticket
    for i in range(6):
        number = random.randint(1, 60)
        lottery_number = lottery_number + str(number) + " "
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title='lottery ticket', message=lottery_number)
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
