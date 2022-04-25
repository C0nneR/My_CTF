# shuffled_data_dict = {0xf9: '6VNjKDn', 0xfa: '6371240IVxYcx',
#                       0xfb: 'matchAll', 0xfc: '4948280PfzqUs',
#                       0xfd: '42cXdJpF', 0xfe: 'flag_input',
#                       0xff: 'length', 0x100: '1829548EQHzrX',
#                       0x101: 'push', 0x102: 'failed!',
#                       0x103: 'addListener', 0x104: 'next',
#                       0x105: 'getElementById', 0x106: '4787853SBLwXC',
#                       0x107: 'value', 0x108: 'success!',
#                       0x109: 'match', 0x10a: 'filter',
#                       0x10b: '152223ILKqKk', 0x10c: 'reload',
#                       0x10d: '([0-9a-f]{4,12})', 0x10e: '7454488gQLWNt',
#                       0x10f: '3771630sdrcXm', 0x110: 'location', 0x111: 'log'}

import ctypes
from pwn import p32

def rshift(val, n):
    if val >= 0:
        return val >> n
    else:
        return (val + 0x100000000) >> n

def tea_decrypt(cipher, key):
    y, z = [ctypes.c_int32(x) for x in cipher]
    sum_val = ctypes.c_int32(34)
    delta = 1

    for _ in range(34):
        z.value -= ((y.value * 16) + key[2]) ^ (y.value + sum_val.value) ^ ((rshift(y.value, 5)) + key[3])
        y.value -= ((z.value * 16) + key[0]) ^ (z.value + sum_val.value) ^ ((rshift(z.value, 5)) + key[1])
        sum_val.value -= delta

    return [y.value, z.value]

def tea_encrypt(cipher, key):
    y, z = [ctypes.c_int32(x) for x in cipher]
    sum_val = ctypes.c_int32(0)
    delta = 1

    for _ in range(34):
        sum_val.value += delta
        y.value += ((z.value * 16) + key[0]) ^ (z.value + sum_val.value) ^ ((rshift(z.value, 5)) + key[1])
        z.value += ((y.value * 16) + key[2]) ^ (y.value + sum_val.value) ^ ((rshift(y.value, 5)) + key[3])

    return [y.value, z.value]

final_cipher = [-0x3dec3227, 0x79f40242, 0x325d0365, 0x6561df78, 0x5747f7c8, -0x26c12bcb]

for i in range(5, -1, -1):
    temp_cipher = [final_cipher[i], final_cipher[(i + 1) % 6]]
    temp_key = [final_cipher[(i + 2) % 6],
                final_cipher[(i + 3) % 6],
                final_cipher[(i + 4) % 6],
                final_cipher[(i + 5) % 6]]

    result = tea_decrypt(temp_cipher, temp_key)
    final_cipher[i] = result[0]
    final_cipher[(i + 1) % 6] = result[1]

flag = 'flag{'
flag += hex(ctypes.c_uint(final_cipher[0]).value)[2:].rjust(8, '0')
flag += '-'
flag += hex(ctypes.c_uint(final_cipher[1]).value)[2:].rjust(4, '0')
flag += '-'
flag += hex(ctypes.c_uint(final_cipher[2]).value)[2:].rjust(4, '0')
flag += '-'
flag += hex(ctypes.c_uint(final_cipher[3]).value)[2:].rjust(4, '0')
flag += '-'
flag += hex(ctypes.c_uint(final_cipher[4]).value)[2:].rjust(12, '0')
flag += '}'
print(flag)
assert hex(ctypes.c_uint(final_cipher[5]).value)[2:] == 'deadbeef'

# flag{847213d0-57a8-4411-b0f8-00000c036474}