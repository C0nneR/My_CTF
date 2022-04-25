import ctypes
from pwn import p32

# def xtea_decrypt(cipher, key, round):
# 	y, z = [ctypes.c_uint32(x) for x in cipher]

# 	delta = 0x9e3779b9
# 	sum_val = ctypes.c_uint32(0)
# 	sum_val.value = delta * round

# 	for i in range(round):
# 		z.value -= (((y.value << 4) ^ (y.value >> 5)) + y.value) ^ (sum_val.value + key[(sum_val.value >> 11) & 3])
# 		sum_val.value -= delta
# 		y.value -= (((z.value << 4) ^ (z.value >> 5)) + z.value) ^ (sum_val.value + key[sum_val.value & 3])

# 	return [y.value, z.value]

# key = [5, 6, 7, 8]
# cipher = [0x22A7549D, 0x89A45DBC, 0x3D663601, 0xA4E2927B, 0xAEAA8768, 0x9EFDC786, 0xEFC4FF92, 0x592B52B8, 0xBE6C5C7D, 0x6FC71050, 0xA8A1801A, 0x22662EFD]

# flag = b''
# for i in range(len(cipher) // 2):
# 	temp_cipher = cipher[i * 2:i * 2 + 2]
# 	plain = xtea_decrypt(temp_cipher, key, 32)
# 	flag += p32(plain[0])
# 	flag += p32(plain[1])
# print(flag)
# flag{0ff_c0ur53_th15_1s_f4k3_but_y0ur_ar3_clO53}

key = [1, 2, 3, 4]
cipher = [0x12F61C9D, 0xE918076D, 0x9911F885, 0x956EDA21, 0xB61F7487, 0x6257145B, 0x951FEE6F, 0x7D32C2AF, 0x5E4EC89, 0xD9176C8A, 0xB4DF2B97]

delta = 0x9e3779b9
sum_val = ctypes.c_uint32(0)
sum_val.value = delta * 10

for _ in range(10):
	idx = 10
	v17 = (sum_val.value >> 2) & 3
	for i in range(idx, -1, -1):
		cur = ctypes.c_uint32(cipher[i])
		_next = ctypes.c_uint32(cipher[(i + 1) % 11])
		_prev = ctypes.c_uint32(cipher[(i - 1) % 11])
		cur.value -= ((sum_val.value ^ _next.value) + (key[v17 ^ i & 3] ^ _prev.value)) ^ (((16 * _prev.value) ^ (_next.value >> 3)) + ((_prev.value >> 5) ^ (4 * _next.value)))
		cipher[i] = cur.value

	sum_val.value -= delta

def ror(value, count, max_bits):
	right = (value & (2**max_bits - 1)) >> (count % max_bits)
	left =  (value << (max_bits - (count % max_bits))) & (2**max_bits - 1)
	return left | right

flag = b''
for i in cipher:
	temp = ror(i, 7, 32)
	flag += p32(temp)
print(flag)
# _flag{96f369d8-df39-4929-9e39-eac73839c643}_