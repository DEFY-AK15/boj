import sys
N = int(sys.stdin.readline())
result = [["*" for _ in range(N)] for _ in range(N)]
def er(n):
    if n==1:
        return
    for i in range(n//3):
        for j in range(n//3):
            er2(i+n//3,j+n//3,n)
    er(n//3)

def er2(r,c,n):
    #result[r][c]=" "
    for i in range(0,N,n):
        for j in range(0,N,n):
            result[r+i][c+j]=" "
er(N)

for i in range(N):
    for j in range(N):
        print(result[i][j],end="")
    print()