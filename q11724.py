import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N)] for _ in range(N)]
checked = [0 for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x:int(x)-1, sys.stdin.readline().rstrip().split())
    graph[i][j] = 1
    graph[j][i] = 1

count = 0
q = deque()
for i in range(N):
    if checked[i] == 1:
        continue
    q.append(i)
    while q:
        j = q.popleft()
        checked[j] = 1
        for k in range(N):
            if graph[j][k] == 1 and checked[k] == 0:
                checked[k] = 1
                q.append(k)
    count+=1

print(count)