import sys
a = [0 for _ in range(20)]
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().rsplit()
    if command[0] == "all":
        for i in range(20):
            a[i] = 1
    elif command[0] == "empty":
        for i in range(20):
            a[i] = 0
    else:
        x = int(command[1])-1
        if command[0] == "add":
            if not a[x]:
                a[x] = 1
        elif command[0] == "remove":
            if a[x]:
                a[x] = 0
        elif command[0] == "check":
            print(a[x])
        elif command[0] == "toggle":
            if a[x]:
                a[x] = 0
            else:
                a[x] = 1