from tkinter import *
from random import randint

def calcola():
    a=[]
    while len(a)<6:
        num=randint(1,90)
        if num not in a:
            a.append(num)
        a.sort()
    entry=Entry(frame, takefocus=0)
    entry.grid(row=0, column=1, padx=(0, 10))
    entry.delete(0,END)
    entry.insert(END, str(a))

root=Tk()
root.title("Lottrygen")
root.resizable(False, False)
frame=LabelFrame(root, text="Sestine Superenalotto")
frame.pack()
button=Button(frame, text="Generate!", command=calcola)
button.grid(row=0, column=0, padx=10, pady=5)
button.focus()
entry=Entry(frame, takefocus=0)
entry.grid(row=0, column=1, padx=(0, 10))
root.mainloop()