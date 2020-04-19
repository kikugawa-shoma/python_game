from tkinter import *
from dataclasses import dataclass
import time
import math

DURATION=0.01

REFLECT_DEGREE=45

PADDLE_X0=450
PADDLE_Y0=600
PADDLE_VX=2

BALL_X0=495
BALL_Y0=200
BALL_D=10
BALL_VY0=3
BALL_VX0=0

BLOCK_X=100
BLOCK_Y=150
BLOCK_W=100
BLOCK_H=20
BLOCK_NUM=5
BLOCK_PAD=10

WALL_W=100
WALL_N=100
WALL_E=900
WALL_S=700

@dataclass
class Game:
    start:int

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
class Paddle:
    id:int
    x:int
    y:int
    w:int
    h:int
    vx:int
    c:str

@dataclass
class Block:
    id:int
    x:int
    y:int
    w:int
    h:int
    c:str

def game_start(event):
    game.start=True

def make_walls(east,west,south,north):
    canvas.create_rectangle(west,north,east,south)

def make_ball(x,y,d,vx,vy,c="black"):
    id=canvas.create_rectangle(x,y,x+d,y+d,fill=c,outline=c)
    return Ball(id,x,y,d,vx,vy,c)

def move_ball(ball):
    ball.x+=ball.vx
    ball.y+= ball.vy

def redraw_ball(ball):
    canvas.coords(ball.id,ball.x,ball.y,
                  ball.x+ball.d,ball.y+ball.d)


def make_paddle(x,y,w=100,h=20,c="blue"):
    id=canvas.create_rectangle(x,y,x+w,y+h,fill=c,outline=c)
    return Paddle(id,x,y,w,h,0,c)

def move_paddle(pad):
    if WALL_W <= pad.x+pad.vx and pad.x+pad.w+pad.vx <= WALL_E:
        pad.x+=pad.vx

def redraw_paddle(pad):
    canvas.coords(pad.id,pad.x,pad.y,pad.x+pad.w,pad.y+pad.h)

def left_paddle(event):
    paddle.vx=-PADDLE_VX

def right_paddle(event):
    paddle.vx=PADDLE_VX

def stop_paddle(event):
    paddle.vx=0

def make_block(x,y,w,h,c="green"):
    id=canvas.create_rectangle(x,y,x+w,y+h,
                            fill=c,outline=c)
    return Block(id,x,y,w,h,c)

def make_blocks(block_num,x0,y,w,h,pad):
    blocks=[]
    for i in range(block_num):
        x=x0+i*(w+pad)
        blocks.append(make_block(x,y,w,h))
    return blocks

def delete_block(block):
    canvas.delete(block.id)

game=Game(False)

tk=Tk()
canvas=Canvas(tk,width=1000,height=800,bd=0)
canvas.pack()
tk.update()

make_walls(WALL_E,WALL_W,WALL_S,WALL_N)
ball=make_ball(BALL_X0,BALL_Y0,BALL_D,BALL_VX0,BALL_VY0)
paddle=make_paddle(PADDLE_X0,PADDLE_Y0)
blocks=make_blocks(BLOCK_NUM,BLOCK_X,BLOCK_Y,BLOCK_W,BLOCK_H,BLOCK_PAD,)

canvas.bind_all("<KeyPress-Left>",left_paddle)
canvas.bind_all("<KeyPress-Right>",right_paddle)
canvas.bind_all("<KeyRelease-Left>",stop_paddle)
canvas.bind_all("<KeyRelease-Right>",stop_paddle)

canvas.bind_all("<KeyPress-space>",game_start)

id_text=canvas.create_text(500,400,text="Press 'SPACE' to start",
                            font=('FixedSys',25))
tk.update()

while not game.start:
    tk.update()
    time.sleep(DURATION)

canvas.delete(id_text)
tk.update()


while 1:
    if ball.x+ball.vx < WALL_W\
       or ball.x+ball.d+ball.vx > WALL_E:
        ball.vx *= -1
    
    if ball.y < WALL_N:
        ball.vy *= -1

    if (ball.x+ball.d+ball.vx > paddle.x\
        and ball.x+ball.vx < paddle.x+paddle.w)\
        and ball.y+ball.d+ball.vy >= paddle.y\
        and ball.y+ball.d+ball.vy <= paddle.y+paddle.h/2:
        W=paddle.w+ball.d
        ball_pos=paddle.x+paddle.w+ball.d//2-(ball.x+ball.d//2)
        r=ball_pos/W
        r=(r-0.5)*2
        rad=math.radians(r*REFLECT_DEGREE)
        ball.vy=-BALL_VY0*math.cos(rad)
        ball.vx=-BALL_VY0*math.sin(rad)


        
    for block in blocks:
        if block.x < ball.x+ball.d+ball.vx\
           and block.x+block.w > ball.x+ball.vx\
           and block.y+block.h > ball.y+ball.vy:
            ball.vy*=-1
            delete_block(block)
            blocks.remove(block)
    
    if ball.y+ball.d > WALL_S:
        id_text=canvas.create_text(500,400,text="Game Over!",
                                    font=('FixedSys',28))
        while 1:
            tk.update()
            time.sleep(DURATION)

    if blocks==[]:
        id_text=canvas.create_text(500,400,text="Clear!",
                                    font=('FixedSys',28))
        while 1:
            tk.update()
            time.sleep(DURATION)

    move_paddle(paddle)
    move_ball(ball)

    redraw_paddle(paddle)
    redraw_ball(ball)

    tk.update()
    time.sleep(DURATION)

