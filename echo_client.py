#echo_client.py
import socket

HEADERSIZE = 10
# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
# HOST = "10.5.0.2"   # Drone side
HOST = "10.5.0.1"   # GS side
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Connect: {HOST} : {PORT}")
        s.connect((HOST, PORT))

        while True:
            full_msg = ''
            new_msg = True
            while True:
                msg = s.recv(16)
                if new_msg:
                    print("new msg len:", msg[:HEADERSIZE])
                    msglen = int(msg[:HEADERSIZE])
                    new_msg = False

                print(f"full message length: {msglen}")

                full_msg += msg.decode("utf-8")

                print(len(full_msg))

                if len(full_msg) - HEADERSIZE == msglen:
                    print("full msg recvd")
                    print(full_msg[HEADERSIZE:])
                    new_msg = True
                    full_msg = ""
