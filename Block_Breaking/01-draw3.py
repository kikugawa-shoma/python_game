from tkinter import*
import math

def draw_point(x,y,r=1,c="black"):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=c,outline=c)

def f(x):
    return x**2

tk =Tk()
canvas=Canvas(tk,width=1000,height=800,bd=20)
canvas.pack()

for x in range(-400,400):
    draw_point(x,f(x))

tk.mainloop()

 

