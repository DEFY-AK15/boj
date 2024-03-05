import sys
fibo = [-1 for _ in range(41)]
fibo[0] = 0
fibo[1] = 1
fibo[2] = 1
def f(n:int):
    if n==-1:
        return 1
    elif n<3:
        return fibo[n]
    else:
        if fibo[n-1] == -1:
            fibo[n-1] = f(n-1)
        if fibo[n-2] == -1:
            fibo[n-2] = f(n-2)
        return fibo[n-1] + fibo[n-2]
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(f(n-1), f(n))