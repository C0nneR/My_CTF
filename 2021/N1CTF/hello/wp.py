encrypted_nums = [(201), (247), (36), (211), (26), (224), (241), (131), (112), (24), (2), (0), (17), (243), (56), (186)]
encrypted_nums = bytes(encrypted_nums)

key = b'NU1Lnu1lnu1lNU1L'
from Crypto.Cipher import AES

dec = AES.new(key, AES.MODE_ECB)
plain = dec.decrypt(encrypted_nums)
print('n1ctf{%s}' % plain.hex())