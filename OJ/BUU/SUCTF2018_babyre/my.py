import subprocess

for key in range(65536):
    proc = subprocess.Popen(['./patch.exe'], stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    out = proc.communicate(('%d\n' % key).encode('utf-8'))[0]
    if "SUCTF{".encode('utf-8') in out:
        print('flag:', out)
        print('key:', key)
        break