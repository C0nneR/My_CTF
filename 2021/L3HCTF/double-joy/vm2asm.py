import struct

opcode_5280 = b"\x11\x15\x00\x00\x00\x0E\x0A\x00\x00\x00\x0E\x15\xCD\x5B\x07\x08\x0E\x0B\x00\x00\x00\x0E\xB1\x68\xDE\x3A\x08\x0E\x12\x00\x00\x00\x0E\x00\x00\x00\x00\x08\x0E\x13\x00\x00\x00\x0E\x00\x00\x00\x00\x08\x0E\x13\x00\x00\x00\x09\x0E\x0A\x00\x00\x00\x0C\x01\x0B\x0A\x10\x44\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x00\x00\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x00\x00\x00\x00\x00\x09\x0E\x13\x00\x00\x00\x09\x0E\x01\x00\x00\x00\x00\x0E\x01\x01\x01\x01\x02\x07\x08\x0E\x13\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x01\x00\x00\x00\x00\x08\x0F\xA8\xFF\xFF\xFF\x0E\x00\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x0E\x4C\x49\x00\x00\x08\x0E\x01\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x0E\x76\x6F\x00\x00\x08\x0E\x02\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x0E\x20\x65\x00\x00\x08\x0E\x03\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x0E\x55\x43\x00\x00\x08\x0E\x13\x00\x00\x00\x0E\x00\x00\x00\x00\x08\x0E\x13\x00\x00\x00\x09\x0E\x0A\x00\x00\x00\x0C\x01\x0B\x0A\x10\x56\x01\x00\x00\x0E\x14\x00\x00\x00\x0E\x00\x00\x00\x00\x08\x0E\x14\x00\x00\x00\x09\x0E\x14\x00\x00\x00\x0C\x01\x0B\x0A\x10\x20\x01\x00\x00\x0E\x0C\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x00\x00\x00\x00\x00\x09\x08\x0E\x0D\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x01\x00\x00\x00\x00\x0E\x00\x00\x00\x00\x00\x09\x08\x0E\x0C\x00\x00\x00\x0E\x0C\x00\x00\x00\x09\x0E\x0D\x00\x00\x00\x09\x0E\x10\x00\x00\x00\x02\x0E\x0D\x00\x00\x00\x09\x0E\x20\x00\x00\x00\x0C\x03\x07\x0E\x0D\x00\x00\x00\x09\x00\x0E\x0B\x00\x00\x00\x09\x0E\x0B\x00\x00\x00\x09\x0E\x03\x00\x00\x00\x05\x0E\x0E\x00\x00\x00\x00\x09\x00\x07\x00\x08\x0E\x0B\x00\x00\x00\x0E\x0B\x00\x00\x00\x09\x0E\x0A\x00\x00\x00\x09\x00\x08\x0E\x0D\x00\x00\x00\x0E\x0D\x00\x00\x00\x09\x0E\x0C\x00\x00\x00\x09\x0E\x10\x00\x00\x00\x02\x0E\x0C\x00\x00\x00\x09\x0E\x20\x00\x00\x00\x0C\x03\x07\x0E\x0C\x00\x00\x00\x09\x00\x0E\x0B\x00\x00\x00\x09\x0E\x0B\x00\x00\x00\x09\x0E\x00\x08\x00\x00\x0C\x03\x0E\x03\x00\x00\x00\x05\x0E\x0E\x00\x00\x00\x00\x09\x00\x07\x00\x08\x0E\x13\x00\x00\x00\x09\x0E\x00\x00\x00\x00\x00\x0E\x0C\x00\x00\x00\x09\x08\x0E\x13\x00\x00\x00\x09\x0E\x01\x00\x00\x00\x00\x0E\x00\x00\x00\x00\x00\x0E\x0D\x00\x00\x00\x09\x08\x12\x01\x00\x00\x00\x0E\x14\x00\x00\x00\x0E\x14\x00\x00\x00\x09\x0E\x01\x00\x00\x00\x00\x08\x0F\xCC\xFE\xFF\xFF\x0E\x13\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x02\x00\x00\x00\x00\x08\x0F\x96\xFE\xFF\xFF\x12\x00\x00\x00\x00"
opcode_5020 = b"\x11\x15\x00\x00\x00\x0E\x0A\x00\x00\x00\x0E\xF7\xCB\x54\x01\x08\x0E\x0B\x00\x00\x00\x0E\xAD\xDE\xED\x5E\x08\x0E\x12\x00\x00\x00\x0E\x00\x00\x00\x00\x08\x0E\x13\x00\x00\x00\x0E\x00\x00\x00\x00\x08\x0E\x13\x00\x00\x00\x09\x0E\x0A\x00\x00\x00\x0C\x01\x0B\x0A\x10\x44\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x00\x00\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x00\x00\x00\x00\x00\x09\x0E\x13\x00\x00\x00\x09\x0E\x01\x00\x00\x00\x00\x0E\x01\x01\x01\x01\x02\x07\x08\x0E\x13\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x01\x00\x00\x00\x00\x08\x0F\xA8\xFF\xFF\xFF\x0E\x00\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x0E\x54\x53\x00\x00\x08\x0E\x01\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x0E\x4D\x4F\x00\x00\x08\x0E\x02\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x0E\x74\x20\x00\x00\x08\x0E\x03\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x0E\x61\x65\x00\x00\x08\x0E\x13\x00\x00\x00\x0E\x00\x00\x00\x00\x08\x0E\x13\x00\x00\x00\x09\x0E\x0A\x00\x00\x00\x0C\x01\x0B\x0A\x10\x5B\x01\x00\x00\x0E\x14\x00\x00\x00\x0E\x00\x00\x00\x00\x08\x0E\x14\x00\x00\x00\x09\x0E\x14\x00\x00\x00\x0C\x01\x0B\x0A\x10\x25\x01\x00\x00\x0E\x0C\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x00\x00\x00\x00\x00\x09\x08\x0E\x0D\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x01\x00\x00\x00\x00\x0E\x00\x00\x00\x00\x00\x09\x08\x0E\x0B\x00\x00\x00\x0E\x0B\x00\x00\x00\x09\x0E\x0A\x00\x00\x00\x09\x00\x08\x0E\x0C\x00\x00\x00\x0E\x0C\x00\x00\x00\x09\x0E\x0D\x00\x00\x00\x09\x0E\x10\x00\x00\x00\x02\x0E\x00\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x09\x00\x0E\x0D\x00\x00\x00\x09\x0E\x0B\x00\x00\x00\x09\x00\x0E\x0D\x00\x00\x00\x09\x0E\x20\x00\x00\x00\x0C\x03\x0E\x01\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x09\x00\x07\x07\x00\x08\x0E\x0D\x00\x00\x00\x0E\x0D\x00\x00\x00\x09\x0E\x0C\x00\x00\x00\x09\x0E\x10\x00\x00\x00\x02\x0E\x02\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x09\x00\x0E\x0C\x00\x00\x00\x09\x0E\x0B\x00\x00\x00\x09\x00\x0E\x0C\x00\x00\x00\x09\x0E\x20\x00\x00\x00\x0C\x03\x0E\x03\x00\x00\x00\x0E\x0E\x00\x00\x00\x00\x09\x00\x07\x07\x00\x08\x0E\x13\x00\x00\x00\x09\x0E\x00\x00\x00\x00\x00\x0E\x0C\x00\x00\x00\x09\x08\x0E\x13\x00\x00\x00\x09\x0E\x01\x00\x00\x00\x00\x0E\x00\x00\x00\x00\x00\x0E\x0D\x00\x00\x00\x09\x08\x12\x01\x00\x00\x00\x0E\x14\x00\x00\x00\x0E\x14\x00\x00\x00\x09\x0E\x01\x00\x00\x00\x00\x08\x0F\xC7\xFE\xFF\xFF\x0E\x13\x00\x00\x00\x0E\x13\x00\x00\x00\x09\x0E\x02\x00\x00\x00\x00\x08\x0F\x91\xFE\xFF\xFF\x12\x00\x00\x00\x00"

def vm2asm(opcode, save_filename):
#     ip = 0
#     asm = ""
#     while ip < len(opcode):
#         asm += "label_{}:\n".format(ip)
#         if opcode[ip] == 0:
#             ip += 1
#             asm += """\
#     pop eax;
#     pop ebx;
#     add eax, ebx;
#     push eax;
# """
#         elif opcode[ip] == 1:
#             ip += 1
#             asm += """\
#     pop eax;
#     pop ebx;
#     sub eax, ebx;
#     push eax;
# """
#         elif opcode[ip] == 2:
#             ip += 1
#             asm += """\
#     pop eax;
#     pop ebx;
#     imul eax, ebx;
#     push eax;
# """
#         elif opcode[ip] == 3:
#             ip += 1
#             asm += """\
#     xor edx, edx;
#     pop eax;
#     pop ebx;
#     idiv ebx;
#     push eax;
# """
#         elif opcode[ip] == 4:
#             ip += 1
#             asm += """\
#     xor edx, edx;
#     pop eax;
#     pop ebx;
#     idiv ebx;
#     push edx;
# """
#         elif opcode[ip] == 5:
#             ip += 1
#             asm += """\
#     pop eax;
#     pop ebx;
#     and eax, ebx;
#     push eax;
# """
#         elif opcode[ip] == 6:
#             ip += 1
#             asm += """\
#     pop eax;
#     pop ebx;
#     or eax, ebx;
#     push eax;
# """
#         elif opcode[ip] == 7:
#             ip += 1
#             asm += """\
#     pop eax;
#     pop ebx;
#     xor eax, ebx;
#     push eax;
# """
#         elif opcode[ip] == 8:
#             ip += 1
#             asm += """\
#     pop eax;
#     pop ebx;
#     mov [ebp+4*ebx], eax;   
# """
#         elif opcode[ip] == 9:
#             ip += 1
#             asm += """\
#     mov eax, [ebp];
#     mov ebx, [ebp+4*eax];
#     mov [esp], ebx;
# """
#         elif opcode[ip] == 10:
#             ip += 1
#             asm += """\
#     xor ebx, ebx;
#     mov eax, [ebp];
#     test eax, eax;
#     sete bl;
#     mov [esp], ebx;
# """
#         elif opcode[ip] == 11:
#             ip += 1
#             asm += """\
#     mov eax, [esp];
#     shr eax, 31;
#     mov [esp], eax;
# """
#         elif opcode[ip] == 12:
#             ip += 1
#             asm += """\
#     pop eax;
#     pop ebx;
#     push eax;
#     push ebx;
# """
#         elif opcode[ip] == 13:
#             ip += 1
#             asm += """\
#     pop eax;
# """
#         elif opcode[ip] == 14:
#             val = struct.unpack("<i", opcode[ip + 1:ip + 5])[0]
#             ip += 5
#             asm += """\
#     push {};
# """.format(val)
#         elif opcode[ip] == 15:
#             val = struct.unpack("<i", opcode[ip + 1:ip + 5])[0]
#             ip += 5
#             asm += """\
#     jmp label_{};
# """.format(ip + val)
#         elif opcode[ip] == 16:
#             val = struct.unpack("<i", opcode[ip + 1:ip + 5])[0]
#             ip += 5
#             asm += """\
#     pop eax;
#     cmp eax, 0;
#     jnz label_{};
# """.format(ip + val)
#         elif opcode[ip] == 17:
#             val = struct.unpack("<i", opcode[ip + 1:ip + 5])[0]
#             ip += 5
#             asm += """\
#     sub esp, {};
# """.format(val * 4)
#         elif opcode[ip] == 18:
#             val = struct.unpack("<i", opcode[ip + 1:ip + 5])[0]
#             ip += 5
#             asm += """\
#     mov eax, {};
#     retn;
# """.format(val)
#         else:
#             ip += 1
    
#     fw = open(save_filename, 'w')
#     fw.write("section .text\n")
#     fw.write('bits 32\n')
#     fw.write(asm)
#     fw.close()
    ip = 0
    asm = ""
    while ip < len(opcode):
        asm += "label_{}:\n".format(ip)     # ip作为label
        if opcode[ip] == 0:     # add
            ip += 1
            asm += """\
    pop eax;
    pop ebx;
    add eax, ebx;
    push eax;
"""
        elif opcode[ip] == 1:     # sub
            ip += 1
            asm += """\
    pop eax;
    pop ebx;
    sub eax, ebx;
    push eax;
"""
        elif opcode[ip] == 2:       # imul
            ip += 1
            asm += """\
    pop eax;
    pop ebx;
    imul eax, ebx;
    push eax;
"""
        elif opcode[ip] == 3:       # idiv
            ip += 1
            asm += """\
    xor edx, edx;
    pop eax;
    pop ebx;
    idiv ebx;
    push eax;    
"""
        elif opcode[ip] == 4:       # mod
            ip += 1
            asm += """\
    pop eax;
    pop ebx;
    idiv ebx;
    push edx;    
"""
        elif opcode[ip] == 5:       # and
            ip += 1
            asm += """\
    pop eax;
    pop ebx;
    and eax, ebx;
    push eax;
"""
        elif opcode[ip] == 6:       # or
            ip += 1
            asm += """\
    pop eax;
    pop ebx;
    or eax, ebx;
    push eax;
"""
        elif opcode[ip] == 7:       # xor
            ip += 1
            asm += """\
    pop eax;
    pop ebx;
    xor eax, ebx;
    push eax;
"""
        elif opcode[ip] == 8:       # stack[TOS1]=TOS
            ip += 1
            asm += """\
    pop eax;
    pop ebx;
    mov [ebp+4*ebx], eax;
"""
        elif opcode[ip] == 9:       # TOS=stack[TOS]
            ip += 1
            asm += """\
    mov eax, [esp];
    mov ebx, [ebp+4*eax];
    mov [esp], ebx;
"""
        elif opcode[ip] == 10:      # TOS=!TOS
            ip += 1
            asm += """\
    xor ebx,ebx;
    mov eax, [esp];
    test eax, eax;
    sete bl;
    mov [esp], ebx;
"""
        elif opcode[ip] == 11:      # TOS=TOS<0
            ip += 1
            asm += """\
    mov eax, [esp];
    shr eax, 31;
    mov [esp], eax;
"""
        elif opcode[ip] == 12:      # xchg TOS1, TOS
            ip += 1
            asm += """\
    pop eax;
    pop ebx;
    push eax;
    push ebx;
"""
        elif opcode[ip] == 13:      # pop
            ip += 1
            asm += """\
    pop eax;
"""
        elif opcode[ip] == 14:      # push
            val = struct.unpack("<i", bytes(opcode)[ip+1:ip+5])[0]
            ip += 5
            asm += """\
    push {};
""".format(val)
        elif opcode[ip] == 15:      # jmp
            val = struct.unpack("<i", bytes(opcode)[ip+1:ip+5])[0]
            ip += 5
            asm += """\
    jmp label_{};
""".format(ip+val)
        elif opcode[ip] == 16:      # jnz  TOS
            val = struct.unpack("<i", bytes(opcode)[ip+1:ip+5])[0]
            # if stack[sp] != 0:
            #     ip += 5 + val
            # else:
            #     ip += 5
            ip += 5
            asm += """\
    pop eax;
    cmp eax, 0;
    jnz label_{};
""".format(ip+val)
        elif opcode[ip] == 17:      # sp += imm
            val = struct.unpack("<i", bytes(opcode)[ip+1:ip+5])[0]
            ip += 5
            asm += """\
    sub esp, {};
""".format(val*4)
        elif opcode[ip] == 18:      # ret
            val = struct.unpack("<i", bytes(opcode)[ip+1:ip+5])[0]
            ip += 5
            asm += """\
    mov eax, {};
    retn;
""".format(val)
        else:
            ip += 1

    fp = open(save_filename, 'w')
    fp.write("section .text\n")
    fp.write("bits 32\n")
    fp.write(asm)
    fp.close()

vm2asm(opcode_5280, 'opcode_5280.asm')
vm2asm(opcode_5020, 'opcode_5020.asm')