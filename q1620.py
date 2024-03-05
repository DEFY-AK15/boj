import sys
N, M = map(int, sys.stdin.readline().split())
q = ["" for _ in range(N)]
d = {}
for i in range(N):
    temp = sys.stdin.readline()
    q[i] = temp
    d[temp] = i

for _ in range(M):
    temp = sys.stdin.readline()
    try:
        temp = int(temp)
        print(q[temp-1],end="")
    except:
        print(d[temp]+1)