from tkinter import *
from tkinter import ttk

root = Tk()


v = str


def clearer():
    enterer.delete(0, END)


def set_text(word):
    enterer.insert(END, str(word))
    return


def equal():
    '''viktigt, bli av med eval och använd
def numeric(equation):
    if '+' in equation:
        y = equation.split('+')
        x = int(y[0])+int(y[1])
    elif '-' in equation:
        y = equation.split('-')
        x = int(y[0])-int(y[1])
    return x
    '''


#TODO,  gör en loop. radera allt karaktär för karaktär om karaktären finns i usable så raderas den inte och hoppas över
    a = enterer.get()
    usable = set('1234567890+')
    k = 0
    for i in a:
        if i not in usable:
            enterer.delete(k)
        else:
            k+=1


    answer = eval(enterer.get())
    enterer.delete(0, END)
    enterer.insert(0, str(answer))
    return


frm = ttk.Frame(root, padding=20)

enterer = ttk.Entry(root, textvariable=v)
enterer.pack()
Button1 = ttk.Button(root, text=1, command=lambda: set_text(1)).pack()
Button2 = ttk.Button(root, text=2, command=lambda: set_text(2)).pack()
Button3 = ttk.Button(root, text=3, command=lambda: set_text(3)).pack()
Button4 = ttk.Button(root, text=4, command=lambda: set_text(4)).pack()
Button5 = ttk.Button(root, text=5, command=lambda: set_text(5)).pack()
Button6 = ttk.Button(root, text=6, command=lambda: set_text(6)).pack()
Button7 = ttk.Button(root, text='+', command=lambda: set_text('+')).pack()
Answerer = ttk.Button(root, text='=', command=lambda: equal()).pack()
deleter = ttk.Button(root, text='delete', command=lambda: clearer()).pack()
root.mainloop()
