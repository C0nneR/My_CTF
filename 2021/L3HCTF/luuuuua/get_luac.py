fr = open('logo.jpg', 'rb')
fr.seek(0x3afa1)
data = fr.read()
fr.close()

data = list(data)
for i in range(1, len(data)):
    data[i] ^= 0x3c
data = bytes(data)

fw = open('luac', 'wb')
fw.write(data)
fw.close()