# import phoenixAES

# with open('tracefile', 'wb') as t:
#     t.write("""
# 706020b140ae0d85e9a6cff90e275d6f
# fb6020b140ae0ddae9a6b0f90ed65d6f
# 706020d040aeae85e9c8cff9ff275d6f
# 70609ab1408e0d85e2a6cff90e275d9f
# 706120b169ae0d85e9a6cfdf0e27a06f
# 706320b1c2ae0d85e9a6cf230e27666f
# ab6020b140ae0dbce9a62bf90ea75d6f
# 7060202f40ae8185e980cff906275d6f
# 706072b140650d85b9a6cff90e275d8d
# """.encode('utf8'))

# phoenixAES.crack_file('tracefile')

from aeskeyschedule import *

round_key = bytes.fromhex("130F86574C77E77C7BDE40266A1F3F72")
base_key = reverse_key_schedule(round_key, 10)
print(base_key)