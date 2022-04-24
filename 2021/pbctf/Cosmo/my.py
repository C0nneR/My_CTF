import angr
import claripy

p = angr.Project('./hello.com')
f = p.factory

start_addr = 0x40308a
state = f.blank_state(addr =start_addr, add_options = angr.options.unicorn)

flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(38)]
flag = claripy.Concat(*flag_chars + [claripy.BVV(b'\n')])

state.regs.r12 = state.regs.rsi
state.memory.store(state.regs.rsi + 0x8, 0x777000110023, endness = p.arch.memory_endness)
state.memory.store(0x777000110023, flag)

for k in flag_chars:
    state.solver.add(k > 0x2e)
    state.solver.add(k < 0x7e)

sm = f.simulation_manager(state)
sm.explore(find = 0x4030d8, avoid = 0x403115)

if sm.found:
    print(sm.found[0].solver.eval(flag, cast_to = bytes))
else:
    print('not found')