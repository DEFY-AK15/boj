import sys
sys.setrecursionlimit(100001)
n = int(sys.stdin.readline())
table = [0 for _ in range(n)]
for i in range(n):
    table[i] = tuple(map(int, sys.stdin.readline().split()))

table.sort()

count = 1
min_time = table[0][1]
for i in range(1,n):
    if min_time > table[i][0]: #안이어짐, 갱신가능성
        min_time = min(min_time, table[i][1])
    else: #이어짐
        count+=1
        min_time = table[i][1]
print(count)