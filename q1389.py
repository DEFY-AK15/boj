import sys
N, M = map(int, sys.stdin.readline().split())
v = [[] for _ in range(N)]
for _ in range(M):
    temp1, temp2 = map(int, sys.stdin.readline().split())
    if temp2-1 in v[temp1-1]:
        continue
    v[temp1-1].append(temp2-1)
    v[temp2-1].append(temp1-1)

def bfs(start, target):
    if start==target:
        return 0
    q = []
    nq = []
    count = 0
    check = [0 for _ in range(N)]

    q.append(start)
    while True:
        while q:
            i = q.pop()
            if check[i]:
                continue
            check[i] =1
            for j in v[i]:
                if j == target:
                    return count+1
                nq.append(j)
        if nq:
            q = nq.copy()
            count+=1
            nq=[]

temp = []
for i in range(N):
    sum = 0
    for j in range(N):
        sum+=bfs(i,j)
    temp.append(sum)
print(temp.index(min(temp))+1)