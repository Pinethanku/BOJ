import sys


def nomal_bag_12865() :
    things, weight = (map(int,sys.stdin.readline().split()))
    candis = []
    
    for i in range(things):
        candis.append(tuple(map(int,sys.stdin.readline().split())))
        
    candis.sort()
    if things==1:
        if candis[0][0]>weight:
            print(0)
            return 0
        else:
            print(candis[0][1])
            return 0
    
    graph = [[0 for i in range(weight+1)] for k in range(things+1)]
    
    for i in range(1, things+1):
        for k in range(candis[0][0], weight+1) :
            if candis[i-1][0] <= k:
                graph[i][k] = max(candis[i-1][1]+graph[i-1][k-candis[i-1][0]], graph[i-1][k])
            else:
                graph[i][k] = graph[i-1][k]

    print(graph[things][weight])
    return 0
    
        
    
nomal_bag_12865()