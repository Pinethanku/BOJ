import sys

times = int(sys.stdin.readline())

for i in range(times):
    A , B = map(int, sys.stdin.readline().split())
    print(A+B)