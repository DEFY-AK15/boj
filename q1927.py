import sys
N = int(sys.stdin.readline())
heap = [0 for _ in range(N)]
head = 0

def sort(index):
    temp1 = heap[index]
    temp2 = heap[index//2]
    if temp1 < temp2:
        heap[index] = temp2
        heap[index//2] = temp1
        sort(index//2)

def sort_down(index):
    parent = heap[index]
    if index*2 < head:
        child1 = heap[index*2]
    else:
        child1 = 2**31
    if index*2+1 < head:
        child2 = heap[index*2+1]
    else:
        child2 = 2**31
    if parent > child1 or parent > child2:
        if child1 < child2:
            heap[index] = child1
            heap[index*2] = parent
            sort_down(index*2)
        else:
            heap[index] = child2
            heap[index*2+1] = parent
            sort_down(index*2+1)

def insert(data):
    global head
    global heap

    heap[head] = data
    sort(head)
    head+=1

def pop():
    global head
    temp = heap[0]
    head-=1
    heap[0] = heap[head]
    sort_down(0)
    return temp

for _ in range(N):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if head==0:
            print(0)
        else:
            print(pop())
    else:
        insert(temp)
