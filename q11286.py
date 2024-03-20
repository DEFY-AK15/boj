import sys
n = int(sys.stdin.readline())
abs_heap = [0 for _ in range(n+1)]
index = 1

def insert(num):
    global index
    abs_heap[index] = num
    up_sort(index)
    index+=1

def pop():
    global index
    index-=1
    temp = abs_heap[1]
    abs_heap[1] = abs_heap[index]
    down_sort(1)
    return temp

def is_small(x,y):
    if x+y == 0:
        return x<y
    return abs(x) < abs(y)

def up_sort(i):
    if i==1: return
    if is_small(abs_heap[i],abs_heap[i//2]):
        abs_heap[i],abs_heap[i//2] = abs_heap[i//2],abs_heap[i]
        up_sort(i//2)

def down_sort(i):
    temp = abs_heap[i]
    index = 0
    for j in range(2):
        if i**2+j < index:
            if is_small(abs_heap[i**2+j],temp):
                index = i**2+j
                temp = abs_heap[i**2+j]
    if index:
        abs_heap[i],abs_heap[index] = abs_heap[index],abs_heap[i]
        down_sort(index)
    