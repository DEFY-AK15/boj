import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    memo = [[0 for _ in range(n)] for _ in range(n)]
    stack = [0 for _ in range(n+1)]
    files = list(map(int, sys.stdin.readline().split()))

    stack[1] = files[0]
    for i in range(2,n+1):
        stack[i] = stack[i-1]+files[i-1]

    for i in range(n-1):
        temp = files[i]+files[i+1]
        memo[i+1][i] = temp
    
    for N in range(3,n+1):
        for start in range(n-N+1):
            end = start+N-1

            min_value = 10000000000
            for k in range(N-1):
                min_value=min(min_value,memo[end-k-1][start]+memo[end][end-k])

            memo[end][start] = min_value + (stack[end+1]-stack[start])

    print(memo[-1][0])