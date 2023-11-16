# =================================================================================================
# Contributing Authors:	    Luke Olsen, Will White
# Email Addresses:          Luke.Olsen@uky.edu, Will.White@uky.edu
# Date:                     11/7/2023
# Purpose:                  This file sets up the server that communicates with clients.
# Misc:                     None.
# =================================================================================================

import socket
import threading
import pongUpdate
import time
from assets.code.helperCode import Paddle, Ball, updateScore


### You will need to support at least two clients
# each client needs to have this line "client.connect(("localhost", 12321))" to connect
### You will need to keep track of where on the screen (x,y coordinates) each paddle is, the score 
### for each player and where the ball is, and relay that to each client
### I suggest you use the sync variable in pongClient.py to determine how out of sync your two
### clients are and take actions to resync the games

### 11/15: GENERAL PIPELINE
# players send updates
# server processes the updates and resolves issues
# server sends updates to players
# players process updates and show updated game state
# repeat

### IT WOULD BE INCREDIBLY HELPFUL if we could define functions to
### send/receive messages so that we could just call the functions
### instead of trying to figure stuff out every time we need to do it
### so functions send(client, updatePacket) and receive(...).

# Add a global dictionary to store the current position of each paddle
paddle_positions = {"left": 0, "right": 0}

def handle_client(client_socket, client_number, all_clients, player_paddle):
    global paddle_positions
    
    while True:
        try:
            # Receive game state updates from the client
            msg = client_socket.recv(1024).decode()
            
            msg_type, msg_content = msg.split(',', 1)

            if msg_type == "paddle_movement":
                # Extract paddle movement information from the message
                paddle_movement = msg_content

                # Update the server's knowledge of the player's paddle movement
                if player_paddle == "left":
                    paddle_positions["left"] += 1 if paddle_movement == "down" else -1
                elif player_paddle == "right":
                    paddle_positions["right"] += 1 if paddle_movement == "down" else -1

                # Broadcast the updated paddle positions to all other clients
                for other_client_socket in all_clients:
                    if other_client_socket != client_socket:
                        other_client_socket.send(msg.encode())


            # Broadcast the game state to all other clients
            for other_client_socket in all_clients:
                if other_client_socket != client_socket:
                    other_client_socket.send(msg.encode())

        except ConnectionResetError:
            break

    print(f"Client {client_number} disconnected.")
    client_socket.close()
    all_clients.remove(client_socket)

# Main server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("10.47.60.82", 12321))
server.listen(2)  # Allow up to 2 simultaneous clients

print("Server listening on 10.47.60.82:12321...")

client_count = 0
clients = []

while client_count < 2:
    client_socket, client_address = server.accept()
    client_count += 1
    print(f"Accepted connection from {client_address}")
    clients.append(client_socket)

    # Determine the player's paddle (left or right)
    player_paddle = "left" if client_count == 1 else "right"

    # Send the player's paddle information to the client
    client_socket.send(player_paddle.encode())

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_count, clients, player_paddle))
    client_thread.start()

# Wait for both threads to finish
for client_thread in threading.enumerate():
    if client_thread != threading.current_thread():
        client_thread.join()

server.close()

