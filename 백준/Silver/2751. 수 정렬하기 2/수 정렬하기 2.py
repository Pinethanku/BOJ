import sys

num = int(sys.stdin.readline())
re = []

for i in range(num) :
    re.append(int(sys.stdin.readline()))

re.sort()

for r in re:
    print(r)