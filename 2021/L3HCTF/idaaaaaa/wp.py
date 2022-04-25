
# cipher_index = [287, 96, 8, 777, 496, 822,
# 				 914, 550, 273, 259, 334, 966,
# 				 331, 680, 374, 717, 965, 952,
# 				 222]
# keys = [b'lqAT7pNI3BX', b'z3Uhis74aPq', b'9tjseMGBHR5', b'FhnvgMQjexH', b'SKnZ51f9WsE', b'gDJy104BSHW',
# 		b'PbRV4rSM7fd', b'WHPnoMTsbx3', b'mLx5hvlqufG', b'QvKgNmUFTnW', b'TCrHaitRfY1', b'm26IAvjq1zC',
# 		b'dQb2ufTZwLX', b'Y6Sr7znOeHL', b'hLFj1wl5A0U', b'H6W03R7TLFe', b'fphoJwDKsTv', b'CMF1Vk7NH4O',
# 		b'43PSbAlgLqj']

def decrypt(ct, key):
	res = ''
	for i in range(len(ct)):
		res += chr(ct[i] ^ key[i % 11])
	return res.encode()

# for i in range(19):
# 	print(decrypt(jIS40A[cipher_index[i]], keys[i]))

def getNextList(cryptedBytes):
	pos = cryptedBytes.find(b'ord(\'a\')\n')
	nextList = []
	while True:
		edge = {'id': 0, 'v': 0, 'key': b''}

		pos = cryptedBytes.find(b'==', pos)
		if pos == -1:
			break
		eolpos = cryptedBytes.find(b':\n', pos)
		edge['id'] = eval(cryptedBytes[pos + 3:eolpos])

		pos = cryptedBytes.find(b'=', pos + 3)
		eolpos = cryptedBytes.find(b'\n', pos)
		edge['v'] = eval(cryptedBytes[pos + 2:eolpos])

		pos = cryptedBytes.find(b'=', pos + 2)
		eolpos = cryptedBytes.find(b'\n', pos)
		edge['key'] = eval(cryptedBytes[pos + 2:eolpos])

		nextList.append(edge)
	return nextList

rootBytes = b'VLzxDy = idaapi.get_byte(5127584 + N4QKUt)\nVLzxDy -= ord(\'a\')\nif VLzxDy == 0:\n    bYsMTa = 287\n    LjzrdT = b\'lqAT7pNI3BX\'\nelif VLzxDy == 1:\n    bYsMTa = 96\n    LjzrdT = b\'z3Uhis74aPq\'\nelif VLzxDy == 2:\n    bYsMTa = 8\n    LjzrdT = b\'9tjseMGBHR5\'\nelif VLzxDy == 3:\n    bYsMTa = 777\n    LjzrdT = b\'FhnvgMQjexH\'\nelif VLzxDy == 4:\n    bYsMTa = 496\n    LjzrdT = b\'SKnZ51f9WsE\'\nelif VLzxDy == 5:\n    bYsMTa = 822\n    LjzrdT = b\'gDJy104BSHW\'\nelif VLzxDy == 6:\n    bYsMTa = 914\n    LjzrdT = b\'PbRV4rSM7fd\'\nelif VLzxDy == 7:\n    bYsMTa = 550\n    LjzrdT = b\'WHPnoMTsbx3\'\nelif VLzxDy == 8:\n    bYsMTa = 273\n    LjzrdT = b\'mLx5hvlqufG\'\nelif VLzxDy == 9:\n    bYsMTa = 259\n    LjzrdT = b\'QvKgNmUFTnW\'\nelif VLzxDy == 10:\n    bYsMTa = 334\n    LjzrdT = b\'TCrHaitRfY1\'\nelif VLzxDy == 11:\n    bYsMTa = 966\n    LjzrdT = b\'m26IAvjq1zC\'\nelif VLzxDy == 12:\n    bYsMTa = 331\n    LjzrdT = b\'dQb2ufTZwLX\'\nelif VLzxDy == 13:\n    bYsMTa = 680\n    LjzrdT = b\'Y6Sr7znOeHL\'\nelif VLzxDy == 14:\n    bYsMTa = 374\n    LjzrdT = b\'hLFj1wl5A0U\'\nelif VLzxDy == 15:\n    bYsMTa = 717\n    LjzrdT = b\'H6W03R7TLFe\'\nelif VLzxDy == 16:\n    bYsMTa = 965\n    LjzrdT = b\'fphoJwDKsTv\'\nelif VLzxDy == 17:\n    bYsMTa = 952\n    LjzrdT = b\'CMF1Vk7NH4O\'\nelif VLzxDy == 18:\n    bYsMTa = 222\n    LjzrdT = b\'43PSbAlgLqj\'\nelse:\n    bYsMTa = -1\nif bYsMTa < 0:\n    cpu.rsp -= 8\n    cpu.rdi = 4927649\n    cpu.rax = 0\n    idaapi.patch_qword(cpu.rsp, 4202616)\n    idaapi.del_bpt(cpu.rip)\n    cpu.rip = 4263680\nelse:\n    zaqhdD = 0x486195\n    bYsMTa = jIS40A[bYsMTa]\n\n    idaapi.patch_bytes(5117568, bYsMTa)\n    idaapi.patch_bytes(5117488, LjzrdT)\n\n    cpu.rsp -= 8\n    idaapi.patch_qword(cpu.rsp, zaqhdD)\n    cpu.rdi = 5117568\n    cpu.rsi = len(bYsMTa)\n    cpu.rdx = 5117488\n    cpu.rcx = 11\n    cpu.r8 = 5117568\n    cpu.rax = 5117568\n\n    idaapi.add_bpt(zaqhdD)\n    jQfwUA = idaapi.bpt_t()\n    idaapi.get_bpt(zaqhdD, jQfwUA)\n    jQfwUA.elang = "Python"\n    jQfwUA.condition = "N4QKUt = {}\\nSdjOr3 = {}\\n".format(N4QKUt, len(bYsMTa)) + \'bYsMTa = idaapi.get_bytes(cpu.rax, SdjOr3).decode()\\nzaqhdD = 4767838\\nidaapi.add_bpt(zaqhdD)\\njQfwUA = idaapi.bpt_t()\\nidaapi.get_bpt(zaqhdD, jQfwUA)\\njQfwUA.elang = "Python"\\njQfwUA.condition = "N4QKUt = {}\\\\n".format(N4QKUt+1) + bYsMTa\\nidaapi.del_bpt(zaqhdD)\\nidaapi.add_bpt(jQfwUA)\\nidaapi.del_bpt(cpu.rip)\\ncpu.rsp -= 8\\nidaapi.patch_qword(cpu.rsp, zaqhdD)\\ncpu.rip = 4447160\\n\'\n    idaapi.del_bpt(zaqhdD)\n    idaapi.add_bpt(jQfwUA)\n    idaapi.del_bpt(cpu.rip)\n    cpu.rip = 4201909\n'

G = {}
root = 0
vis = [0 for i in range(1000)]

def buildG(cur, curBytes):
	if vis[cur] != 0:
		return
	vis[cur] = 1
	curStruct = {}
	curStruct['plaintext'] = curBytes
	curStruct['nextList'] = getNextList(curBytes)
	G[cur] = curStruct

	for e in curStruct['nextList']:
		nextBytes = jIS40A[e['v']]
		nextBytes = decrypt(nextBytes, e['key'])
		buildG(e['v'], nextBytes)

buildG(root, rootBytes)

# for n, s in G.items():
# 	if len(s['nextList']) == 0:
# 		print(n)
# 		print(s['plaintext'].decode())

import queue

def dij(s, t):
	dis = [0x3f3f3f3f for i in range(1000)]
	done = [0 for i in range(1000)]
	path = [-1 for i in range(1000)]
	pathId = [-1 for i in range(1000)]

	dis[s] = 0
	que = queue.PriorityQueue()
	que.put([0, s])
	while not que.empty():
		[cdis, cur] = que.get()
		if done[cur] != 0:
			continue
		done[cur] = 1
		if cur == t:
			break
		for e in G[cur]['nextList']:
			if dis[e['v']] > cdis + 1:
				dis[e['v']] = cdis + 1
				path[e['v']] = cur
				pathId[e['v']] = e['id']
				que.put([dis[e['v']], e['v']])
	validInput = []
	cur = t
	while cur != s:
		c = pathId[cur]
		validInput.append(chr(ord('a') + c))
		cur = path[cur]
	validInput.reverse()
	return validInput

result = dij(0, 426)
print(''.join(result))