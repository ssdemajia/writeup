from pwn import *

rand = 1804289383
deadbeef = 0xdeadbeef
key = rand^deadbeef
conn = process('./random')
conn.send(str(key)+'\n')
conn.interactive()