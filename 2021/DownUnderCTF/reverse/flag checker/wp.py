from z3 import *

# original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# shuffled = 'XQTM5YRWNSZ4JCLE70DIFK16VO92HAPU38BG'

# shuffle_index = []
# for char in shuffled:
# 	shuffle_index.append(original.find(char))
# print(shuffle_index)

def unshuffle(shuffled):
	shuffle_index = [23, 16, 19, 12, 31, 24, 17, 22, 13, 18, 25, 30, 9, 2, 11, 4, 33, 26, 3, 8, 5, 10, 27, 32, 21, 14, 35, 28, 7, 0, 15, 20, 29, 34, 1, 6]
	ret = [0] * 36
	for i in range(36):
		ret[shuffle_index[i]] = shuffled[i]
	return bytearray(ret)

# print(unshuffle('XQTM5YRWNSZ4JCLE70DIFK16VO92HAPU38BG'))

def char_transform(char):
	return ((2 * char) & 0xff) ^ (27 * (char >> 7))

def reverse_num_combine(inp, nums):
	n = [BitVec(f"n{i}", 9) for i in range(6)]
	s = Solver()

	s.add(inp[nums[0]] == n[2] ^ n[0] ^ char_transform(n[0]) ^ char_transform(n[2]) ^ char_transform(n[4]))
	s.add(inp[nums[1]] == char_transform(n[5]) ^ char_transform(n[3]) ^ n[3] ^ n[1] ^ char_transform(n[1]))
	s.add(inp[nums[2]] == char_transform(n[0]) ^ n[4])
	s.add(inp[nums[3]] == char_transform(n[1]) ^ n[5])
	s.add(inp[nums[4]] == char_transform(n[2]) ^ char_transform(n[0]) ^ n[0])
	s.add(inp[nums[5]] == char_transform(n[3]) ^ char_transform(n[1]) ^ n[1])

	if s.check() == sat:
		m = s.model()
		final_nums = [int(str(m[e])) for e in n]

		for i in range(6):
			inp[nums[i]] = final_nums[i]
		return inp

def reverse_combine(inp):
	nums = [
	[0, 1, 2, 6, 12, 18],
	[3, 4, 5, 11, 17, 23],
	[7, 8, 9, 13, 14, 15],
	[10, 16, 22, 28, 29, 35],
	[19, 20, 24, 25, 26, 30],
	[21, 27, 31, 32, 33, 34]
	]

	for n in nums[::-1]:
		inp = reverse_num_combine(inp, n)
	return inp

target = bytes.fromhex("0f4f733c41c6a4afb441d665c899aab36c99613c4edd704615663c1b7f16a66f2313126e")
for _ in range(16):
	target = unshuffle(target)
	target = reverse_combine(target)
print(target)