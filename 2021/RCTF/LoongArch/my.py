from pwn import u64

fr = open('output', 'rb')
data = fr.read()
fr.close()

_32 = u64(data[0:8])
_40 = u64(data[8:16])
_48 = u64(data[16:24])
_56 = u64(data[24:32])
_64 = u64(data[32:40])
_72 = u64(data[40:48])
_80 = u64(data[48:56])
_88 = u64(data[56:64])

t4 = _64 ^ 0xffffffffffffffff
t5 = _72 ^ 0xffffffffffffffff
t6 = _80 ^ 0xffffffffffffffff
t7 = _88 ^ 0xffffffffffffffff

def bitrev_8b(num):
	original = bin(num)[2:].rjust(64, '0')
	ret = ''
	for i in range(8):
		ret += original[i * 8:i * 8 + 8][::-1]
	return ret

t0 = bitrev_8b(t4)
t1 = bitrev_8b(t5)
t2 = bitrev_8b(t6)
t3 = bitrev_8b(t7)

t4 = t1[40:64] + t2[0:40]
t5 = t2[40:64] + t0[0:40]
t6 = t0[40:64] + t3[0:40]
t7 = t3[40:64] + t1[0:40]

t0 = int(t4[::-1], 2)
t1 = int(t5[::-1], 2)
t2 = int(t6[::-1], 2)
t3 = int(t7[::-1], 2)

t0 = t0 ^ _32
t1 = t1 ^ _40
t2 = t2 ^ _48
t3 = t3 ^ _56

flag = b''
import binascii

flag += binascii.a2b_hex(hex(t0)[2:])[::-1]
flag += binascii.a2b_hex(hex(t1)[2:])[::-1]
flag += binascii.a2b_hex(hex(t2)[2:])[::-1]
flag += binascii.a2b_hex(hex(t3)[2:])[::-1]

print(flag)

# RCTF{We1c0m3_t0_RCTF_2o21_@&-=+}