import base64

original_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
changed_table = "TGtUnkaJD0frq61uCQYw3-FxMiRvNOB/EWjgVcpKSzbs8yHZ257X9LldIeh4APom"
trans = str.maketrans(changed_table, original_table)

encoded = '3lkHi9iZNK87qw0p6U391t92qlC5rwn5iFqyMFDl1t92qUnL6FQjqln76l-P'
decoded = base64.b64decode(encoded.translate(trans).encode('utf-8'))
print(decoded)