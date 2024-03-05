import sys
N, r, c = map(int, sys.stdin.readline().split())
result = 0
for i in range(N):
    result+=(4**i * (((r//2**i)%2)*2 + ((c//2**i)%2)))
print(result)