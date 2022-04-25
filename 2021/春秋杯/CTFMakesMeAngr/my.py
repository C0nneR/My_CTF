from pwn import p64

# rbp_48 = 0x75475f337840654f
# rbp_40 = 0x5f66337968455f33		# d0
# rbp_32 = 0x7431455f6c244052
# rbp_24 = 0x3f6775
# rbp_12 = 27 	# f4	len
# rbp_8 = 0 		# f8	index

text = b''
text += p64(0x75475f337840654f)
text += p64(0x5f66337968455f33)
text += p64(0x7431455f6c244052)
text += p64(0x3f6775)
text = text[:-5]
print(text)

# rdx = b''
# rdx += p64(0x5f66337968455f33)
# print(rdx)

# rax = b''
# rax += p64(0x7431455f6c244052)
# print(rax)

flag = ''
for char in text:
	if char >= ord('A') and char <= ord('Z'):
		index = (char - ord('A') + 13) % 26
		flag += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[index]
	elif char >= ord('a') and char <= ord('z'):
		index = (char - ord('a') + 13) % 26
		flag += 'abcdefghijklmnopqrstuvwxyz'[index]
	else:
		flag += chr(char)
print(flag)