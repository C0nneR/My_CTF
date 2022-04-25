mul = [0x249E15C5, 0x34C7EAE2, 0x637973BA, 0xE5FD104]
sub = [0xFFFF59BC, 0x216B, 0x819D, 0x9393]

flag = ''
for i in range(4):
    for a in range(0xffff):
        b = (a - sub[i]) & 0xffff
        if a * b == mul[i]:
            flag += hex(a)[2:].upper()
            flag += hex(b)[2:].upper()

print(flag)