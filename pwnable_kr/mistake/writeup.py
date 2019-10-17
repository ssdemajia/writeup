from pwn import *
p = process('mistake')
pass1 = '1234567890'
p.send(pass1)
pass2 = ''.join(chr(ord(i)^1) for i in pass1)
p.send(pass2)
p.interactive()