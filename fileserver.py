# Student Name: Kartik Kris Pillay
# Student ID: S11229876

# Student Name: Nichel Lal
# Student ID: S11230115

import socket          # Used to enable client-server network communication
import os              # Used to handle file paths and file naming

# -----------------------------
# Server Settings
# -----------------------------
HOST = "127.0.0.1"     # Server IP
PORT = 5000            # Server listening port
BUFFER_SIZE = 4096     # Size for sending file data


# Create a TCP socket using IPv4
def start_server():                         
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind server to IP and port so clients know where to connect
        server.bind((HOST, PORT))

        # Listen for 1 client connection at a time
        server.listen(1)

        print("Server started on 127.0.0.1:5000")     # Shows server has started
        print("Waiting for client connection...\n")   # Indicates server is idle waiting

        # Accept connection from client
        connection, address = server.accept()
        print(f"Client connected from {address}")     # Displays client IP and port

        # Receive requested file name from client
        requested_file = connection.recv(BUFFER_SIZE).decode().strip()

        # Remove any path and keep only filename (security)
        requested_file = os.path.basename(requested_file)

        print(f"Client requested: {requested_file}")

        # Check if file exists in current folder
        if os.path.isfile(requested_file):

            # Get file size
            file_size = os.path.getsize(requested_file)

            # Send success message with file size info
            message = f"FOUND#{file_size}"
            connection.send(message.encode())       # Sends file info to client    

            print("Sending file...")                # Indicates file transfer has started

            # Open file in binary mode
            with open(requested_file, "rb") as file:
                while True:
                    chunk = file.read(BUFFER_SIZE)  # Read file in chunks

                    if not chunk:                   # Stop when file ends
                        break

                    connection.sendall(chunk)       # Send chunk to client

            print("File transfer successful")

        else:
            # If file does not exist, send error message
            connection.send("NOTFOUND#File not available".encode())
            print("Requested file not found")

        # Close connection after operation
        connection.close()

    except Exception as error:              # Prints any runtime errors
        print("Server error:", error)

    finally:
        # Always close server socket
        server.close()
        print("Server shut down")


# Runs server only if file is executed directly
if __name__ == "__main__":
    start_server()              # Starts server program