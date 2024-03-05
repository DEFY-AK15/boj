import sys
T = int(sys.stdin.readline())
for _ in range(T):
    func = sys.stdin.readline()
    n = int(sys.stdin.readline())
    temp = sys.stdin.readline()[1:-2]
    if temp:
        arr = list(temp.split(","))
    else:
        arr = []
    d = [0,0]
    index = 0
    for i in range(len(func)):
        if func[i]=="D":
            d[index]+=1
        elif func[i] == "R":
            index+=1
            index%=2
    temp = arr[d[0]:len(arr)-d[1]]

    if not temp or (len(arr)-d[1]<0):
        if d[0]+d[1] == n:
            print("[]")
        else:
            print("error")
    else:
        if index == 0:
            print(f'[{",".join(temp)}]')
        else:
            print(f'[{",".join(temp[::-1])}]')
