import sys

def readints():
    return map(int, sys.stdin.readline().split())

def readint():
    return int(sys.stdin.readline().strip())

N, M = readints()
cds = range(N+1)   # cd => case
listen = [readint() for _ in xrange(M)]
current = 0

for cd in listen:
    cds[current] = cds[cd]
    cds[cd] = 0
    current = cd

cd_case = sorted(enumerate(cds), key=lambda x: x[1])
for cd, case in cd_case[1:]:
    print cd
