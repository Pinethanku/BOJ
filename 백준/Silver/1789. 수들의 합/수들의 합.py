import sys

def naturalsum_1789():
    num = int(sys.stdin.readline())
    i = 0
    sum = 0
    while(sum<=num):
        i += 1
        sum += i

    print(i-1)
            
naturalsum_1789()