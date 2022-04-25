import subprocess

def oracle(v):
  p = subprocess.Popen(f"./the_magic_oracle_above.sh {v}", stdout = subprocess.PIPE, shell = True)
  output, _ = p.communicate()
  return int(output.strip().decode())

ans = ['*'] * 32
for i in range(31, -1, -1):
  for c in '_{}@0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
    ans[i] = c
    flag = ''.join(ans)
    if oracle(flag) == 32 - i:
      print(flag)
      break

print(flag)