import sys
sq_arr = [(i+1)**2 for i in range(223)]
sq_arr_2 = [[0 for _ in range(223)] for _ in range(223)]
n = int(sys.stdin.readline())
def sol():
    for i in range(223):
        if n==sq_arr[i]:
            return 1
    for i in range(223):
        for j in range(i,223):
            temp = sq_arr[i] + sq_arr[j]
            if temp == n:
                return 2
            sq_arr_2[i][j] = temp

    for i in range(223):
        for j in range(i, 223):
            for k in range(j,223):
                if sq_arr_2[i][j]+sq_arr[k] == n:
                    return 3
    return 4
print(sol())
