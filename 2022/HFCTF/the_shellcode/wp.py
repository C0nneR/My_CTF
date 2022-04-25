import base64
from pwn import p32

def ror(value, count, max_bits):
	right = (value & (2**max_bits - 1)) >> (count % max_bits)
	left =  (value << (max_bits - (count % max_bits))) & (2**max_bits - 1)
	return left | right

xxtea_decrypted = [0x6243e703, 0x993831bb, 0x925c2396, 0x60925c81, 0x5ca0925c, 0xbd784193, 0xff993152, 0xe1650699, 0x6110e30b, 0x687e0e01, 0x8717c718, 0x925cba92, 0xe1125c80, 0x25c1618, 0x78062cc3, 0xf524, 0x82161800, 0x5cc0425c, 0xd61801c2, 0x7800cf1c, 0x4d24, 0xa15c4a00, 0x9997185c, 0x650699ff, 0x18687e0e, 0xab26d1c7, 0x21e318a7, 0x21e3d920, 0x99ceab60, 0x1c4e99ff, 0xb5788216, 0x7e0e5020, 0xac71868, 0xab70cf1c, 0x687e0e8f, 0x99ff99ba, 0x21a25c4e, 0xb57892e1, 0x3bc570e0, 0xbf333333, 0x5cd78e5f, 0xf8470e16, 0x206c1618, 0xd2c65904, 0x5020b578, 0x7e0e1e59, 0xac71868, 0xab70cf1c, 0x687e0ea6, 0xa321e1d9, 0x9b2943b0, 0x265c0000, 0x7b7343, 0x5c82a200, 0xff4221e2, 0x43a05f9e, 0x9b29, 0xcb43265c, 0xa2009b2b, 0x21e25c82, 0xc29eff42, 0xc2c2c2c2, 0xc2c2c2c2, 0xfac21e0b, 0x4f905cd2, 0xffffff58]
plain = b''
for i in range(66):
	plain += p32(xxtea_decrypted[i]).rjust(4, b'\x00')
plain = list(plain)
for i in range(66 * 4):
	plain[i] = ror(plain[i], 3, 8)
plain = bytearray(plain)
print(base64.b64encode(plain))

key = b'LoadLibraryExA'
plain = b'is program can'
cipher = ''
for i in range(14):
    cipher += chr(plain[i] + (key[i] % 5))
print(cipher)