import sys
from collections import deque
N, M , R = map(int, sys.stdin.readline().split())
v = [[] for _ in range(N+1)]
result = [0 for _ in range(N)]
q  = deque()
count=1

for _ in range(M):
    temp1, temp2 = map(int, sys.stdin.readline().split())
    v[temp1].append(temp2)
    v[temp2].append(temp1)

q.append(R)
while q:
    i = q.popleft()
    if result[i-1]!=0:
        continue
    result[i-1]=count
    count+=1
    v[i].sort(reverse=True)
    for j in v[i]:
        if result[j-1]!=0:
            continue
        q.append(j)

for i in result:
    print(i)