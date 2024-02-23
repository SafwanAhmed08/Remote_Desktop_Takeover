import tkinter as tk 
from tkinter.messagebox import showinfo 

x = 10
y = 10

def motion(event):
    x, y = event.x, event.y
    data = str(x)+' '+str(y)
    print(data)

def key(event):
    print(event.keysym)

def click(event):
    print(event)

root = tk.Tk()
root.title('Trackpad')
root.geometry('960x540')

root.bind('<Motion>', motion)
root.bind('<Button-1>', click)
root.bind('<Key>', key)
root.mainloop()