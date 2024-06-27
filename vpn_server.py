# vpn_server.py
from vpnsocket import VPNSocket

def main():
    server = VPNSocket()
    server.bind(('0.0.0.0', 12345))  # Choose a port
    server.listen()

    print("VPN server listening on port 12345...")

    while True:
        client_socket, _ = server.accept()
        print(f"New connection from {client_socket.getpeername()}")

        # Handle client requests here (e.g., forward traffic)

if __name__ == "__main__":
    main()
