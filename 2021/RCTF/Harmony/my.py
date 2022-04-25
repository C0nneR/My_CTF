from pwn import p32

plain = b''
plain += p32(0x4d524148)
plain += p32(0x44594e4f)
plain += p32(0x4d414552)
plain += p32(0x4f505449)
plain += p32(0x42495353)
plain += p32(0x454c)
plain = plain[:-2]

plain = list(plain)

for i in range(len(plain)):
	temp = plain[i]
	if temp + 3 < 0x5b:
		plain[i] = temp + 3
	else:
		plain[i] = temp + 3 - 0x1a

cipher = [chr(i) for i in plain]
print(''.join(cipher))