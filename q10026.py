import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
picture=[[" " for _ in range(n)] for _ in range(n)]
checked = [[-1 for _ in range(n)] for _ in range(n)]
checked2 = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = sys.stdin.readline()
    for j in range(n):
        picture[i][j] = temp[j]

posx = [1,0,-1,0]
posy = [0,1,0,-1]
def dfs(x,y):
    if checked[x][y]!=-1:
        return False
    checked[x][y] = 0
    temp = picture[x][y]
    for i in range(4):
        nx,ny = x+posx[i],y+posy[i]
        if (0<=nx<n and 0<=ny<n) and temp == picture[nx][ny]:
            dfs(nx,ny)
    return True

def dfs2(x,y):
    if checked2[x][y]!=-1:
        return False
    checked2[x][y] = 0
    temp = picture[x][y] == "B"
    for i in range(4):
        nx,ny = x+posx[i],y+posy[i]
        if (0<=nx<n and 0<=ny<n):
            if temp and picture[nx][ny]=="B":
                dfs2(nx,ny)
            elif not temp and not picture[nx][ny]=="B":
                dfs2(nx,ny)
    return True

count=0
count2=0
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            count+=1
        if dfs2(i,j):
            count2+=1
print(count, count2)