import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

VERSION = 5

def getCheckSum(buff):
    r = 0
    for i in range(len(buff) - 1):
        r = VERSION * (r + ord(buff[i]))
    r = r & 0xff
    return r

HEAD = "RBT"
MSG_TYPE = "GET"
MSG_TYPE = "ACK"
MSG_TYPE = "SET"
SEP = " "
DATA_TYPE = "VEL"
DATA_TYPE = "POS"

def doDecode(buff):
    s = buff.split(SEP)
    if(s[0] == HEAD):
        if(s[1] == "SET"):
            if(s[2] == "POS"):
                print (s[3])



while True:

    data, addr = sock.recvfrom(1024)
    v = getCheckSum(data)

    if(v == ord(data[len(data) - 1])):
        print("valid")
    else:
        print("error")
    #print (data)
    doDecode(data)