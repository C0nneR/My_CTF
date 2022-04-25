import ctypes
from pwn import p32, u32
from aeskeyschedule import key_schedule
from phoenixAES import MC, InvMC, InvSBox, SBox, InvShiftRow, ShiftRow, AddKey

def tea_encrypt(plain, key):
	y, z = [ctypes.c_uint32(x) for x in plain]

	sum_val = ctypes.c_uint32(0)
	delta = 0x73637466

	for i in range(32):
		sum_val.value += delta
		y.value += ((z.value << 4) + key[0]) ^ (z.value + sum_val.value) ^ ((z.value >> 5) + key[1]) ^ (sum_val.value + i)
		z.value += ((y.value << 4) + key[2]) ^ (y.value + sum_val.value) ^ ((y.value >> 5) + key[3]) ^ (sum_val.value + i)

	return [y.value, z.value]

def tea_decrypt(cipher, key):
	y, z = [ctypes.c_uint32(x) for x in cipher]
	sum_val = ctypes.c_uint32(0x6C6E8CC0)
	delta = 0x73637466

	for i in range(31, -1, -1):
		z.value -= ((y.value << 4) + key[2]) ^ (y.value + sum_val.value) ^ ((y.value >> 5) + key[3]) ^ (sum_val.value + i)
		y.value -= ((z.value << 4) + key[0]) ^ (z.value + sum_val.value) ^ ((z.value >> 5) + key[1]) ^ (sum_val.value + i)
		sum_val.value -= delta

	return [y.value, z.value]

def AES_encrypt(plain, round_keys):
	cipher = plain
	cipher = AddKey(cipher, round_keys[0])
	for i in range(16):
		cipher[i] ^= 0x66

	for j in range(1, 10):
		cipher = InvSBox(cipher)
		cipher = InvShiftRow(cipher)
		cipher = MC(cipher)
		cipher = AddKey(cipher, round_keys[j])

	cipher = SBox(cipher)
	cipher = ShiftRow(cipher)
	cipher = AddKey(cipher, round_keys[10])

	# for num in cipher:
	# 	print(hex(num)[2:], end = ' ')
	# print('')

	return cipher

def AES_decrypt(cipher, round_keys):
	plain = cipher

	plain = AddKey(plain, round_keys[10])
	plain = InvShiftRow(plain)
	plain = InvSBox(plain)

	for j in range(9, 0, -1):
		plain = AddKey(plain, round_keys[j])
		plain = InvMC(plain)
		plain = ShiftRow(plain)
		plain = SBox(plain)
	
	for i in range(16):
		plain[i] ^= 0x66
	plain = AddKey(plain, round_keys[0])

	# for num in plain:
	# 	print(hex(num)[2:], end = ' ')
	# print('')

	return plain

TEA_key = [0] * 4
TEA_key[1] = 0x21667463
TEA_key[0] = 0x735F6F74
TEA_key[3] = 0x5F656D6F
TEA_key[2] = 0x636C6557

cipher = b"\xBE\x1C\xB3\xF3\xA1\xF4\xE4\x63\x11\xE1\x1C\x6B\x54\x0A\xDF\x74\xF2\x93\x55\xDA\x48\xFC\xA2\x3C\x89\x63\x2E\x7F\x8D\xA4\x6D\x4E"

# rand_seed = 0x53435446
rand_vals = [0x6591, 0x10a9, 0x5208, 0x4be2, 0x52a2, 0x16e6, 0x603e, 0x22bc, 
             0x1ce2, 0x5202, 0x4e9c, 0x30ce, 0x3e65, 0x048a, 0x0308, 0x7bb7, 
             0x405f, 0x04ba, 0x6566, 0x4c1d, 0x07f1, 0x25f8, 0x330b, 0x034d, 
             0x6543, 0x5ba1, 0x2675, 0x7421, 0x18d3, 0x7908, 0x4739, 0x4327]

delta = [0x66, 0x74, 0x63, 0x73][::-1]
# TEA_cipher = []
# temp_plain = [0x61616161, 0x62626262]
# TEA_cipher += tea_encrypt(temp_plain, TEA_key)
# temp_plain = [0x63636363, 0x64646464]
# TEA_cipher += tea_encrypt(temp_plain, TEA_key)

# dummy input: aaaabbbbccccddddeeeeeeeeeeeeeeee

# dst = b''
# for i in range(4):
# 	dst += p32(TEA_cipher[i] ^ delta[i])
# f3271cc23e74d3b8e358c213820795f7

AES_key = b'Welcome_to_sctf!'
round_keys = key_schedule(AES_key)
assert AES_key == round_keys[0]

#  0: 57656c636f6d655f746f5f7363746621
#  1: c4569198ab3bf4c7df54abb4bc20cd95
#  2: 71ebbbfddad04f3a0584e48eb9a4291b
#  3: 3c4e14abe69e5b91e31abf1f5abe9604
#  4: 9adee6157c40bd849f5a029bc5e4949f
#  5: e3fc3db39fbc803700e682acc5021633
#  6: b4bbfe152b077e222be1fc8eeee3eabd
#  7: e53c843dce3bfa1fe5da06910b39ec2c
#  8: 77f2f516b9c90f095c130998572ae5b4
#  9: 892b784d30e277446cf17edc3bdb9b68
# 10: 063f3daf36dd4aeb5a2c343761f7af5f

# AES_cipher = AES_encrypt(dst, round_keys)

flag = b''
for i in range(2):
	AES_cipher = cipher[i * 16: i * 16 + 16]
	AES_plain = AES_decrypt(AES_cipher, round_keys)
	for i in range(4):
		AES_plain[i * 4] ^= delta[i]
	TEA_cipher = AES_plain
	TEA_plain = [] 
	TEA_plain += tea_decrypt([u32(TEA_cipher[0:4]), u32(TEA_cipher[4:8])], TEA_key)
	TEA_plain += tea_decrypt([u32(TEA_cipher[8:12]), u32(TEA_cipher[12:16])], TEA_key)
	for num in TEA_plain:
		flag += p32(num)
print(flag)

# SCTF{5277cc2af8f1155f7a61030f46fdf9df}