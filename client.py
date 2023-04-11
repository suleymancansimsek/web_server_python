# client.py
import sys
import socket

def main():
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    client_socket.send(request.encode())

    response = ''
    while True:
        recv_data = client_socket.recv(1024)
        if not recv_data:
            break
        response += recv_data.decode()

    print(response)
    client_socket.close()

if __name__ == "__main__":
    main()
