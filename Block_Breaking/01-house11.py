from tkinter import *

tk = Tk()
canvas = Canvas(tk,width=500,height = 400,bd=0)
canvas.pack()

canvas.create_polygon(100,100,0,200,200,200,outline = "blue",fill="red")

canvas.create_rectangle(0,200,200,300,outline="gray",fill="gray")
tk.mainloop()


