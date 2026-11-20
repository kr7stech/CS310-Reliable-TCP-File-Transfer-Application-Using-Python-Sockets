					CS310 – Computer Networks
			Assignment 1: File Transfer System using TCP Socket Programming


Student Name: Kartik Kris Pillay
Student ID:   S11229876

Student Name: Nichel Lal
Student ID:   S11230115



	PROJECT DESCRIPTION

This project implements a simple file transfer system using Python socket programming over TCP. It consists of a server program and a client program that communicate over a localhost connection.

The server listens for incoming client requests, checks whether the requested file exists, and sends it if available. The client requests a file, receives it in binary form, and saves it locally while displaying download progress.

The project demonstrates key networking concepts such as socket programming, client-server communication, reliable data transfer, file handling, and progress monitoring.



	REQUIREMENTS

- Python 3.x installed
- Programs run on the same machine (localhost)
- No external libraries required



	HOW TO RUN THE PROGRAM

Step 1: Open Command Prompt and go to the server folder

	cd Desktop\Kartik_S11229876_FileTransfer_Assignment\server


Step 2: Start the server

	py fileserver.py

- The server will start and wait for a client connection.


Step 3: Open a new Command Prompt window and navigate to the client folder

	cd Desktop\Kartik_S11229876_FileTransfer_Assignment\client


Step 4: Run the client

	.\client.py


Step 5: Enter the file name when prompted

Examples:
	test.txt
	test.jpg
	test.pdf



	SYSTEM WORKFLOW

1. The server starts and waits for a client to connect.
2. The client connects and sends the name of the requested file.
3. The server checks if the file exists in its directory.
4. If the file exists:
	- The server sends a confirmation message along with file size.
	- The file is transmitted in chunks.

5. The client receives the file and writes it to a new file.
6. A progress bar is displayed showing the percentage of download.
7. Once the transfer is complete, both server and client display success messages.
8. If the file does not exist, an error message is shown.



	FEATURES IMPLEMENTED

- TCP socket communication using Python
- Single client connection (no multithreading)
- File existence validation on server
- File transfer in binary format (supports all file types [txt, .jpg, .pdf etc.])
- Real-time progress bar during download
- Error handling for invalid file requests
- Automatic file saving with "downloaded_" prefix



	TESTING

The program was tested using multiple file types:

- test.txt (small file) to verify basic functionality
- test.jpg (image file) to confirm binary file transfer
- test.pdf (~220KB) to demonstrate the progress bar clearly

All files were successfully transferred and opened after download.



	IMPORTANT NOTES

- The requested file must be located in the same directory or folder as fileserver.py
- Only the file name should be entered (not full file path)
- The server must be started before running the client
- The system uses IP address 127.0.0.1 and port 5000
- Downloaded files are saved inside the client folder



	AI DECLARATION STATEMENT

I declare that this assignment is my own work and has been completed independently in collaboration with my partner. Artificial Intelligence was used only to support understanding of concepts and improve clarity. It was not used to generate the final program code. All code, logic, and implementation submitted are the result of our own work and reflect our understanding of socket programming concepts.



	CONCLUSION

This project successfully demonstrates a basic file transfer system using TCP sockets. It shows how reliable communication can be established between a client and server, and how data can be transferred efficiently with progress monitoring.




