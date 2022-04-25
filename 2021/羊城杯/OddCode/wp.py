from unicorn import *
from unicorn.x86_const import *
from capstone import *

ADDRESS = 0x2E1000
INPUT_ADDRESS = 0x2E701D
KEY_ADDRESS = 0x2E705C

with open('OddCode.exe', 'rb') as file:
    file.seek(0x400)
    X64_CODE = file.read(0x4400)

class Unidbg:
    def __init__(self, flag, expect_hit):
        self.expect_hit = expect_hit
        self.hit = 0
        self.success = False

        mu = Uc(UC_ARCH_X86, UC_MODE_64)
        mu.mem_map(ADDRESS, 0x1000000)
        mu.mem_write(ADDRESS, X64_CODE)
        mu.mem_write(INPUT_ADDRESS, flag)
        mu.mem_write(KEY_ADDRESS, b'\x90\xF0\x70\x7C\x52\x05\x91\x90\xAA\xDA\x8F\xFA\x7B\xBC\x79\x4D')

        mu.reg_write(UC_X86_REG_RAX, 1)
        mu.reg_write(UC_X86_REG_RBX, 0x51902D)
        mu.reg_write(UC_X86_REG_RCX, 0xD86649D8)
        mu.reg_write(UC_X86_REG_RDX, 0x2E701C)
        mu.reg_write(UC_X86_REG_RSI, INPUT_ADDRESS)
        mu.reg_write(UC_X86_REG_RDI, KEY_ADDRESS)
        mu.reg_write(UC_X86_REG_RBP, 0x6FFBBC)
        mu.reg_write(UC_X86_REG_RSP, 0x6FFBAC)
        mu.reg_write(UC_X86_REG_RIP, 0x2E1010)
        mu.hook_add(UC_HOOK_CODE, self.trace)
        # mu.hook_add(UC_HOOK_MEM_READ, self.hook_mem_read)

        self.mu = mu
        self.except_addr = 0
        self.traces = []
        self.md = Cs(CS_ARCH_X86, CS_MODE_64)

    def trace(self, mu, address, size, data):
        # disasm = self.md.disasm(mu.mem_read(address, size), address)
        # for i in disasm:
        #     mnemonic = i.mnemonic
        #     if mnemonic == 'cmp' or mnemonic == 'test':
        #         print(f'Instruction {mnemonic} at {hex(address)}')

        if address != self.except_addr:
            self.traces.append(address)
        self.except_addr = address + size

        if address == 0x2E38EF:
            self.hit += 1
            if self.hit == self.expect_hit:
                self.success = True
                mu.emu_stop()

    def hook_mem_read(self, mu, access, address, size, value, data):
        if address >= INPUT_ADDRESS and address <= INPUT_ADDRESS + 41:
            print(f'Read input[{address - INPUT_ADDRESS}] at {hex(mu.reg_read(UC_X86_REG_RIP))}')
        if address >= KEY_ADDRESS and address <= KEY_ADDRESS + 16:
            print(f'Read key[{address - KEY_ADDRESS}] at {hex(mu.reg_read(UC_X86_REG_RIP))}')

    def solve(self):
        try:
            self.mu.emu_start(0x2E1010, -1)
        except:
            pass
        # print([hex(addr) for addr in self.traces])
        return self.success

def get_flag(flag, expect_hit):
    for i in b'1234567890abcdefABCDEF':
        for j in b'1234567890abcdefABCDEF':
            flag[8 + (expect_hit - 1) * 2] = i
            flag[8 + (expect_hit - 1) * 2 + 1] = j
            if Unidbg(bytes(flag), expect_hit).solve():
                return

flag = bytearray(b'SangFor{00000000000000000000000000000000}')
for i in range(1, 17):
    get_flag(flag, i)
    print(flag.decode())