import sys
n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
tree[int(sys.stdin.readline())] = -2
is_leaf = [0 for _ in range(n)]

def dfs(i):
    if tree[i]==-2:
        return False
    elif tree[i]==-1:
        return True
    else:
        is_leaf[tree[i]]-=n
        return dfs(tree[i])

for i in range(n):
    if dfs(i):
        is_leaf[i]+=1

count = 0
for i in range(n):
    if is_leaf[i]>0:
        count+=1
print(count)