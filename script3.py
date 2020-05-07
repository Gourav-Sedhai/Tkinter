from tkinter import *

window=Tk()

def calculator():
    add=float()
    sub=float()
    mul=float()
    div=float()

k=0

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=0, columnspan=6, pady=3)

for i in range(3,6):
    for j in range(0,3):
        k=k+1
        b1=Button(window, text=k,width=5,height=3,fg="red",bg="#fffff0")
        b1.grid(row=i,column=j)

b1=Button(window, text="+",width=5,height=3,fg="red",bg="#fffff0")
b1.grid(row=3,column=3)

b1=Button(window, text="-",width=5,height=3,fg="red",bg="#fffff0")
b1.grid(row=4,column=3)

b1=Button(window, text="*",width=5,height=3,fg="red",bg="#fffff0")
b1.grid(row=5,column=3)

b1=Button(window, text="clr",width=5,height=3,fg="red",bg="#fffff0")
b1.grid(row=6,column=0)

b1=Button(window, text="0",width=5,height=3,fg="red",bg="#fffff0")
b1.grid(row=6,column=1)

b1=Button(window, text="=",width=5,height=3,fg="red",bg="#fffff0")
b1.grid(row=6,column=2)

b1=Button(window, text="/",width=5,height=3,fg="red",bg="#fffff0")
b1.grid(row=6,column=3)

window.mainloop()