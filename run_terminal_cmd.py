import subprocess
s = subprocess.getstatusoutput('ls -l')
if s[0] == 0:
    print(s[1])
else:
    print('Custom Error {}'.format(s[1]))
# call(["ls", "-l"])