import socket         #Library needed for sockets  
import threading   

def handle_client(client_socket, client_number, all_clients):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            print(f"Client {client_number} sent: {msg}")
            
            # Broadcast the message to all other clients
            for other_client_socket in all_clients:
                if other_client_socket != client_socket:
                    other_client_socket.send(f"Client {client_number} sent: {msg}".encode())

            
            if msg.lower() == "quit":
                break
        except ConnectionResetError:
            break

    print(f"Client {client_number} disconnected.")
    client_socket.close()

#Main server setup
server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #Creating the client
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #Working on local host needs this
server.bind(("10.47.60.82", 12321))
server.listen(2) # Allow up to 2 simultaneous clients

print("Server listening on 10.47.60.82:12321...")

client_count = 0
clients = []

while client_count < 2:
    client_socket, client_address = server.accept()
    client_count += 1
    print(f"Accepted connection from {client_address}")
    clients.append(client_socket)
    
    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_count, clients))
    client_thread.start()

# Wait for both threads to finish
#client_thread.join()
#client_thread.join()

for client_thread in threading.enumerate():
    if client_thread != threading.current_thread():
        client_thread.join()

server.close()





#clientSocket, clientAddress = server.accept()

# message = clientSocket.recv(1024)                                # Expect "Hello Server

# print(f"Client sent: {message.deocde()}")

# clientSocket.send("Hello client.".encode())

#msg = ""
#while msg != "quit":
    #msg = clientSocket.recv(1024).decode()                     # Receieved message from client 
    #print(f"Client sent: {msg}")
    #clientSocket.send(msg.encode())

#clientSocket.close()
#server.close()
