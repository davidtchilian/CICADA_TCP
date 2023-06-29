import socket
import random

simple_quine = "quine='quine=%r;print (quine%%quine)';print (quine%quine)"

def handle_command(c, client_socket):
    c = c.split(" ")


    if c[0] == "rand":
        if len(c) < 2 or not c[1].isdigit():
            client_socket.send("02 Error : USAGE : RAND <number>\n".encode())
            return
        client_socket.send(f"01 OK\n".encode())
        for i in range(int(c[1])):
            client_socket.send(f"{random.randint(0, 255)}\n".encode())
        client_socket.send(".\n".encode())
    if c[0] == "quine":
        client_socket.send("01 OK\n".encode())
        q = simple_quine + "\n.\n"
        client_socket.send(q.encode())
    if c[0] == "code":
        client_socket.send("01 OK\n".encode())
        code = open(__file__).read() + "\n.\n"
        client_socket.send(code.encode())
    if c[0] == "base29":
        if len(c) < 2 or not c[1].isdigit():
            client_socket.send("02 Error : USAGE : BASE29 <string>\n".encode())
            return
        client_socket.send("01 OK\n".encode())
        client_socket.send(f"{convert_to_base29(int(c[1]))}\n".encode())
    if c[0] == "koan":
        client_socket.send("01 OK\n".encode())
        with open('koans.txt') as f:
            data = f.read().split('----')
        toprint = data[random.randint(0, len(data)-1)]
        toprint = toprint[1:-1]
        client_socket.send(f"{toprint}\n.\n".encode())
    if c[0] == "dh":
        # Diffie-Hellman key exchange
        if len(c) < 2 or not c[1].isdigit():
            client_socket.send("02 Error : USAGE : DH <number>\n".encode())
            return
        client_socket.send("01 OK\n".encode())
        p = int(c[1])
        # !TODO


def handle_client(client_socket):
    client_address = client_socket.getpeername()
    print(f"Connected to client: {client_address[0]}:{client_address[1]}")

    greeting = "00 Welcome : Welcome to my server ! My favourite snake is the python !\n"
    client_socket.send(greeting.encode())

    while True:
        try:
            command = client_socket.recv(1024).decode().strip().lower()
            if command == "goodbye":
                client_socket.send("99 Goodbye\n".encode())
                client_socket.close()
                break
            if command == "next":
                client_socket.send("01 OK\n".encode())
                with open('next.txt', 'w') as f:
                    while command != ".":
                        command = client_socket.recv(1024).decode().strip()
                        f.write(command + "\n")
                client_socket.send("01 OK\n".encode())
            else:
                handle_command(command, client_socket)

            print(f"Received command from {client_address[0]}:{client_address[1]}: {command}")
        except UnicodeDecodeError:
            print(f"Error decoding data from {client_address[0]}:{client_address[1]}")
            break

    client_socket.close()

def convert_to_base29(n):
    if n == 0:
        return '0'

    base29_digits = []
    while n > 0:
        n, r = divmod(n, 29)
        base29_digit = chr(ord('0') + r) if r < 10 else chr(ord('A') + r - 10)
        base29_digits.append(base29_digit)

    base29_digits.reverse()
    return ''.join(base29_digits)


def run_server():
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")
    while True:
        client_socket, addr = server_socket.accept()
        handle_client(client_socket)
    server_socket.close()

run_server()
