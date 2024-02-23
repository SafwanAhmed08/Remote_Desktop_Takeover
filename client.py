import pyautogui as pg
import socket

if __name__ == '__main__':

    host = input('Host: ') 
    port = int(input('Port: ')) 

    client_socket = socket.socket() 
    client_socket.connect((host, port))  

    message = 'sent'
    while True:
        try:
            while message.lower().strip() != 'bye':
                client_socket.send(message.encode())                # send message
                data = client_socket.recv(1024).decode()            # receive response
                if data == 'click':
                    pg.click(x, y)
                
                elif len(data) == 1:
                    pg.typewrite(data)

                elif data.isalpha():
                    pg.press(data.lower())

                else:
                    x = int(data.split(' ')[0])
                    y = int(data.split(' ')[1])
                    pg.moveTo(x, y)                                 # show in terminal
                message = 'done'                                    # again take input

            client_socket.close()                                   # close the connection
        
        except Exception as e:
            print("Error:", e)
            break
