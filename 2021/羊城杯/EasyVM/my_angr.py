import angr
import claripy

p = angr.Project('EasyVM', support_selfmodifying_code = True)

flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(44)]
flag = claripy.Concat(*flag_chars + [claripy.BVV(b'\n')])

st = p.factory.full_init_state(
    args = ['./EasyVM'],
    add_options = angr.options.unicorn,
    stdin = flag,
)

for k in flag_chars:
    st.solver.add(k > 0x2e)
    st.solver.add(k < 0x7e)

sm = p.factory.simulation_manager(st)
sm.explore(find = 0x8048f40)

if sm.found:
    print(sm.found[0].solver.eval(flag, cast_to = bytes))