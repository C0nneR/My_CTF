ciher = [0x00000005, 0x0000008F, 0x0000009E, 0x00000079, 0x0000002A, 0x000000C0, 0x00000068, 0x00000081, 0x0000002D, 0x000000FC, 0x000000CF, 0x000000A4, 0x000000B5, 0x00000055, 0x0000005F, 0x000000E4, 0x0000009D, 0x00000023, 0x000000D6, 0x0000001D, 0x000000F1, 0x000000E7, 0x00000097, 0x00000091, 0x00000006, 0x00000024, 0x00000042, 0x00000071, 0x0000003C, 0x00000058, 0x0000005C, 0x00000030, 0x00000019, 0x000000C6, 0x000000F5, 0x000000BC, 0x0000004B, 0x00000042, 0x0000005D, 0x000000DA, 0x00000058, 0x0000009B, 0x00000024, 0x00000040]
key = [0x00000056, 0x000000DA, 0x000000CD, 0x0000003A, 0x0000007E, 0x00000086, 0x00000013, 0x000000B5, 0x0000001D, 0x0000009D, 0x000000FC, 0x00000097, 0x0000008C, 0x00000031, 0x0000006B, 0x000000C9, 0x000000FB, 0x0000001A, 0x000000E2, 0x0000002D, 0x000000DC, 0x000000D3, 0x000000F1, 0x000000F4, 0x00000036, 0x00000009, 0x00000020, 0x00000042, 0x00000004, 0x0000006A, 0x00000071, 0x00000053, 0x00000078, 0x000000A4, 0x00000097, 0x0000008F, 0x0000007A, 0x00000072, 0x00000039, 0x000000E8, 0x0000003D, 0x000000FA, 0x00000040, 0x0000003D, 0x00000198, 0x00000000, 0x00000000, 0x00000000]

flag = ''
for i in range(44):
	flag += chr(ciher[i] ^ key[i])
print(flag)