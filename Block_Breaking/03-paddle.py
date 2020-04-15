from tkinter import *
from dataclasses import dataclass
import time

DURATION=0.01
PADDLE_X0=750
PADDLE_Y0=200
PAD_VY=2

@dataclass
class Paddle:
    id:int
    x:int
    y:int
    w:int
    h:int
    vy:int
    c:str

def make_paddle(x,y,w=20,h=100,c="blue"):
    id=canvas.create_rectangle(x,y,x+w,y+h,
                                fill=c,outline=c)
    return Paddle(id,x,y,w,h,0,c)

def move_paddle(pad):
    pad.y+=pad.vy

def redraw_paddle(pad):
    canvas.coords(pad.id,pad.x,pad.y,
                    pad.x+pad.w,pad.y+pad.h)

def up_paddle(event):
    paddle.vy=-PAD_VY

def down_paddle(event):
    paddle.vy=PAD_VY

def stop_paddle(event):
    paddle.vy=0

tk=Tk()
canvas=Canvas(tk,width=800,height=600,bd=0)
canvas.pack()
tk.update()

paddle=make_paddle(PADDLE_X0,PADDLE_Y0)

canvas.bind_all("<KeyPress-Up>",up_paddle)
canvas.bind_all("<KeyPress-Down>",down_paddle)
canvas.bind_all("<KeyRelease-Up>",stop_paddle)
canvas.bind_all("<KeyRelease-Down>",stop_paddle)
while 1:
    move_paddle(paddle)
    redraw_paddle(paddle)
    tk.update()
    time.sleep(DURATION)

