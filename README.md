# CICADA_TCP

This project is an implementation of a TCP server using Python. It allows for communication between a client and server using the Transmission Control Protocol (TCP) network protocol.

## Features

- **TCP Server:** The project includes a TCP server that can handle incoming client connections and facilitate communication.

- **Message Handling:** The server supports sending and receiving messages between the client and server.

## Prerequisites

To run the TCP server, make sure you have the following installed:

- Python 3.x: You can download it from the official Python website: https://www.python.org/downloads/ or install it using your operating system's package manager.

## Usage

1. Clone the repository:

```
git clone https://github.com/davidtchilian/CICADA_TCP.git
```

2. Navigate to the project directory:

```
cd CICADA_TCP
```

3. Run the server:

```
python3 cicadatcp.py
```

4. The server will start listening for client connections on a specified port (default: 12345). Make sure the port is not blocked by a firewall or used by another process.

5. Connect a client to the server:

In another terminal, run the following command:

```
telnet <host> <port>
# Example: telnet localhost 12345
```

6. The client will establish a connection with the server. You can now start sending and receiving messages between the client and server.

## Configuration

You can modify the server configuration by editing the `cicadatcp.py` file. The file allows you to specify the server's listening IP address (host variable) and port.

## License

This project is licensed under the MIT License.

## Acknowledgments

The project was inspired by the Cicada 3301 puzzles, which challenged participants to code a TCP server as part of the puzzle-solving process.

The original mail that the participants received is available in the cicada_mail.txt file.
