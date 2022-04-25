import angr

def to_little(val):
    little_hex = bytearray.fromhex(val)
    little_hex.reverse()

    str_little = ''.join(format(x, '02x') for x in little_hex)

    return str_little

def basic_symbolic_execution():
    p = angr.Project('./optimized')

    start_addr = 0x400969
    init_state = p.factory.blank_state(addr = start_addr)

    init_state.regs.rsp -= 0x130

    pass1 = init_state.solver.BVS('pass1', 32)
    pass2 = init_state.solver.BVS('pass2', 32)
    pass3 = init_state.solver.BVS('pass3', 32)
    pass4 = init_state.solver.BVS('pass4', 32)

    init_state.memory.store(init_state.regs.rsp + 0x10, pass1)
    init_state.memory.store(init_state.regs.rsp + 0x14, pass2)
    init_state.memory.store(init_state.regs.rsp + 0x18, pass3)
    init_state.memory.store(init_state.regs.rsp + 0x1c, pass4)

    sm = p.factory.simulation_manager(init_state)

    def is_bad(state):
        return (b'Wrong!' in state.posix.dumps(1)) or (b'Bad format!' in state.posix.dumps(1))

    sm.explore(find = 0x400b5d, avoid = is_bad)

    if sm.found:
        found_state = sm.found[0]
        password1 = found_state.solver.eval(pass1)
        password2 = found_state.solver.eval(pass2)
        password3 = found_state.solver.eval(pass3)
        password4 = found_state.solver.eval(pass4)

        print(password1)
        print(password2)
        print(password3)
        print(password4)
        print(int(to_little(hex(password1)[2:]), 16))
        print(int(to_little(hex(password2)[2:]), 16))
        print(int(to_little(hex(password3)[2:]), 16))
        print(int(to_little(hex(password4)[2:]), 16))
    else:
        print('not found')

basic_symbolic_execution()