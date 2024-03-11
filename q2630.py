import sys
N = int(sys.stdin.readline())
paper = [[0 for _ in range(N)]for _ in range(N)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        paper[i][j] = temp[j]

count = [0,0] #[0] while /[1] blue
def sol(r,c,size):
    is_squr = True
    temp = paper[r][c]
    for i in range(size):
        for j in range(size):
            if paper[r+i][c+j] != temp:
                is_squr = False
                break
        if not is_squr:
            break

    if is_squr:
        global count
        count[temp]+=1
    else:
        for k in range(4):
            sol(r+((k//2)*size//2),c+((k%2)*size//2),size//2)
sol(0,0,N)
for i in count:
    print(i)