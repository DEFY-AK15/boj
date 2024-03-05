import sys
from collections import deque
N, M , V = map(int, sys.stdin.readline().split())
v = [[] for _ in range(N)]

for _ in range(M):
    temp1, temp2 = map(int, sys.stdin.readline().split())
    v[temp1-1].append(temp2-1)
    v[temp2-1].append(temp1-1)

arr = deque()

check = [0 for _ in range(N)]
result = ""
arr.append(V-1)
while arr:
    i = arr.pop()
    if check[i]:
        continue
    check[i] = 1
    result+=str(i+1)+" "
    v[i].sort(reverse=True)
    for j in v[i]:
        arr.append(j)
print(result[:-1])

check = [0 for _ in range(N)]
result = ""
arr.append(V-1)
while arr:
    i = arr.popleft()
    if check[i]:
        continue
    check[i] = 1
    result+=str(i+1)+" "
    v[i].sort()
    for j in v[i]:
        arr.append(j)
print(result[:-1])