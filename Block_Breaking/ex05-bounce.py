from tkinter import *
import time

WALL_E=50
WALL_W=450
WALL_S=350
WALL_N=50

DURATION_sec=0.01

class Ball:
    def __init__(self,id,x,y,d,vx,vy):
        self.id=id
        self.x=x
        self.y=y
        self.d=d
        self.vx=vx
        self.vy=vy
    
    def move(self):
        self.x+=self.vx
        self.y+=self.vy

    def redraw(self):
        canvas.coords(self.id,self.x,self.y,self.x+self.d,self.y+self.d)

def create_ball(x,y,d,vx,vy):
    id=canvas.create_rectangle(x,y,x+d,y+d,fill="black")
    ball=Ball(id,x,y,d,vx,vy)
    return ball

def make_walls(east,west,south,north):
    canvas.create_rectangle(west,north,east,south)

tk=Tk()
canvas=Canvas(tk,width=500,height=400,bd=0)
canvas.pack()

make_walls(WALL_E,WALL_W,WALL_S,WALL_N)
balls=[create_ball(100,100,10,3,2),
       create_ball(120,300,15,3,3),
       create_ball(400,150,12,1,3),
       create_ball(200,200,5,5,5)]

while 1:
    for ball in balls:
        if ball.x+ball.vx < WALL_E\
            or ball.x+ball.vx+ball.d > WALL_W:
            ball.vx *= -1
        if ball.y+ball.vy < WALL_N\
            or ball.y+ball.vy+ball.d > WALL_S:
            ball.vy *= -1
        ball.move()
        ball.redraw()
    tk.update()
    time.sleep(DURATION_sec)