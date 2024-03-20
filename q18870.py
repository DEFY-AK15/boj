import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
index_arr_input = [i for i in range(n)]
result = [-1 for i in range(n)]
def quick_sort(index_arr):
    def sort(i,j):
        if i>=j:
            return
        m=partition(i,j)
        sort(i,m-1)
        sort(m,j)
    def partition(i,j):
        pivot = arr[index_arr[(i+j)//2]]
        while i<=j:
            while arr[index_arr[i]] < pivot:
                i+=1
            while pivot < arr[index_arr[j]]:
                j-=1
            if i<=j:
                index_arr[i],index_arr[j]=index_arr[j],index_arr[i]
                i+=1
                j-=1
        return i
    sort(0, len(index_arr)-1)
    return index_arr

index_arr_input = quick_sort(index_arr_input)

result[index_arr_input[0]] = 0

j=0
temp=arr[index_arr_input[0]]
for i in range(1,n):
    if arr[index_arr_input[i]] == temp:
        j+=1
    else:
        temp = arr[index_arr_input[i]]
    result[index_arr_input[i]] = i-j

print(" ".join(map(str,result)))