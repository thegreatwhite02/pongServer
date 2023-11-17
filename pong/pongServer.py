# =================================================================================================
# Contributing Authors:	    Luke Olsen, Will White
# Email Addresses:          Luke.Olsen@uky.edu, Will.White@uky.edu
# Date:                     11/17/2023
# Purpose:                  Creates server that communicates with clients.
# Misc:                     None.
# =================================================================================================

import socket
import threading

### You will need to support at least two clients
### You will need to keep track of where on the screen (x,y coordinates) each paddle is, the score 
### for each player and where the ball is, and relay that to each client
### I suggest you use the sync variable in pongClient.py to determine how out of sync your two
### clients are and take actions to resync the games

##### handle_client()
# Authors: Luke Olsen and Will White
# Purpose: Receives updates from a client and broadcasts the updates to the other clients.
# Pre: handle_client() expects two clients to be connected to the server.
# Post: Both clients disconnect from the server.
def handle_client(client_socket: socket.socket, client_number: int, all_clients: list) -> None:
    while True:
        try:
            # receive game state updates from the client
            msg = client_socket.recv(1024).decode()

            # broadcast to other clients
            for other_client_socket in all_clients:
                if other_client_socket != client_socket:
                    other_client_socket.send(msg.encode())
        
        # break if a client disconnects
        except ConnectionResetError:
                    break
        
    # close socket and remove from list of active clients
    client_socket.close()
    all_clients.remove(client_socket)

# Main server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("10.46.42.92", 12321))
server.listen(2)  # Allow up to 2 simultaneous clients

client_count = 0 # used to decide "host"
clients = [] # list of active clients

# only accept two clients
while client_count < 2:
    client_socket, client_address = server.accept() # accept client connection
    client_count += 1 # increment client count
    clients.append(client_socket) # add to list of connected clients

    # Determine the player's paddle (left or right)
    player_paddle = "left" if client_count == 1 else "right"

    # store the paddle side and client number in a string
    msg = player_paddle + "," + str(client_count)

    # Send the player's paddle information to the client
    client_socket.send(msg.encode())

    # Start a new thread for handle_client(client info)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_count, clients))
    client_thread.start()

# Wait for both threads to finish before closing server
for client_thread in threading.enumerate():
    if client_thread != threading.current_thread():
        client_thread.join()

# close server
server.close()
