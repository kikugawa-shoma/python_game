from tkinter import *
tk=Tk()

canvas=Canvas(tk,width=400,height=300)
canvas.pack

def on_key_press(event):
    print("key: {}".format(event.keysym))

canvas.bind_all("<KeyPress>",on_key_press)
tk.mainloop()
