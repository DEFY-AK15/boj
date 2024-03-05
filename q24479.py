import sys
sys.setrecursionlimit(10**7)
N, M , R = map(int, sys.stdin.readline().split())
v = [[] for _ in range(N+1)]

for _ in range(M):
    temp1, temp2 = map(int, sys.stdin.readline().split())
    v[temp1].append(temp2)
    v[temp2].append(temp1)

count = 2
result = [0 for _ in range(N)]
result[R-1]=1

def dfs(now):
    global count
    v[now].sort(reverse=True)
    for i in v[now]:
        if result[i-1] == 0:
            result[i-1] = count
            count+=1
            dfs(i)

dfs(R)
for i in result:
    print(i)