import sys
from collections import deque
sys.setrecursionlimit(2**15)
n, k = map(int, sys.stdin.readline().split())
dp = [-1 for _ in range(100001)]

q = deque()
q.append([n,0])
while q:
    num, count = q.popleft()
    dp[num] = count
    if num == k:
        break
    if num-1 >= 0 and dp[num-1] == -1:
        q.append([num-1,count+1])
    if num+1 <= 100000 and dp[num+1] == -1:
        q.append([num+1,count+1])
    if num*2 <= 100000 and dp[num*2] == -1:
        q.append([num*2,count+1])

print(dp[k])