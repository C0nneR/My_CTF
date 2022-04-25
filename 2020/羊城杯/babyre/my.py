from Crypto.Cipher import DES, AES

DES_cipher = b"\x0A\xF4\xEE\xC8\x42\x8A\x9B\xDB\xA2\x26\x6F\xEE\xEE\xE0\xD8\xA2"
DES_key = b'\xAD\x52\xF2\x4C\xE3\x2C\x20\xD6'
DES_iv = b'\x00\x00\x00\x00\x00\x00\x00\x00'
DES_obj = DES.new(DES_key, DES.MODE_CBC, DES_iv)
DES_plain = DES_obj.decrypt(DES_cipher)

AES_key = DES_plain

# tese_plain = b'a' * 16 + b'b' * 16
AES_obj = AES.new(AES_key, AES.MODE_ECB)
# test_cipher = AES_obj.encrypt(tese_plain)
# test_cipher = list(test_cipher)
# for i in range(32):
#     for j in range(i // 4):
#         test_cipher[i] ^= test_cipher[j]

# encoded_input = [0] * 31
# for k in range(1, 32):
#     encoded_input[k - 1] = ((2 * (test_cipher[k - 1] ^ 0x13) + 7) & 0xff) ^ ((test_cipher[k - 1] % 9 + test_cipher[k] + 2) & 0xff)

encoded_input = [0xBD, 0xAD, 0xB4, 0x84, 0x10, 0x63, 0xB3, 0xE1, 0xC6, 0x84, 0x2D, 0x6F, 0xBA, 0x88, 0x74, 0xC4, 0x90, 0x32, 0xEA, 0x2E, 0xC6, 0x28, 0x65, 0x70, 0xC9, 0x75, 0x78, 0xA0, 0x0B, 0x9F, 0xA6]

for i in range(256):
    test_cipher = [0] * 32
    test_cipher[0] = i
    for k in range(1, 32):
        test_cipher[k] = ((encoded_input[k - 1] ^ ((2 * (test_cipher[k - 1] ^ 0x13) + 7) & 0xff)) - 2 - (test_cipher[k - 1] % 9)) &0xff
    if test_cipher[31] == 0xc4:
        for p in range(31, -1, -1):
            for q in range(p // 4 - 1, -1, -1):
                test_cipher[p] ^= test_cipher[q]
        plain = AES_obj.decrypt(bytes(test_cipher))
        print(plain)

# GWHT{th1s_gam3_1s_s0_c00l_and_d}