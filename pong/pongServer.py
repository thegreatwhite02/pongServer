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
# You will need to support at least two clients
# You will need to keep track of where on the screen (x,y coordinates) each paddle is, the score 
# for each player and where the ball is, and relay that to each client
# I suggest you use the sync variable in pongClient.py to determine how out of sync your two
# clients are and take actions to resync the games