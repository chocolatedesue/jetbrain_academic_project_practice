import sys
import socket
import itertools

host = sys.argv[1]
port = int(sys.argv[2])

with socket.socket() as client_socket:
    address = (host, port)
    client_socket.connect(address)

    def check (password):
        # nonlocal client_socket
        message=password.encode()
        client_socket.send(message)
        response=client_socket.recv(100000)
        response=response.decode()
        if (response=="Connection success!"):
            return True
        else :
            return False
    data = "abcdefghijklmnopqrstuvwxyz0123456789"
    flag=False
    for i in range(1, 36):
        for item in itertools.product(data, repeat=i):
            Pass="".join(item)
            flag=check(Pass)
            if (flag):
                print (Pass)
                break
        if (flag):
            break