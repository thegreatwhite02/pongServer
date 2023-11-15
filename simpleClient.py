# simpleClient.py

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            resp = client_socket.recv(1024)
            print(resp.decode())
        except ConnectionResetError:
            break

# Creating the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("10.47.60.82", 12321))

# Start a new thread to continuously receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

msg = ""
while msg.lower() != "quit":
    msg = input("Enter message: ")
    client.send(msg.encode())

# Close the client socket when the loop ends
client.close()
