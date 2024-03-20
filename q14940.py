import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
Map = [[0 for _ in range(m)]for _ in range(n)]
distanceMap = [[-1 for _ in range(m)]for _ in range(n)]
q = deque()
nq = deque()
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(m):
        Map[i][j] = temp[j]
        if temp[j] == 2:
            q.append((i,j))
            distanceMap[i][j] = 0
        elif temp[j] == 0:
            distanceMap[i][j] = 0

posx = [1,0,-1,0]
posy = [0,1,0,-1]
distance = 0
while q:
    distance+=1
    while q:
        i,j = q.popleft()
        for k in range(4):
            nx, ny = posx[k]+i, posy[k]+j
            if (0<=nx<n and 0<=ny<m) and distanceMap[nx][ny]==-1 and Map[nx][ny]==1:
                distanceMap[nx][ny] = distance
                nq.append((nx,ny))
    q = nq.copy()
    nq.clear()
for i in range(n):
    print(" ".join(map(str, distanceMap[i])))