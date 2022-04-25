# import os

# class TreeNode:
#     def __init__(self, path = '', data = '', left = None, right = None):
#         self.path = path
#         self.data = data
#         self.left = left
#         self.right = right

#     def __str__(self):
#         return self.data

#     def read_data(self):
#         fr = open(f'{self.path}\\data', 'r')
#         data = fr.read().strip()
#         fr.close()
#         return data

# def create_tree(root: TreeNode) -> TreeNode:
#     _dir = os.listdir(root.path)
#     len_dir = len(_dir)
#     assert len_dir == 3 or len_dir == 1

#     if len(_dir) == 3:
#         root.data = root.read_data()

#         root.left = TreeNode(f'{root.path}\\letf')
#         root.left = create_tree(root.left)

#         root.right = TreeNode(f'{root.path}\\Right')
#         root.right = create_tree(root.right)

#         return root
#     else:
#         root.data = root.read_data()
#         return root
        
# root_path = 'C:\\Users\\18502\\Desktop\\Practices\\CTF\\2021\\SCTF\\This_is_A_tree'
# root = TreeNode(root_path)
# root = create_tree(root)

# def output(root: TreeNode):
#     if root != None:
#         print(root.data, end = '')
#         output(root.left)
#         output(root.right)

# output(root)
# print('')

# encoded = 'Q2hpbmVzZSB0cmFkaXRpb25hbCBjdWx0dXJlIGlzIGJyb2FkIGFuZCBwcm9mb3VuZCEgU28gSSBXYW50IEdpdmUgWW91IE15IEZsYWcgQnV0IFlvdSBOZWVkIERlY29kZSBJdC5FbmpveSBUaGUgRmxhZyEhOuW4iCDlhZEg5aSNIOaNnyDlt70g6ZyHIOaZiyDlp6Qg5aSn6L+HIOiuvCDlmazll5Eg6ZyHIOaBkiDoioIg6LGrIA=='
# import base64

# plain = base64.b64decode(encoded)[118:]
# print(plain.decode('utf-8'))

plain = ['师', '兑', '复', '损', '巽', '震', '晋', '姤', '大过', '讼', '噬嗑', '震', '恒', '节', '豫']

# box = ['乾', '坤', '屯', '蒙', '需',
#        '讼', '师', '比', '小畜', '履',
#        '泰', '否', '同人', '大有', '谦',
#        '豫', '随', '蛊', '临', '观',
#        '噬嗑', '贲', '剥', '复', '无妄',
#        '大畜', '颐', '大过', '坎', '离',
#        '咸', '恒', '遁', '大壮', '晋',
#        '明夷', '家人', '睽', '蹇', '解',
#        '损', '益', '夬', '姤', '萃',
#        '升困', '井', '革', '鼎',
#        '震', '艮', '渐', '归妹', '丰',
#        '旅', '巽', '兑', '涣', '节',
#        '中孚', '小过', '既济', '未济']

dic = {'坤': '000000', '剥': '000001', '比': '000010', '观': '000011', '豫': '000100', '晋': '000101', '萃': '000110', '否': '000111', '谦': '001000', '艮': '001001', '蹇': '001010', '渐': '001011', '小过': '001100', '旅': '001101', '咸': '001110', '遁': '001111', '师': '010000', '蒙': '010001', '坎': '010010', '涣': '010011', '解': '010100', '未济': '010101', '困': '010110', '讼': '010111', '升': '011000', '蛊': '011001', '井': '011010', '巽': '011011', '恒': '011100', '鼎': '011101', '大过': '011110', '姤': '011111', '复': '100000', '颐': '100001', '屯': '100010', '益': '100011', '震': '100100', '噬嗑': '100101', '随': '100110', '无妄': '100111', '明夷': '101000', '贲': '101001', '既济': '101010', '家人': '101011', '丰': '101100', '离': '101101', '革': '101110', '同人': '101111', '临': '110000', '损': '110001', '节': '110010', '中孚': '110011', '归妹': '110100', '睽': '110101', '兑': '110110', '履': '110111', '泰': '111000', '大畜': '111001', '需': '111010', '小畜': '111011', '大壮': '111100', '大有': '111101', '夬': '111110', '乾': '111111'}

flag = ''
for char in plain:
    flag += dic[char]

decode = ''
for i in range(len(flag) // 8):
    decode += chr(int(flag[i * 8: i * 8 + 8], 2))
print(decode)