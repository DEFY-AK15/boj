import sys
n= int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().rstrip().split()))
line.sort()
sum=line[0]
for i in range(1,n):
    line[i]+=line[i-1]
    sum+=line[i]
print(sum)