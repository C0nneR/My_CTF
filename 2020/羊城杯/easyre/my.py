cipher = list('EmBmP5Pmn7QcPU4gLYKv5QcMmB3PWHcP5YkPq3=cT6QckkPckoRG')

num = '0123456789'
low = 'abcdefghijklmnopqrstuvwxyz'
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i, char in enumerate(cipher):
    if char in num:
        cipher[i] = num[(ord(char) - ord('0') - 3) % 10]
    elif char in low:
        cipher[i] = low[(ord(char) - ord('a') - 3) % 26]
    elif char in up:
        cipher[i] = up[(ord(char) - ord('A') - 3) % 26]
cipher = ''.join(cipher)

cipher = cipher[13:26] + cipher[39:52] + cipher[0:13] + cipher[26:39]
import base64
plain = base64.b64decode(cipher.encode())
print(plain)
# GWHT{672cc4778a38e80cb362987341133ea2}