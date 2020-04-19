from dataclasses import dataclass
from tkinter import *
import time

DURATION=0.01
X0=150
Y0=150
D=15
VX0=2

@dataclass
class Ball:
    id:int
    x:int
    y:int
    d:int
    c:str
    vx:int

@dataclass
class Border:
    left:int
    right:int
    top:int
    bottom:int

def make_ball(x,y,d=3,c="black",vx=2):
    id = canvas.create_rectangle(x,y,x+d,y+d,fill=c,outline=c)
    return Ball(id,x,y,d,c,vx)

def move_ball(ball):
    ball.x=ball.x+ball.vx

def make_walls(ox,oy,width,height):
    canvas.create_rectangle(ox,oy,ox+width,oy+height)

def redraw_ball(ball):
    d=ball.d
    canvas.coords(ball.id,ball.x,ball.y,ball.x+d,ball.y+d)

tk=Tk()
canvas=Canvas(tk,width=800,height=600,bd=0)
canvas.pack()
tk.update()

border=Border(100,700,100,500)

make_walls(
    border.left,border.top,
    border.right-border.left,
    border.bottom-border.top
)
ball=make_ball(X0,Y0,D,"black",VX0)

while 1:
    move_ball(ball)
    if ball.x+ball.vx < border.left \
        or ball.x+ball.d+ball.vx > border.right:
        ball.vx *= -1
    redraw_ball(ball)
    tk.update()
    time.sleep(DURATION)

