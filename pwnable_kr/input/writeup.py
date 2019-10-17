from pwn import *
import sys
inp = [str(i) for i in range(99)] # stage 1
inp[ord('A')-1] = '\x00'
inp[ord('B')-1] = '\x20\x0a\x0d\x00'
inp[ord('C')-1] = '9999' # stage 5
print(' '.join(inp))
fp = open('\x0a', 'wa')
fp.write('\x00\x00\x00\x00\x00') # stage 4
fp.close()

inp = ['./input'] + inp
conn = process(inp, env={'\xde\xad\xbe\xef': '\xca\xfe\xba\xbe'}) # stage 3
conn.write('\x00\x0a\x00\xff') # stage 2
conn.stderr.write('\x00\x0a\x02\xff') # stage 3

conn.interactive()