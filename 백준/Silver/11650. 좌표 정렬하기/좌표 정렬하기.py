import sys

def sortcor_11650():
    times = int(sys.stdin.readline())
    cordi = []
    for i in range(times):
        cordi.append(list(map(int, sys.stdin.readline().split())))
    
    cordi.sort()
    for cor in cordi:
        print(cor[0], cor[1])
    
sortcor_11650()