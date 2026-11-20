# Student Name: Kartik Kris Pillay
# Student ID: S11229876

# Student Name: Nichel Lal
# Student ID: S11230115

import socket         # Used to enable client-server network communication
import os             # Used to handle file paths and file naming

# -----------------------------
# Client Settings
# -----------------------------
HOST = "127.0.0.1"     # Server IP
PORT = 5000            # Server listening port
BUFFER_SIZE = 4096     # Size of data are received at once

#Displays download progress bar in terminal.
def show_progress(received, total):
    if total == 0:      # Prevent division by zero error
        return          # Stops function if total size is invalid

    percent = (received / total) * 100      # Calculate percentage of file received
    bar_length = 25                         # Length of progress bar

    filled = int(bar_length * received / total)         # Number of filled blocks
    bar = "█" * filled + "-" * (bar_length - filled)    # Build progress bar

    print(f"\rDownloading: [{bar}] {percent:.2f}%", end="")  # Print progress bar on same line


def start_client():

    # Create TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server
        client.connect((HOST, PORT))
        print("Connected to server")

        # Ask user for file name
        filename = input("Enter file name: ").strip()   # Takes input from user and removes extra spaces

        if filename == "":                 # Checks if user did not enter any file name
            print("No file name entered")  # Shows message to user
            return                         # Stops function so nothing is sent to server

        # Send file request
        client.send(filename.encode())

        # Receive response from server and decodes it
        response = client.recv(BUFFER_SIZE).decode()

        # Check if server found file
        if response.startswith("NOTFOUND"):
            print("Server response:", response.split("#")[1])
            return

        # Extract file size
        parts = response.split("#")     # Server sends two pieces of information in one message
        file_size = int(parts[1])       # Extracts file size from server response

        print(f"Downloading file ({file_size} bytes)...")   # Displays file size to user

        received_data = 0               # Tracks how many bytes have been received so far     

        # Creates new file name to avoid overwrite
        new_filename = "downloaded_" + os.path.basename(filename)

        # Open file for writing binary data
        with open(new_filename, "wb") as file:
            while received_data < file_size:
                data = client.recv(BUFFER_SIZE)  # Receives chunk of file data from server

                if not data:                     # Checks if no more data is coming      
                    break

                file.write(data)                 # Writes received data into file
                received_data += len(data)

                # Show progress
                show_progress(received_data, file_size)
                

        print("\nDownload complete")
        print(f"File saved as: {new_filename}")

    except ConnectionRefusedError:              # Handles case where server is not running
        print("Cannot connect to server. Make sure server is running.")

    except Exception as error:                  # Handles any unexpected errors
        print("Client error:", error)

    finally:
        client.close()                          # Ensures socket is closed properly
        print("Connection closed")              # Confirms connection termination 


# Runs the client program only if this file is executed directly
if __name__ == "__main__":
    start_client()