import sys
n1,n2 = map(int,sys.stdin.readline().split())
print("==" if n1==n2 else "<" if n1<n2 else ">")