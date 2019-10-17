from pwn import *

conn = remote('localhost', 9999)
conn.send('\xde\xad\xbe\xef')