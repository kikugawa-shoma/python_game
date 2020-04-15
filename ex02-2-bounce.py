from dataclasses import dataclass
from tkinter import *
import time

DURATION=0.01

@dataclass
class Ball:
    id:int
    x:int
    y:int
    d:int
    vx:int
    vy:int
    c:str

@dataclass
class Border:
    left:int
    right:int
    top:int
    bottom:int

def make_ball(x,y,d=10,vx=2,vy=2,c="black"):
    id=canvas.create_rectangle(x,y,x+d,y+d,
                                fill=c,outline=c)
    return Ball(id,x,y,d,vx,vy,c)

def move_ball(ball):
    ball.x=ball.x+ball.vx
    ball.y=ball.y+ball.vy

def redraw_ball(ball):
    canvas.coords(ball.id,ball.x,ball.y,
                    ball.x+ball.d,ball.y+ball.d)

def make_walls(ox,oy,width,height):
    canvas.create_rectangle(ox,oy,ox+width,oy+height)

tk=Tk()
canvas=Canvas(tk,width=800,height=600)
canvas.pack()
tk.update()

border=Border(100,700,100,500)
make_walls(border.left,border.top,
            border.right-border.left,
            border.bottom-border.top)

balls=[make_ball(110,110),
       make_ball(200,300),
       make_ball(500,100),
       make_ball(400,300),]


while 1:
    for ball in balls:
        if ball.x+ball.vx < border.left \
               or ball.x+ball.d+ball.vx > border.right:
            ball.vx *= -1
    
        if ball.y+ball.vy < border.top \
               or ball.y+ball.d+ball.vy > border.bottom:
            ball.vy *= -1
    
        move_ball(ball)
        redraw_ball(ball)
    tk.update()
    time.sleep(DURATION)