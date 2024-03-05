import sys
sys.setrecursionlimit(250000)
m, n = map(int, sys.stdin.readline().split())
mapp = [list(map(int, sys.stdin.readline().split()))for _ in range(m)]
checked = [[-1 for _ in range(n)]for _ in range(m)]
nx = [1,0,-1,0]
ny = [0,-1,0,1]
max=0
checked[-1][-1]=1

def dfs(x,y):
    if (x==m-1 and y==n-1) or checked[x][y]!=-1:
       return
    checked[x][y] = 0
    temp = mapp[x][y]
    for i in range(4):
      px = x+nx[i]
      py = y+ny[i]
      if 0<=px<m and 0<=py<n:
          if mapp[px][py] < temp:
            dfs(px,py)
            checked[x][y] += checked[px][py]

dfs(0,0)
print(checked[0][0])