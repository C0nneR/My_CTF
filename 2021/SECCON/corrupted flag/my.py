from typing import *

def find_corrupt_bit(bits: List[int]) -> int:
    _0, _1, _2, _3 = bits[0], bits[1], bits[2], bits[4]
    find_dict = {}

    find_dict['012'] = (_0 ^ _1 ^ _2 == bits[3])
    find_dict['013'] = (_0 ^ _1 ^ _3 == bits[5])
    find_dict['023'] = (_0 ^ _2 ^ _3 == bits[6])
    
    if (find_dict['012'] == False) and (find_dict['013'] == False) and (find_dict['023'] == False):
        return 0
    
    if (find_dict['012'] == False) and (find_dict['013'] == False) and (find_dict['023'] == True):
        return 1
    
    if (find_dict['012'] == False) and (find_dict['013'] == True) and (find_dict['023'] == False):
        return 2
    
    if (find_dict['012'] == True) and (find_dict['013'] == False) and (find_dict['023'] == False):
        return 4
    
    return -1

fr = open('flag.txt.enc', 'rb')
encrypted = fr.read()
fr.close()

shuffled = ''
for num in encrypted:
    shuffled += ((bin(num)[2:]).rjust(8, '0'))[::-1]

flag = ''
for i in range(len(shuffled) // 14):
    to_find_corrupt_one = [int(num) for num in shuffled[i * 14: i * 14 + 7]]
    to_find_corrupt_two = [int(num) for num in shuffled[i * 14 + 7: i * 14 + 14]]

    currupt_pos_one = find_corrupt_bit(to_find_corrupt_one)
    currupt_pos_two = find_corrupt_bit(to_find_corrupt_two)

    if currupt_pos_one >= 0:
        to_find_corrupt_one[currupt_pos_one] ^= 1
    if currupt_pos_two >= 0:
        to_find_corrupt_two[currupt_pos_two] ^= 1

    temp = ''
    temp += str(to_find_corrupt_two[4])
    temp += str(to_find_corrupt_two[2])
    temp += str(to_find_corrupt_two[1])
    temp += str(to_find_corrupt_two[0])
    temp += str(to_find_corrupt_one[4])
    temp += str(to_find_corrupt_one[2])
    temp += str(to_find_corrupt_one[1])
    temp += str(to_find_corrupt_one[0])
    temp = int(temp, 2)
    flag += chr(temp)
print(flag)
# SECCON{9e469af5f60e7f0c98854ebf0afd254c102154587a7491594900a8d186df4801}