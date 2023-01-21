import sys

def sort_1427():
    num = list(sys.stdin.readline().strip())
    num.sort(reverse=True)
    
    for n in num:
        print(n, end="")
    return 0

sort_1427()