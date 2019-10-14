from pwn import *
import struct
target = 0x21dd09ec
part = target / 5
print("{:08x}".format(part))
print("{:08x}".format(target - part*4))

# 得到这5个数后使用python -c '脚本代码' 来执行
#  ./col $(python -c 'print("\xc8\xce\xc5\x06"*4 + "\xcc\xce\xc5\x06")';)