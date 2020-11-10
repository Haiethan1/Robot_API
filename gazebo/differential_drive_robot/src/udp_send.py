import socket
import time as t


UDP_IP = '127.0.0.1'
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



while True:
    val = raw_input("Input val: ")
    dir = raw_input("right or left:")
    buff = val + " " + dir

    sock.sendto(buff, (UDP_IP, UDP_PORT))
    t.sleep(0.5)
