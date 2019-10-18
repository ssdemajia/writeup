from pwn import *
con =remote("pwnable.kr", 9007)
print(con.read())
line = con.read()
print(line)
N, C = [int(i.strip().split('=')[1]) for i in line.split(' ')]
for i in range(C):
    con.send(str(N))
    print(con.readline())
