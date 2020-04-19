# -*- coding: utf-8 -*-
from tkinter import *
from dataclasses import dataclass
import random
import time

DURATION=0.01         #描画間隔
PADDLE_X0=750         #パドルの位置(x)
PADDLE_Y0=200         #パドルの位置(y)
BALL_Y0=PADDLE_Y0+20  #ボールの位置(y)

PAD_VY=2              #パドルの速度(y)
BALL_VX=5             #ボールの速度(x)

#パドルの変化しうる色
COLORS=["blue","red","green","yellow","brown","gray"]

NUM_BLOCKS=7
BLOCK_X=20            #ブロックの位置(x)
BLOCK_Y=200            #ブロックの位置(y)
BLOCK_W=20            #ブロックの幅
BLOCK_H=120           #ブロックの高さ

@dataclass
class Ball:
    id:int
    x:int
    y:int
    d:int
    vx:int
    c:str

@dataclass
class Paddle:
    id:int
    x:int
    y:int
    w:int
    h:int
    vy:int
    c:str

@dataclass
class Block:
    id:int
    x:int
    y:int
    w:int
    h:int
    c:str

#ボール
def make_ball(x,y,d,vx,c="black"):
    id=canvas.create_rectangle(x,y,x+d,y+d,
                                fill=c,outline=c)
    return Ball(id,x,y,d,vx,c)

def move_ball(ball):
    ball.x += ball.vx

def redraw_ball(ball):
    canvas.coords(ball.id,ball.x,ball.y,
                  ball.x+ball.d,ball.y+ball.d)


#パドル
def make_paddle(x,y,w=20,h=100,c="blue"):
    id=canvas.create_rectangle(x,y,x+w,y+h,
                                fill=c,outline=c)
    return Paddle(id,x,y,w,h,0,c)

def move_paddle(pad):
    pad.y+=pad.vy

def change_paddle_color(paddle,c="red"):
    canvas.itemconfigure(paddle.id,fill=c)
    canvas.itemconfigure(paddle.id,outline=c)
    redraw_paddle(paddle)

def redraw_paddle(pad):
    canvas.coords(pad.id,pad.x,pad.y,
                    pad.x+pad.w,pad.y+pad.h)

def up_paddle(event):
    paddle.vy=-PAD_VY

def down_paddle(event):
    paddle.vy=PAD_VY

def stop_paddle(event):
    paddle.vy=0


#ブロック
def make_block(x,y,w=20,h=120,c="green"):
    id = canvas.create_rectangle(x,y,x+w,y+h,
                                 fill=c, outline=c)
    return Block(id,x,y,w,h,c)

def make_blocks(n_rows,x0,y0,w,h,pad=10):
    blocks=[]
    for i in range(n_rows):
        x=x0+i*(w+pad)
        blocks.append(make_block(x,y0,w,h))
    return blocks

def delete_block(block):
    canvas.delete(block.id)


#外壁
def make_walls(ox,oy,width,height):
    canvas.create_rectangle(ox,oy,ox+width,oy+height)

tk=Tk()
canvas=Canvas(tk,width=800,height=600,bd=0)
canvas.pack()
tk.update()

#各オブジェクトの生成
paddle=make_paddle(PADDLE_X0,PADDLE_Y0)
ball=make_ball(500,BALL_Y0,10,BALL_VX)
make_walls(0,0,800,600)
blocks=make_blocks(NUM_BLOCKS,BLOCK_X,BLOCK_Y,BLOCK_W,BLOCK_H)

#キーイベントとイベントハンドラを結びつける
canvas.bind_all("<KeyPress-Up>",up_paddle)
canvas.bind_all("<KeyPress-Down>",down_paddle)
canvas.bind_all("<KeyRelease-Up>",stop_paddle)
canvas.bind_all("<KeyRelease-Down>",stop_paddle)

while 1:
    #ボールが左の壁で反射
    if ball.x+ball.vx < 0:
        ball.vx *= -1

    #ボールを逃したら終了
    if ball.x+ball.vx > 800:
        break

    #ボールがパドルに当たったら反射
    if ball.x+ball.d+ball.vx > paddle.x\
       and paddle.y+paddle.vy < ball.y+ball.d\
       and paddle.y+paddle.h+paddle.vy > ball.y:
        ball.vx*=-1
        change_paddle_color(paddle,random.choice(COLORS))

    #ボールがブロックに当たったら反射、ブロック消去
    for block in blocks:
        if block!=None\
        and ball.x + ball.vx < block.x+block.w\
        and ball.y < block.y+block.h\
        and ball.y+ball.d > block.y:
            ball.vx *= -1
            delete_block(block)
            blocks.remove(block) 
    if blocks ==[]:
        break
    #
    move_paddle(paddle)
    move_ball(ball)

    #
    redraw_paddle(paddle)
    redraw_ball(ball)

    tk.update()
    time.sleep(DURATION)

