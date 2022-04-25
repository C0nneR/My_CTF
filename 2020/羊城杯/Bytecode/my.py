# flag = input('please input your flag:')
# str = flag
# a = len(str)
# if a >= 38:
#     print('lenth wrong!')
#     exit(0)

# if (((ord(str[0])*2020+ord(str[1]))*2020+ord(str[2]))*2020+ord(str[3]))*2020+ord(str[4]) != 1182843538814603:
#     print('bye~')
#     exit(0)

# num = 1182843538814603
# prefix = [''] * 5
# for i in range(4, -1, -1):
#     prefix[i] = chr(num % 2020)
#     num = num // 2020
# print(''.join(prefix))
prefix = 'GWHT{'

# en = [3, 37, 72, 9, 6, 132]
# output = [101, 96, 23, 68, 112, 42, 107, 62, 96, 53, 176, 179, 98, 53, 67, 29, 41, 120, 60, 106, 51, 101, 178, 189, 101, 48]

# x = []
# k = 5
# for i in range(13):
#     b = ord(str[k])
#     c = ord(str[k + 1])
#     a11 = en[i % 6] ^ c
#     a22 = en[i % 6] ^ b
#     x.append(a11)
#     x.append(a22)
#     k += 2

# if x != output:
#     print('oh,you are wrong!')
#     exit(0)

# middle = ''
# for i in range(13):
#     c = output[i * 2] ^ en[i % 6]
#     b = output[i * 2 + 1] ^ en[i % 6]
#     middle += chr(b)
#     middle += chr(c)
# print(middle)
middle = 'cfa2b87b3f746a8f0ac5c5963f'

# l = len(str)
# a1 = ord(str[l - 7])
# a2 = ord(str[l - 6])
# a3 = ord(str[l - 5])
# a4 = ord(str[l - 4])
# a5 = ord(str[l - 3])
# a6 = ord(str[l - 2])

# if a1*3+a2*2+a3*5==1003:
#     if a1*4+a2*7+a3*9==2013:
#         if a1+a2*8+a3*2==1109:
#             if a4*3+a5*2+a6*5==671:
#                 if a4*4+a5*7+a6*9==1252:
#                     if a4+a5*8+a6*2==644:
#                         print('congraduation!you get the right flag!')

from z3 import *

s = Solver()
a1, a2, a3, a4, a5, a6 = [Int('a%d' % i) for i in range(1, 7)]
s.add(a1*3+a2*2+a3*5==1003)
s.add(a1*4+a2*7+a3*9==2013)
s.add(a1+a2*8+a3*2==1109)
s.add(a4*3+a5*2+a6*5==671)
s.add(a4*4+a5*7+a6*9==1252)
s.add(a4+a5*8+a6*2==644)

result = {}
if s.check() == sat:
    m = s.model()
    for i in m:
        result[str(i)] = chr(m[i].as_long())
flag = prefix + middle
for i in range(1, 7):
    flag += result['a%d' % i]
print(flag + '}')