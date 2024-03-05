import sys
import re
string = sys.stdin.readline()
number = list(map(int, re.split(r'[+-]',string.strip())))
oper = list(re.sub(r'[0-9]',"",string.strip()))

result = number[0]
sign = 1
opened = 0
for i in range(len(oper)):
    if oper[i] == "+":
        if not opened:
            opened += 1
            opened %= 2
            sign = 1
    elif oper[i] == "-":
        if not opened:
            opened += 1
            opened %= 2
        sign = -1
    result += number[i+1] * sign
print(result)