import base64
from pwn import *

p = remote('pwn-2021.duc.tf', 31914)

def loop(msg):
	global p

	p.recvuntil('Enter plaintext:\n')
	p.send(msg + '\n')
	cipher = p.recvuntil('\n').strip()
	return base64.b64decode(cipher)

key = '!_SECRETSOURCE_!'
# for char in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
# 	msg = 'A' * (15 - len(key)) + key + char + 'A' * (15 - len(key))
# 	cipher = loop(msg)
# 	guess = cipher[32:48]
# 	right = cipher[48:64]
# 	if guess == right:
# 		print(char)
# 		break

# p.close()

from Crypto.Cipher import AES
cipher_text = loop('')
cipher_text = cipher_text[:32]
cipher = AES.new(key, AES.MODE_ECB)
print(cipher.decrypt(cipher_text))