from tkinter import *
import time

DURATION=0.01
X_RIGHT=400
X=0
Y=100
D=10

tk = Tk()
canvas=Canvas(tk,width=600,height=400,bd=0)
canvas.pack()
tk.update()

id=canvas.create_rectangle(X,Y,X+D,Y+D,fill="darkblue",outline="black")
for x in range(X,X_RIGHT):
    canvas.coords(id,x,Y,x+D,Y+D)
    tk.update()
    time.sleep(DURATION)
