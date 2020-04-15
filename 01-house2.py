from tkinter import *
from dataclasses import dataclass

@dataclass
class House:
    w:int
    h:int
    roof_color:str
    wall_color:str

house = House(200,200,"red","gray")
print(house)

def draw_house_at(x,y,w,h,roof_color,wall_color):
    rtop_x = x+w/2
    wtop_y = y+h/2
    bottom_x = x+w
    bottom_y = y+h
    canvas.create_polygon(rtop_x,y,
                            x,wtop_y,
                            x+w,wtop_y,
                            outline=roof_color,fill=roof_color)
    canvas.create_rectangle(x,wtop_y,bottom_x,bottom_y,outline=wall_color,fill=wall_color)

def draw_house(house,x,y):
    w = house.w
    h = house.h
    roof_color = house.roof_color
    wall_color = house.wall_color
    draw_house_at(x,y,w,h,roof_color,wall_color)

tk = Tk()
canvas=Canvas(tk,width=500,height=400,bd=0)
canvas.pack()

house=House(200,200,"red","gray")
print(house)
draw_house(house,0,100)
tk.mainloop()
