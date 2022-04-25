from pwn import p32

ebp_0x32 = b''
ebp_0x32 += p32(0x656d3174)
ebp_0x32 += p32(0x7530795f)
ebp_0x32 += p32(0x6a6e655f)
ebp_0x32 += p32(0x775f7930)
ebp_0x32 += p32(0x31743561)
ebp_0x32 += p32(0x775f676e)
ebp_0x32 += p32(0x6e5f3561)
ebp_0x32 += p32(0x775f746f)
ebp_0x32 += p32(0x65743561)
ebp_0x32 += p32(0x0064)
plain = ebp_0x32[:-3]

ebp_0x54 = 3
key = ebp_0x54

ebp_0x4c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
box = ebp_0x4c

flag = ''
for num in plain:
	if num + 3 <= ord('Z'):
		flag += chr(num + 3)
	else:
		flag += box[((num + 3 - ord('Z')) % 26) - 1]
print(flag)

