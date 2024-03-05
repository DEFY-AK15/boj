import sys

def sum(start:int, end:int):

    if memo[start][end]!=0:
            return memo[start][end], memo[end][start]
        
    if end == start:
            return files[start], files[start]
        
    else:
        temp = []
        for i in range(end-start):
            temp1, temp1_acc = sum(start,end-i-1)
            temp2, temp2_acc = sum(end-i,end)
            temp.append(temp1_acc+temp2_acc)
            
        memo[start][end] = temp1+temp2
        memo[end][start] = min(temp)+memo[start][end]
        return memo[start][end], memo[end][start]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    memo = [[0 for _ in range(n)] for _ in range(n)]
    files = list(map(int, sys.stdin.readline().split()))
    r1, r2 = sum(0,n-1)
    print(r2-r1)