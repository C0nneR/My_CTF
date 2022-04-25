import base64

original_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
changed_table = "ABCDEFGHIJKLMNOPQRST0123456789+/UVWXYZabcdefghijklmnopqrstuvwxyz"
trans = str.maketrans(changed_table, original_table)

encoded = '7G5d5bAy+TMdLWlu5CdkMTlcJnwkNUgb2AQL3CcmPpVf6DAp72scOSlb'
decoded = base64.b64decode(encoded.translate(trans).encode('utf-8'))
decoded = list(decoded)

input_len = len(decoded)
for i in range(1, 11):
	for j in range(input_len):
		if input_len % i:
			decoded[j] ^= i + j
		else:
			decoded[j] ^= (j % i) + j
print(bytes(decoded))