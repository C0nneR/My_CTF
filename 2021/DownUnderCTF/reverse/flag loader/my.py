from z3 import *

# found by angr
def check1():
    check_str = 'A|#&F'
    v2 = 1
    for i in range(5):
        v2 *= (i + 1) * ord(check_str[i])
    return v2 & 0xff

def check2(add_sum):
    global p
    v1 = add_sum + 0x100
    v2 = 0xffffff00
    p.sendline(str(v1))
    p.sendline(str(v2))
    return (v1 * v2) & 0xffff

def check3(check1_ret, check2_ret, add_sum):
    global p
    found_flag = False
    for i in range(60, 0x8000):
        temp = i * check1_ret * check2_ret
        if (temp & 0xffffffff) < 100:
            print(i)
            print("0x%x" % (temp & 0xffffffff))
            found_flag = True
            break

    if found_flag:
        v1, v2, v3, v4, v5 = Ints('v1 v2 v3 v4 v5')
        s = Solver()

        s.add(v1 > 0)
        s.add(v2 > 0)
        s.add(v3 > 0)
        s.add(v4 > 0)
        s.add(v5 > 0)
        s.add(v1 < v2)
        s.add(v2 < v3)
        s.add(v3 < v4)
        s.add(v4 < v5)
        s.add(v1 + v2 + v3 + v4 + v5 == add_sum)
        s.add(((v3 - v2) * (v5 - v4)) == i)
        result = {}
        if s.check() == sat:
            m = s.model()
            for i in m:
                result[str(i)] = m[i].as_long()
        print(result)

        p.sendline(str(result['v1']))
        p.sendline(str(result['v2']))
        p.sendline(str(result['v3']))
        p.sendline(str(result['v4']))
        p.sendline(str(result['v5']))
    else:
        print('not found')
        p.close()

from pwn import *

p = remote('pwn-2021.duc.tf', 31919)
data = p.recvuntil(': ')
p.sendline('A|#&F')

check1_ret = check1()

p.recvuntil('= ')
data = p.recvuntil('\n')
check2_ret = check2(int(data))

p.recvuntil('= ')
data = p.recvuntil('\n')
check3(check1_ret, check2_ret, int(data))

flag = p.recvuntil('}')
print(flag)