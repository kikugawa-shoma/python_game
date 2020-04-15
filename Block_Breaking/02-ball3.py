from tkinter import *
from dataclasses import dataclass
import time

DURATION=0.01

X=0
Y=100
D=10

@dataclass
class Ball:
    id:int
    x:int
    y:int 
    d:int
    c:str

def make_ball(x,y,d=3,c="black"):
    id=canvas.create_rectangle(x,y,x+d,y+d,fill=c,outline=c)
    return Ball(id,x,y,d,c)

def redraw_ball(ball):
    d=ball.d
    canvas.coords(ball.id,ball.x,ball.y,ball.x+d,ball.y+d)

tk=Tk()    
canvas=Canvas(tk,width=800,height=600,bd=0)
canvas.pack()
tk.update()

ball=make_ball(X,Y,D,"darkblue")

for p in range(0,600,2):
    ball.x=p
    redraw_ball(ball)
    tk.update()
    time.sleep(DURATION)
