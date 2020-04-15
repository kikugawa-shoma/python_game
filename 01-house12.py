from tkinter import *

def draw_haouse_at(x,y,w,h,roof_color,wall_color):
    rtop_x = x+w/2
    wtop_y = y+h/2
    bottom_x = x+w
    bottom_y = y+h
    canvas.create_polygon(rtop_x,y,
                            x,wtop_y,
                            x+w,wtop_y,
                            outline=roof_color,fill=roof_color)
    canvas.create_rectangle(x,wtop_y,bottom_x,bottom_y,outline=wall_color,fill=wall_color)
tk = Tk()
canvas = Canvas(tk,width = 500,height=400,bd=0)
canvas.pack()

draw_haouse_at(0,100,200,200,"red","gray")
tk.mainloop()

