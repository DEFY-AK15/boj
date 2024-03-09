import sys
N = int(sys.stdin.readline())
paper = [[0 for _ in range(N)]for _ in range(N)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        paper[i][j] = temp[j]

def is_squr(start_index, size):
    pass