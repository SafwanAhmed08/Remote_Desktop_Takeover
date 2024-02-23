import socket 
import tkinter as tk 
from tkinter.messagebox import showinfo 
from random import randint


if __name__ == "__main__":
    
    port = randint(1000, 10000)
    showinfo('Control Data','Host = '+socket.gethostbyname(socket.gethostname())+'\nPort = '+str(port))
   
    root = tk.Tk()
    root.title('Trackpad')
    root.geometry('960x540')
    global x, y, data
    host = socket.gethostname()

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    x = 10
    y = 10
    def motion(event):
        x, y = event.x, event.y
        data = conn.recv(1024).decode()
        print(data)
        data = str(x*2)+' '+str(y*2)
        conn.send(data.encode())


    def click(event):
        conn.send('click'.encode())

    def key(event):
        print(event.keysym)
        conn.send(event.keysym.encode())

    root.bind('<Motion>', motion)
    root.bind('<Button-1>', click)
    root.bind('<Key>', key)

    root.mainloop()