import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3
    bobby1545 = random.randint(0,3)

    # If the random number is 0
    if bobby1545 == 0:
        bob = simpledialog.askstring(title='shrek', prompt='ask me something')
        messagebox.showinfo(title='f', message='yes')
        # tell the user "Yes"

    # If the random number is 1
    if bobby1545 == 1:
        messagebox.showinfo(title='g', message='no')
        # tell the user "No"

    # If the random number is 2
    if bobby1545 == 2:
        messagebox.showinfo(title='', message='ask google')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if bobby1545 == 3:
        messagebox.showinfo(title='', message='SHUT UP!!!')
        # write your own answer
