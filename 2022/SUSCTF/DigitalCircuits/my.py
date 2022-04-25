import ctypes
from pwn import p32

def tea_decrypt(cipher, key):
	y, z = [ctypes.c_uint32(x) for x in cipher]
	sum_val = ctypes.c_uint32(0xC6EF3720)
	delta = 0x9e3779b9

	for _ in range(32):
		z.value -= ((y.value << 4) + key[2]) ^ (y.value + sum_val.value) ^ ((y.value >> 5) + key[3])
		y.value -= ((z.value << 4) + key[0]) ^ (z.value + sum_val.value) ^ ((z.value >> 5) + key[1])
		sum_val.value -= delta

	return [y.value, z.value]

res = '001111101000100101000111110010111100110010010100010001100011100100110001001101011000001110001000001110110000101101101000100100111101101001100010011100110110000100111011001011100110010000100111'
cipher = []
for i in range(len(res) // 32):
    cipher.append(int(res[i * 32:i * 32 + 32],2 ))

k0 = '0100010001000101'.zfill(32)
k1 = '0100000101000100'.zfill(32)
k2 = '0100001001000101'.zfill(32)
k3 = '0100010101000110'.zfill(32)
key = [int(k0, 2), int(k1, 2), int(k2, 2), int(k3, 2)]

flag = b''
for i in range(3):
    ret = tea_decrypt(cipher[i * 2:i * 2 + 2], key)
    flag += p32(ret[0])[::-1]
    flag += p32(ret[1])[::-1]
print('SUSCTF{%s}' % flag.decode())