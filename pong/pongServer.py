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

# Use this file to write your server logic
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Creating the server
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # Working on localhost need this
server.bind(("10.47.132.222", 12321)) # args are IP, port
server.listen(5)

clientSocket, clientAddress = server.accept()

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

"""
msg = ""
while True:
    msg = clientSocket.recv(1024).decode()          # Received message from client
    print(f"Client sent: {msg}")
    clientSocket.send(msg.encode())



clientSocket.close()
server.close()

def updatePaddles():
    global xPos1, yPos1, xPos2, yPos2
    while True:
        if not pongUpdate.isGameOver():
            xPos1, yPos1, xPos2, yPos2 = pongUpdate.updatePaddles()
            time.sleep(.001)
        else:
            break

def sendScoresToClients():
    while True:
        scores = pongUpdate.getScore()
        clientSocket.sendall((str(scores[0]) + "," + str(scores[1])).encode())
        time.sleep(.001)
        break
    pongThread = threading.Thread(target=updatePaddles)
    pongThread.start()
    scoresThread = threading.Thread(target=sendScoresToClients)
    scoresThread.start()
    pongUpdate.initiateGame()
"""
#testing if git push works