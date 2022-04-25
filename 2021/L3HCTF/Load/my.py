flag_num = [-8, 18, -9, 6, -13, 6, -1, 2, -1, 13, -3, -30, 7]

flag = ''
for i in range(13):
	flag += hex((flag_num[i] & 0xff))[2:].rjust(2, '0')
print(flag)