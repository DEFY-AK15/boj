import sys
sys.setrecursionlimit(100001)
n = int(sys.stdin.readline())
table = [0 for _ in range(n)]
count = [0 for _ in range(n)]
for i in range(n):
    table[i] = tuple(map(int, sys.stdin.readline().split()))

table.sort()

count=-1
end_time = 0
start_index = 0
find = True
while find:
    count+=1
    temp = 2**31
    find = False
    for i in range(start_index, n):
        if end_time<=table[i][0] and table[i][1]<temp:
            start_index = i+1
            end_time = table[i][1]
            temp = table[i][1]
            find = True
print(count)