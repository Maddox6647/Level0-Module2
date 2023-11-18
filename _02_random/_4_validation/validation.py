import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range(10):
        shrek = simpledialog.askstring(title='shrek', prompt='enter a number, 1 to 5')
    else:
        messagebox.showerror(title='shhhshshsshshshshshshsh', message='U SUCK MAN!!!')
        if shrek == 1:
            messagebox.showinfo(title='gsjsgjsjgsdd', message=' u r good')
        elif shrek == 2:
            messagebox.showinfo()
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
