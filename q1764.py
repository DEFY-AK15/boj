import sys
N, M = map(int, sys.stdin.readline().split())
a = ["" for _ in range(N)]
b = ["" for _ in range(M)]
for i in range(N):
    a[i] = sys.stdin.readline().rstrip()
for i in range(M):
    b[i] = sys.stdin.readline().rstrip()
a=set(a)
b=set(b)
r = list(a&b)
r.sort()
print(len(r))
for i in r:
    print(i)