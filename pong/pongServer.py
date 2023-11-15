# =================================================================================================
# Contributing Authors:	    Luke Olsen, Will White
# Email Addresses:          Luke.Olsen@uky.edu, Will.White@uky.edu
# Date:                     11/7/2023
# Purpose:                  This file sets up the server that communicates with clients.
# Misc:                     None.
# =================================================================================================

import socket
import threading

# Use this file to write your server logic
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Creating the server
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # Working on localhost need this
server.bind(("10.47.132.222", 12321)) # args are IP, port
server.listen(5)

### You will need to support at least two clients
# each client needs to have this line "client.connect(("localhost", 12321))" to connect
### You will need to keep track of where on the screen (x,y coordinates) each paddle is, the score 
### for each player and where the ball is, and relay that to each client
### I suggest you use the sync variable in pongClient.py to determine how out of sync your two
### clients are and take actions to resync the games

# it would probably be good to have an "update" object with paddle positions and all that

#testing if git push works