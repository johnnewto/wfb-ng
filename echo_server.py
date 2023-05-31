#echo_client.py
import socket
import time


HEADERSIZE = 10
# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
HOST = "10.5.0.2"  # drone
# HOST = "10.5.0.1"   # GS  side
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Bind: {HOST} : {PORT}")
        s.bind((HOST, PORT))
        s.listen(5)

        while True:
            # now our endpoint knows about the OTHER endpoint.
            clientsocket, address = s.accept()
            print(f"Connection from {address} has been established.")

            msg = "Welcome to the server!"
            msg = f"{len(msg):<{HEADERSIZE}}"+msg

            clientsocket.send(bytes(msg,"utf-8"))

            while True:
                time.sleep(0.05)
                msg = f"The time is {time.time()}"
                msg = f"{len(msg):<{HEADERSIZE}}"+msg

                print(msg)

                clientsocket.send(bytes(msg,"utf-8"))
