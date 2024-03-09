import sys
from collections import deque
n = int(sys.stdin.readline())
v = int(sys.stdin.readline())
network = [[0 for _ in range(n)]for _ in range(n)]
checked = [0 for _ in range(n)]
for _ in range(v):
    temp1, temp2 = map(lambda x:int(x)-1, sys.stdin.readline().rstrip().split())
    network[temp1][temp2] = 1
    network[temp2][temp1] = 1

q = deque()
q.append(0)
checked[0] = 1
count = -1
while q:
    count+=1
    i = q.popleft()
    for j in range(n):
        if network[i][j] == 1 and checked[j] == 0:
            q.append(j)
            checked[j] = 1
print(count)