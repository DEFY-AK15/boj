import sys
N,M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
prefix_sum = [0 for _ in range(N+1)]

for i in range(1,N+1):
    prefix_sum[i] = arr[i-1]+prefix_sum[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[j]-prefix_sum[i-1])