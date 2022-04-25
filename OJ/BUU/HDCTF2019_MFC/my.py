from Crypto.Cipher import DES

key = b'{I am a Des key}'[:8]
assert len(key) == 8

obj = DES.new(key, DES.MODE_ECB)
cipher = bytes.fromhex('944c8d100f82f0c18b682f63e4dbaa207a2f1e72581c2f1b')
plain = obj.decrypt(cipher)
print(plain)