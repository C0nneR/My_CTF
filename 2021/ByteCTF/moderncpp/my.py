# bytectf{abcdefghijklmnopqrstuvwxyz123456}

import ctypes
from pwn import p32

cipher = [0xC5D3669F, 0xB917171A, 0xB4B37B19, 0x0AE80C5F, 0x8D80307F, 0x21522880, 0x34D80589, 0xDE6C83D1, 0x59B73618, 0xC6E65D35]
tea_key = [0x62797465, 0x2d637466, 0x77656c63, 0x6f6d657e]

def tea_decrypt(cipher, key):
	y, z = [ctypes.c_uint32(x) for x in cipher]
	sum_val = ctypes.c_uint32(0xC6EF3720)
	delta = 0x9e3779b9

	for _ in range(32):
		z.value -= ((y.value << 4) + key[2]) ^ (y.value + sum_val.value) ^ ((y.value >> 5) + key[3])
		y.value -= ((z.value << 4) + key[0]) ^ (z.value + sum_val.value) ^ ((z.value >> 5) + key[1])
		sum_val.value -= delta

	return [y.value, z.value]

plain = []
for i in range(5):
    cipher_part = cipher[i * 2: i * 2 + 2]
    plain += tea_decrypt(cipher_part, tea_key)

plain_bytes = b''
for num in plain:
    plain_bytes += p32(num)

ans = list(plain_bytes)[:-7]
print([hex(num) for num in ans])

table = {'!': '00110110', '#': '101001', '%': '00010', '&': '10100011100', '(': '010011', ')': '111100', '*': '0110010', '+': '10111', '-': '10100010', ';': '1010000', '=': '000000', '@': '1110011', '[': '110011', ']': '00100', '^': '01111', '_': '01010', '{': '10001', '}': '1010001111', 'a': '100101', 'b': '00001', 'c': '01110', 'd': '11011', 'e': '0011010', 'f': '010010', 'g': '111011', 'h': '01000', 'i': '10110', 'j': '00110111', 'k': '1111010', 'l': '110010', 'm': '00011', 'n': '10000', 'o': '10100011101', 'p': '0110011', 'q': '011000', 'r': '111110', 's': '01011', 't': '11000', 'u': '11110110', 'v': '000001', 'w': '111000', 'x': '00101', 'y': '10011', 'z': '101000110', '1': '100100', '2': '111111', '3': '01101', '4': '11010', '5': '11110111', '6': '001100', '7': '111010', '8': '00111', '9': '10101', '0': '1110010'}
flag = ""

ans = ''.join([bin(x)[2:].zfill(8) for x in ans])
while ans != '000':
    for i, j in table.items():
        if ans.startswith(j):
            flag += i
            ans = ans[len(j):]
print(flag)