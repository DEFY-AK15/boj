import sys
import math
target = int(sys.stdin.readline())
number_len = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
result = abs(100-target)

for i in range(500000):
    digit = int(math.log10(i))+1 if i!=0 else 1
    p = False
    for j in range(digit):
        temp = i % 10**(digit-j) // 10**(digit-j-1)
        if temp in numbers:
            p=True
            break
    if p:
        continue
    result = min(result, abs(target-i)+digit)

print(result)