import sys
sys.setrecursionlimit(2**31 -1)
n, k = map(int, sys.stdin.readline().split())
c=0
is_small = True
def findmin(n,k):
    global c
    global is_small
    temp = n
    count = 0
    while True:
        if abs(k-temp) < abs(k-temp*2):
            break
        temp*=2
        count+=1
    if temp < k:
        c+=1
        is_small = True
        return False
    elif temp > k:
        c+=1
        is_small = False
        return False
    else:
        c+=count
        return True
    
while True:
    if findmin(n,k):
        print(c)
        break
    else:
        if is_small:
            n+=1
        else:
            n-=1