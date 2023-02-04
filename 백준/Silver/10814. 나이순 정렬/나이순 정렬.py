import sys

def sort_1181():
    times = int(sys.stdin.readline())
    if times==1:
        print(sys.stdin.readline())
        return 0
    
    mem = []
    for i in range(times):
        temp = list(sys.stdin.readline().split())
        mem.append([int(temp[0]), temp[1]])

    mem.sort(key=lambda x:x[0])
    for me in mem:
        print(me[0],me[1])
    return 0
    
sort_1181()