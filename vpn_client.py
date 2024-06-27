# vpn_client.py
from vpnsocket import VPNSocket

def main():
    client = VPNSocket()
    client.connect(('0.0.0.0', 12345))  # Replace with your server's IP and port

    print("Connected to VPN server!")

    # Now you can send/receive data through the VPN connection

if __name__ == "__main__":
    main()
