from pwn import u32

opcode = [0xA1, 0xC1, 0x00, 0xB1, 0x77, 0xC2, 0x4A, 0x01, 0x00, 0x00, 0xC1, 0x01, 0xB2, 0x77, 0xC2, 0x19, 0x01, 0x00, 0x00, 0xC1, 0x02, 0xB4, 0x77, 0xC2, 0xDD, 0x01, 0x00, 0x00, 0xC1, 0x03, 0xB3, 0x77, 0xC2, 0x0F, 0x01, 0x00, 0x00, 0xC1, 0x04, 0xB2, 0x77, 0xC2, 0x1B, 0x01, 0x00, 0x00, 0xC1, 0x05, 0xB4, 0x77, 0xC2, 0x89, 0x01, 0x00, 0x00, 0xC1, 0x06, 0xB1, 0x77, 0xC2, 0x19, 0x01, 0x00, 0x00, 0xC1, 0x07, 0xB3, 0x77, 0xC2, 0x54, 0x01, 0x00, 0x00, 0xC1, 0x08, 0xB1, 0x77, 0xC2, 0x4F, 0x01, 0x00, 0x00, 0xC1, 0x09, 0xB1, 0x77, 0xC2, 0x4E, 0x01, 0x00, 0x00, 0xC1, 0x0A, 0xB3, 0x77, 0xC2, 0x55, 0x01, 0x00, 0x00, 0xC1, 0x0B, 0xB3, 0x77, 0xC2, 0x56, 0x01, 0x00, 0x00, 0xC1, 0x0C, 0xB4, 0x77, 0xC2, 0x8E, 0x00, 0x00, 0x00, 0xC1, 0x0D, 0xB2, 0x77, 0xC2, 0x49, 0x00, 0x00, 0x00, 0xC1, 0x0E, 0xB3, 0x77, 0xC2, 0x0E, 0x01, 0x00, 0x00, 0xC1, 0x0F, 0xB1, 0x77, 0xC2, 0x4B, 0x01, 0x00, 0x00, 0xC1, 0x10, 0xB3, 0x77, 0xC2, 0x06, 0x01, 0x00, 0x00, 0xC1, 0x11, 0xB3, 0x77, 0xC2, 0x54, 0x01, 0x00, 0x00, 0xC1, 0x12, 0xB2, 0x77, 0xC2, 0x1A, 0x00, 0x00, 0x00, 0xC1, 0x13, 0xB1, 0x77, 0xC2, 0x42, 0x01, 0x00, 0x00, 0xC1, 0x14, 0xB3, 0x77, 0xC2, 0x53, 0x01, 0x00, 0x00, 0xC1, 0x15, 0xB1, 0x77, 0xC2, 0x1F, 0x01, 0x00, 0x00, 0xC1, 0x16, 0xB3, 0x77, 0xC2, 0x52, 0x01, 0x00, 0x00, 0xC1, 0x17, 0xB4, 0x77, 0xC2, 0xDB, 0x00, 0x00, 0x00, 0xC1, 0x18, 0xB1, 0x77, 0xC2, 0x19, 0x01, 0x00, 0x00, 0xC1, 0x19, 0xB4, 0x77, 0xC2, 0xD9, 0x00, 0x00, 0x00, 0xC1, 0x1A, 0xB1, 0x77, 0xC2, 0x19, 0x01, 0x00, 0x00, 0xC1, 0x1B, 0xB3, 0x77, 0xC2, 0x55, 0x01, 0x00, 0x00, 0xC1, 0x1C, 0xB2, 0x77, 0xC2, 0x19, 0x00, 0x00, 0x00, 0xC1, 0x1D, 0xB3, 0x77, 0xC2, 0x00, 0x01, 0x00, 0x00, 0xC1, 0x1E, 0xB1, 0x77, 0xC2, 0x4B, 0x01, 0x00, 0x00, 0xC1, 0x1F, 0xB2, 0x77, 0xC2, 0x1E, 0x00, 0x00, 0x00, 0xC1, 0x20, 0x80, 0x02, 0x18, 0x00, 0x00, 0x00, 0x23, 0x10, 0xC1, 0x21, 0x80, 0x02, 0x10, 0x00, 0x00, 0x00, 0x23, 0xF7, 0xC1, 0x22, 0x80, 0x02, 0x08, 0x00, 0x00, 0x00, 0x23, 0xF7, 0xC1, 0x23, 0xF7, 0xFE, 0x80, 0x02, 0x05, 0x00, 0x00, 0x00, 0x22, 0x77, 0x10, 0x80, 0x02, 0x07, 0x00, 0x00, 0x00, 0x23, 0x80, 0x02, 0x23, 0x77, 0xF1, 0x98, 0x31, 0x77, 0x10, 0x80, 0x02, 0x18, 0x00, 0x00, 0x00, 0x23, 0x80, 0x02, 0x20, 0xB9, 0xE4, 0x35, 0x31, 0x77, 0x10, 0x80, 0x02, 0x12, 0x00, 0x00, 0x00, 0x22, 0x77, 0xA0, 0xC1, 0x24, 0x80, 0x02, 0x18, 0x00, 0x00, 0x00, 0x23, 0x10, 0xC1, 0x25, 0x80, 0x02, 0x10, 0x00, 0x00, 0x00, 0x23, 0xF7, 0xC1, 0x26, 0x80, 0x02, 0x08, 0x00, 0x00, 0x00, 0x23, 0xF7, 0xC1, 0x27, 0xF7, 0xFE, 0x32, 0x20, 0x43, 0x33, 0x77, 0x80, 0x02, 0x11, 0x00, 0x00, 0x00, 0x22, 0x35, 0x37, 0x38, 0x77, 0x80, 0x02, 0x0D, 0x00, 0x00, 0x00, 0x23, 0x77, 0x38, 0x39, 0x10, 0x32, 0x20, 0x43, 0x33, 0x77, 0x80, 0x02, 0x11, 0x00, 0x00, 0x00, 0x22, 0x35, 0x37, 0x38, 0x77, 0x80, 0x02, 0x0D, 0x00, 0x00, 0x00, 0x23, 0x77, 0x38, 0x39, 0xC7, 0xC1, 0x28, 0x80, 0x02, 0x18, 0x00, 0x00, 0x00, 0x23, 0x10, 0xC1, 0x29, 0x80, 0x02, 0x10, 0x00, 0x00, 0x00, 0x23, 0xF7, 0xC1, 0x2A, 0x80, 0x02, 0x08, 0x00, 0x00, 0x00, 0x23, 0xF7, 0xC1, 0x2B, 0xF7, 0xFE, 0x32, 0x20, 0x43, 0x33, 0x77, 0x80, 0x02, 0x11, 0x00, 0x00, 0x00, 0x22, 0x35, 0x37, 0x38, 0x77, 0x80, 0x02, 0x0D, 0x00, 0x00, 0x00, 0x23, 0x77, 0x38, 0x39, 0x10, 0x32, 0x20, 0x43, 0x33, 0x77, 0x80, 0x02, 0x11, 0x00, 0x00, 0x00, 0x22, 0x35, 0x37, 0x38, 0x77, 0x80, 0x02, 0x0D, 0x00, 0x00, 0x00, 0x23, 0x77, 0x38, 0x39, 0xC8, 0x99]

dword_804B080 = [0x7b, 0x2f, 0x37, 0xe8]

xor_key = []
xor_result = []

i = 0
while True:
    if opcode[i] == 0x41:
        print('table[1] += table[2]')
        i += 1
    if opcode[i] == 0x42:
        print('table[1] -= table[4]')
        i += 1
    if opcode[i] == 0x43:
        print('table[1] *= table[3]')
        i += 1
    if opcode[i] == 0x37:
        print('table[1] = table[5]')
        i += 1
    if opcode[i] == 0x38:
        print('table[1] ^= table[4]')
        i += 1
    if opcode[i] == 0x39:
        print('table[1] ^= table[5]')
        i += 1
    if opcode[i] == 0x35:
        print('table[5] = table[1]')
        i += 1
    if opcode[i] == 0xf7:
        print('table[9] += table[1]')
        i += 1
    if opcode[i] == 0x44:
        print('table[1] //= table[5]')
        i += 1
    if opcode[i] == 0x80:
        print('table[2] = 0x%x' % u32(bytes(opcode[i + 2: i + 6])))
        i += 6
    if opcode[i] == 0x77:
        print('table[1] ^= table[9]')
        i += 1
    if opcode[i] == 0x53:
        i += 2
    if opcode[i] == 0x22:
        print('table[1] >>= table[2]')
        i += 1
    if opcode[i] == 0x23:
        print('table[1] <<= table[2]')
        i += 1
    if opcode[i] == 0x99:
        break
    if opcode[i] == 0x76:
        print('table[3] = *table[6]')
        print('*table[6] = 0')
        print('table[6] += 4')
        i += 5
    if opcode[i] == 0x54:
        print('v2 = table[3]')
        print('*v2 = getchar()')
        i += 2
    if opcode[i] == 0x30:
        print('table[1] |= table[2]')
        i += 1
    if opcode[i] == 0x31:
        print('table[1] &= table[2]')
        i += 1
    if opcode[i] == 0x32:
        print('table[3] = 0x%x' % opcode[i + 1])
        i += 2
    if opcode[i] == 0x9:
        print('table[1] = 1877735783')
        i += 1
    if opcode[i] == 0x10:
        print('table[9] = table[1]')
        i += 1
    if opcode[i] == 0x33:
        print('table[4] = table[1]')
        i += 1
    if opcode[i] == 0x34:
        print('table[2] = 0x%x' % opcode[i + 1])
        i += 2
    if opcode[i] == 0xfe:
        print('table[1] = table[9]')
        i += 1
    if opcode[i] == 0x11:
        i += 1
    if opcode[i] == 0xa0:
        print('assert table[1] == 1877735783')
        i += 1
    if opcode[i] == 0xa1:
        print('read(0, s, 44)')
        i += 1
    if opcode[i] == 0xb1:
        print('table[9] = 0x%x' % dword_804B080[0])
        xor_key.append(dword_804B080[0])
        i += 1
    if opcode[i] == 0xb2:
        print('table[9] = 0x%x' % dword_804B080[1])
        xor_key.append(dword_804B080[1])
        i += 1
    if opcode[i] == 0xb3:
        print('table[9] = 0x%x' % dword_804B080[2])
        xor_key.append(dword_804B080[2])
        i += 1
    if opcode[i] == 0xb4:
        print('table[9] = 0x%x' % dword_804B080[3])
        xor_key.append(dword_804B080[3])
        i += 1
    if opcode[i] == 0xc1:
        print('table[1] = s[0x%x]' % opcode[i + 1])
        i += 2
    if opcode[i] == 0xc7:
        print('assert 0x%x == table[1]' % 0xCF1304DC)
        i += 1
    if opcode[i] == 0xc8:
        print('assert 0x%x == table[1]' % 0x283B8E84)
        i += 1
    if opcode[i] == 0xc2:
        print('assert 0x%x == table[1]' % opcode[i + 1])
        xor_result.append(opcode[i + 1])
        i += 5

# flag = ''
# for i in range(32):
#     flag += chr(xor_result[i] ^ xor_key[i])

# str_space = 'abcdefghijklmnopqrstuvwxyz0123456789'

# for a in str_space:
#     for b in str_space:
#         for c in str_space:
#             for d in str_space:
#                 table = [0] * 10
#                 table[1] = ord(a)
#                 table[2] = 0x18
#                 table[1] <<= table[2]
#                 table[9] = table[1]
#                 table[1] = ord(b)
#                 table[2] = 0x10
#                 table[1] <<= table[2]
#                 table[9] += table[1]
#                 table[1] = ord(c)
#                 table[2] = 0x8
#                 table[1] <<= table[2]
#                 table[9] += table[1]
#                 table[1] = ord(d)
#                 table[9] += table[1]
#                 table[1] = table[9]
#                 table[2] = 0x5
#                 table[1] >>= table[2]
#                 table[1] ^= table[9]
#                 table[9] = table[1]
#                 table[2] = 0x7
#                 table[1] <<= table[2]
#                 table[2] = 0x98f17723
#                 table[1] &= table[2]
#                 table[1] ^= table[9]
#                 table[9] = table[1]
#                 table[2] = 0x18
#                 table[1] <<= table[2]
#                 table[2] = 0x35e4b920
#                 table[1] &= table[2]
#                 table[1] ^= table[9]
#                 table[9] = table[1]
#                 table[2] = 0x12
#                 table[1] >>= table[2]
#                 table[1] ^= table[9]

#                 if table[1] & 0xffffffff == 1877735783:
#                     print(a, b, c, d)
#                     flag += a
#                     flag += b
#                     flag += c
#                     flag += d
#                     break
#             else:
#                 continue
#             break
#         else:
#             continue
#         break
#     else:
#         continue
#     break

flag = '16584abc45baff901c59dde3b1bb6701a254'

# str_space = 'abcdefghijklmnopqrstuvwxyz0123456789'

# for a in str_space:
#     for b in str_space:
#         for c in str_space:
#             for d in str_space:
#                 table = [0] * 10
#                 table[1] = ord(a)
#                 table[2] = 0x18
#                 table[1] <<= table[2]
#                 table[9] = table[1]
#                 table[1] = ord(b)
#                 table[2] = 0x10
#                 table[1] <<= table[2]
#                 table[9] += table[1]
#                 table[1] = ord(c)
#                 table[2] = 0x8
#                 table[1] <<= table[2]
#                 table[9] += table[1]
#                 table[1] = ord(d)
#                 table[9] += table[1]
#                 table[1] = table[9]
#                 table[3] = 0x20
#                 table[1] = (table[1] * table[3]) & 0xffffffff
#                 table[4] = table[1]
#                 table[1] ^= table[9]
#                 table[2] = 0x11
#                 table[1] >>= table[2]
#                 table[5] = table[1]
#                 table[1] = table[5]
#                 table[1] ^= table[4]
#                 table[1] ^= table[9]
#                 table[2] = 0xd
#                 table[1] = (table[1] << table[2]) & 0xffffffff
#                 table[1] ^= table[9]
#                 table[1] ^= table[4]
#                 table[1] ^= table[5]
#                 table[9] = table[1]
#                 table[3] = 0x20
#                 table[1] = (table[1] * table[3]) & 0xffffffff
#                 table[4] = table[1]
#                 table[1] ^= table[9]
#                 table[2] = 0x11
#                 table[1] >>= table[2]
#                 table[5] = table[1]
#                 table[1] = table[5]
#                 table[1] ^= table[4]
#                 table[1] ^= table[9]
#                 table[2] = 0xd
#                 table[1] = (table[1] << table[2]) & 0xffffffff
#                 table[1] ^= table[9]
#                 table[1] ^= table[4]
#                 table[1] ^= table[5]
#                 if 0xcf1304dc == table[1]:
#                     print(a, b, c, d)
#                     flag += a
#                     flag += b
#                     flag += c
#                     flag += d
#                     break
#             else:
#                 continue
#             break
#         else:
#             continue
#         break
#     else:
#         continue
#     break

flag = '16584abc45baff901c59dde3b1bb6701a254b06c'

str_space = 'abcdefghijklmnopqrstuvwxyz0123456789'

for a in str_space:
    for b in str_space:
        for c in str_space:
            for d in str_space:
                table = [0] * 10
                table[1] = ord(a)
                table[2] = 0x18
                table[1] <<= table[2]
                table[9] = table[1]
                table[1] = ord(b)
                table[2] = 0x10
                table[1] <<= table[2]
                table[9] += table[1]
                table[1] = ord(c)
                table[2] = 0x8
                table[1] <<= table[2]
                table[9] += table[1]
                table[1] = ord(d)
                table[9] += table[1]
                table[1] = table[9]
                table[3] = 0x20
                table[1] = (table[1] * table[3]) & 0xffffffff
                table[4] = table[1]
                table[1] ^= table[9]
                table[2] = 0x11
                table[1] >>= table[2]
                table[5] = table[1]
                table[1] = table[5]
                table[1] ^= table[4]
                table[1] ^= table[9]
                table[2] = 0xd
                table[1] = (table[1] << table[2]) & 0xffffffff
                table[1] ^= table[9]
                table[1] ^= table[4]
                table[1] ^= table[5]
                table[9] = table[1]
                table[3] = 0x20
                table[1] = (table[1] * table[3]) & 0xffffffff
                table[4] = table[1]
                table[1] ^= table[9]
                table[2] = 0x11
                table[1] >>= table[2]
                table[5] = table[1]
                table[1] = table[5]
                table[1] ^= table[4]
                table[1] ^= table[9]
                table[2] = 0xd
                table[1] = (table[1] << table[2]) & 0xffffffff
                table[1] ^= table[9]
                table[1] ^= table[4]
                table[1] ^= table[5]
                if 0x283b8e84 == table[1]:
                    print(a, b, c, d)
                    flag += a
                    flag += b
                    flag += c
                    flag += d
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

print(flag)