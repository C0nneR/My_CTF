target_hash = b"\xBF\x0B\x0F\xA2\xA5\x94\x0E\xD7\xCB\x85"

thing = b"\xA3\xD7\x09\x83\xF8\x48\xF6\xF4\xB3\x21\x15\x78\x99\xB1\xAF\xF9\xE7\x2D\x4D\x8A\xCE\x4C\xCA\x2E\x52\x95\xD9\x1E\x4E\x38\x44\x28\x0A\xDF\x02\xA0\x17\xF1\x60\x68\x12\xB7\x7A\xC3\xE9\xFA\x3D\x53\x96\x84\x6B\xBA\xF2\x63\x9A\x19\x7C\xAE\xE5\xF5\xF7\x16\x6A\xA2\x39\xB6\x7B\x0F\xC1\x93\x81\x1B\xEE\xB4\x1A\xEA\xD0\x91\x2F\xB8\x55\xB9\xDA\x85\x3F\x41\xBF\xE0\x5A\x58\x80\x5F\x66\x0B\xD8\x90\x35\xD5\xC0\xA7\x33\x06\x65\x69\x45\x00\x94\x56\x6D\x98\x9B\x76\x97\xFC\xB2\xC2\xB0\xFE\xDB\x20\xE1\xEB\xD6\xE4\xDD\x47\x4A\x1D\x42\xED\x9E\x6E\x49\x3C\xCD\x43\x27\xD2\x07\xD4\xDE\xC7\x67\x18\x89\xCB\x30\x1F\x8D\xC6\x8F\xAA\xC8\x74\xDC\xC9\x5D\x5C\x31\xA4\x70\x88\x61\x2C\x9F\x0D\x2B\x87\x50\x82\x54\x64\x26\x7D\x03\x40\x34\x4B\x1C\x73\xD1\xC4\xFD\x3B\xCC\xFB\x7F\xAB\xE6\x3E\x5B\xA5\xAD\x04\x23\x9C\x14\x51\x22\xF0\x29\x79\x71\x7E\xFF\x8C\x0E\xE2\x0C\xEF\xBC\x72\x75\x6F\x37\xA1\xEC\xD3\x8E\x62\x8B\x86\x10\xE8\x08\x77\x11\xBE\x92\x4F\x24\xC5\x32\x36\x9D\xCF\xF3\xA6\xBB\xAC\x5E\x6C\xA9\x13\x57\x25\xB5\xE3\xBD\xA8\x3A\x01\x05\x59\x2A\x46"

def find_license():
	out = []

	for t in target_hash:
		for v in range(255):
			if thing[v ^ 119] == t:
				out.append(v)
				break

	license = "BEAN-{:02x}{:02x}-{:02x}{:02x}{:02x}{:02x}{:02x}-{:02x}{:02x}{:02x}".format(
				out[1], out[0], out[6], out[5], out[4], out[3], out[2], out[9], out[8], out[7])

	return out, license

out, license = find_license()

MAP = []
for i in range(10):
	MAP.append([])
	for j in range(256):
		MAP[i].append(thing[out[i] ^ j])

cipher = b"\x46\x9D\xFA\x32\x51\xE2\x65\xF4\x80\xC6\xBE\xB3\xC6\x6E\x7E\x3C\x65\xC1\x35\xE0\x11\x19\x0D\x86\x2E\x93\xFE\xEA\xD6\x67\xD7\xB1\xCD\xEC\x52\xE4\x53\x3E\x3B\xE1\x0A\xFD\x50\x7E\xB4\xF8\xD0\x43"

seed = (MAP[8][10] << 16) + (MAP[5][14] << 8) + (MAP[1][14]) + (MAP[9][31] << 24)
# print(seed)
rand = [444242706, 339433174, 1053149467, 1523027287, 1117968178, 2092997650, 816324422, 1095556438, 747709558, 301071833, 598496766, 1810696988, 953767466, 1765134604, 2028312134, 1171168959, 1961149144, 425175821, 1299180724, 1105033260, 282672453, 169003868, 412382634, 162192383, 492960224, 560096927, 1172437624, 128594585, 441632769, 1993060813, 966622640, 885875475]
for i in range(32):
	rand[i] &= 0xffff

def z(enc, a2, a3, rand_pos):
	v3 = enc[a3]
	v4 = rand[rand_pos] ^ v3
	enc[a2] = enc[a2] ^ v4
	return enc

def g(enc, a2, a3, a4, a5, a6):
	final = enc[a2]

	temp3 = 0
	for i in range(0xffff):
		if final == i ^ MAP[a3][i >> 8]:
			temp3 = i
			break

	temp2 = 0
	for i in range(0xffff):
		if temp3 == i ^ (MAP[a4][i & 0xff] << 8):
			temp2 = i
			break

	temp1 = 0
	for i in range(0xffff):
		if temp2 == i ^ MAP[a5][i >> 8]:
			temp1 = i
			break

	original = 0
	for i in range(0xffff):
		if temp1 == i ^ (MAP[a6][i & 0xff] << 8):
			original = i
			break

	enc[a2] = original
	return enc

def g0(enc, num):
	return g(enc, num, 0, 1, 2, 3)

def g1(enc, num):
	return g(enc, num, 4, 5, 6, 7)

def g2(enc, num):
	return g(enc, num, 8, 9, 0, 1)

def g3(enc, num):
	return g(enc, num, 2, 3, 4, 5)

def g4(enc, num):
	return g(enc, num, 6, 7, 8, 9)

def get_enc_from_cipher(cipher):
	enc = []
	for i in range(4):
		enc.append((cipher[i * 2] << 8) | cipher[i * 2 + 1])
	return enc

def get_plain_from_enc(enc):
	plain = []
	for i in range(4):
		plain.append((enc[i] >> 8) & 0xff)
		plain.append(enc[i] & 0xff)
	return plain

flag = ''
for i in range(6):
	enc = get_enc_from_cipher(cipher[i * 8: i * 8 + 8])

	enc = g1(enc, 0)
	enc = z(enc, 1, 0, 31)
	enc = g0(enc, 1)
	enc = z(enc, 2, 1, 30)
	enc = g4(enc, 2)
	enc = z(enc, 3, 2, 29)
	enc = g3(enc, 3)
	enc = z(enc, 0, 3, 28)
	enc = g2(enc, 0)
	enc = z(enc, 1, 0, 27)
	enc = g1(enc, 1)
	enc = z(enc, 2, 1, 26)
	enc = g0(enc, 2)
	enc = z(enc, 3, 2, 25)
	enc = g4(enc, 3)
	enc = z(enc, 0, 3, 24)
	enc = z(enc, 3, 0, 23)
	enc = g3(enc, 0)
	enc = z(enc, 0, 1, 22)
	enc = g2(enc, 1)
	enc = z(enc, 1, 2, 21)
	enc = g1(enc, 2)
	enc = z(enc, 2, 3, 20)
	enc = g0(enc, 3)
	enc = z(enc, 3, 0, 19)
	enc = g4(enc, 0)
	enc = z(enc, 0, 1, 18)
	enc = g3(enc, 1)
	enc = z(enc, 1, 2, 17)
	enc = g2(enc, 2)
	enc = z(enc, 2, 3, 16)
	enc = g1(enc, 3)
	enc = g0(enc, 0)
	enc = z(enc, 1, 0, 15)
	enc = g4(enc, 1)
	enc = z(enc, 2, 1, 14)
	enc = g3(enc, 2)
	enc = z(enc, 3, 2, 13)
	enc = g2(enc, 3)
	enc = z(enc, 0, 3, 12)
	enc = g1(enc, 0)
	enc = z(enc, 1, 0, 11)
	enc = g0(enc, 1)
	enc = z(enc, 2, 1, 10)
	enc = g4(enc, 2)
	enc = z(enc, 3, 2, 9)
	enc = g3(enc, 3)
	enc = z(enc, 0, 3, 8)
	enc = z(enc, 3, 0, 7)
	enc = g2(enc, 0)
	enc = z(enc, 0, 1, 6)
	enc = g1(enc, 1)
	enc = z(enc, 1, 2, 5)
	enc = g0(enc, 2)
	enc = z(enc, 2, 3, 4)
	enc = g4(enc, 3)
	enc = z(enc, 3, 0, 3)
	enc = g3(enc, 0)
	enc = z(enc, 0, 1, 2)
	enc = g2(enc, 1)
	enc = z(enc, 1, 2, 1)
	enc = g1(enc, 2)
	enc = z(enc, 2, 3, 0)
	enc = g0(enc, 3)

	plain = get_plain_from_enc(enc)
	for i in plain:
		flag += chr(i)

print(flag)