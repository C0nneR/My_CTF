from pwn import u32

fake_opcode = [
    0xF5, 
    0xF1, 0xE1, 0x00, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x20, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x01, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x21, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x02, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x22, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x03, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x23, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x04, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x24, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x05, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x25, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x06, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x26, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x07, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x27, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x08, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x28, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x09, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x29, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x0A, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x2A, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x0B, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x2B, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x0C, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x2C, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x0D, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x2D, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x0E, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x2E, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x0F, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x2F, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x10, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x30, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x11, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x31, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x12, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x32, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x13, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x33, 0x00, 0x00, 0x00, 
    0xF4]

real_opcode = [
    0xF5, 
    0xF1, 0xE1, 0x00, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x01, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x00, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x01, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x02, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x01, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x02, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x03, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x02, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x03, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x04, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x03, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x04, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x05, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x04, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x05, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x06, 0x00, 0x00, 0x00, 
    0xF2, 
    0xF1, 0xE4, 0x05, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x06, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x07, 0x00, 0x00, 0x00, 
    0xF1, 0xE3, 0x08, 0x00, 0x00, 0x00, 
    0xF1, 0xE5, 0x0C, 0x00, 0x00, 0x00, 
    0xF6, 
    0xF7, 
    0xF1, 0xE4, 0x06, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x07, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x08, 0x00, 0x00, 0x00, 
    0xF1, 0xE3, 0x09, 0x00, 0x00, 0x00, 
    0xF1, 0xE5, 0x0C, 0x00, 0x00, 0x00, 
    0xF6, 
    0xF7, 
    0xF1, 0xE4, 0x07, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x08, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x09, 0x00, 0x00, 0x00, 
    0xF1, 0xE3, 0x0A, 0x00, 0x00, 0x00, 
    0xF1, 0xE5, 0x0C, 0x00, 0x00, 0x00, 
    0xF6, 
    0xF7, 
    0xF1, 0xE4, 0x08, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x0D, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x13, 0x00, 0x00, 0x00, 
    0xF8, 
    0xF1, 0xE4, 0x0D, 0x00, 0x00, 0x00, 
    0xF1, 0xE7, 0x13, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x0E, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x12, 0x00, 0x00, 0x00, 
    0xF8, 
    0xF1, 0xE4, 0x0E, 0x00, 0x00, 0x00, 
    0xF1, 0xE7, 0x12, 0x00, 0x00, 0x00, 
    0xF1, 0xE1, 0x0F, 0x00, 0x00, 0x00, 
    0xF1, 0xE2, 0x11, 0x00, 0x00, 0x00, 
    0xF8, 
    0xF1, 0xE4, 0x0F, 0x00, 0x00, 0x00, 
    0xF1, 0xE7, 0x11, 0x00, 0x00, 0x00, 
    0xF4]

pos = 0
while real_opcode[pos] != 0xF4:
    if real_opcode[pos] == 0xF5:
        print('input')
        pos += 1
    elif real_opcode[pos] == 0xF1:
        operation = real_opcode[pos + 1]
        if operation == 0xE1:
            op_num = bytes(real_opcode[pos + 2: pos + 6])
            op_num = u32(op_num)
            print(f'context[0] = input[{op_num}]')
        elif operation == 0xE2:
            op_num = bytes(real_opcode[pos + 2: pos + 6])
            op_num = u32(op_num)
            print(f'context[1] = input[{op_num}]')
        elif operation == 0xE3:
            op_num = bytes(real_opcode[pos + 2: pos + 6])
            op_num = u32(op_num)
            print(f'context[2] = input[{op_num}]')
        elif operation == 0xE4:
            op_num = bytes(real_opcode[pos + 2: pos + 6])
            op_num = u32(op_num)
            print(f'input[{op_num}] = context[0]')
        elif operation == 0xE5:
            op_num = bytes(real_opcode[pos + 2: pos + 6])
            op_num = u32(op_num)
            print(f'context[3] = input[{op_num}]')
        elif operation == 0xE7:
            op_num = bytes(real_opcode[pos + 2: pos + 6])
            op_num = u32(op_num)
            print(f'input[{op_num}] = context[1]')
        pos += 6
    elif real_opcode[pos] == 0xF2:
        print('context[0] ^= context[1]')
        pos += 1
    elif real_opcode[pos] == 0xF6:
        print('context[0] = context[2] + 2 * context[1] + 3 * context[0]')
        pos += 1
    elif real_opcode[pos] == 0xF7:
        print('context[0] *= context[3]')
        pos += 1
    elif real_opcode[pos] == 0xF8:
        print('context[0], context[1] = context[1], context[0]')
        pos += 1

input = [0x69, 0x45, 0x2A, 0x37, 0x09, 0x17, 0xC5, 0x0B, 0x5C, 0x72, 0x33, 0x76, 0x33, 0x21, 0x74, 0x31, 0x5F, 0x33, 0x73, 0x72]
context = [0] * 4

input[15], input[17] = input[17], input[15]
input[14], input[18] = input[18], input[14]
input[13], input[19] = input[19], input[13]

for num in range(256):
    context[0] = num
    context[1] = input[9]
    context[2] = input[10]
    context[3] = input[12]
    context[0] = context[2] + 2 * context[1] + 3 * context[0]
    context[0] *= context[3]
    if context[0] % 256 == input[8]:
        input[8] = num
        break

for num in range(256):
    context[0] = num
    context[1] = input[8]
    context[2] = input[9]
    context[3] = input[12]
    context[0] = context[2] + 2 * context[1] + 3 * context[0]
    context[0] *= context[3]
    if context[0] % 256 == input[7]:
        input[7] = num
        break

for num in range(256):
    context[0] = num
    context[1] = input[7]
    context[2] = input[8]
    context[3] = input[12]
    context[0] = context[2] + 2 * context[1] + 3 * context[0]
    context[0] *= context[3]
    if context[0] % 256 == input[6]:
        input[6] = num
        break

input[5] ^= input[6]
input[4] ^= input[5]
input[3] ^= input[4]
input[2] ^= input[3]
input[1] ^= input[2]
input[0] ^= input[1]

print(bytes(input))
# Y0u_hav3_r3v3rs3_1t!