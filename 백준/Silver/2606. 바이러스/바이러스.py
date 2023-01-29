import queue
import sys

def virus_2606():
    computers = int(sys.stdin.readline())
    connection = int(sys.stdin.readline())
    
    if connection == 0:
        print("0")
        return 0
    
    
    graph = [[0 for i in range(computers+1)] for i in range(computers+1)]
    queue = [1]
    
    for i in range(connection) :
        x, y = tuple(map(int, sys.stdin.readline().split()))
        graph[x][y] = 1
        graph[y][x] = 1
        
    if computers == 2:
        print(1)
        return 0
    
    total = -1
    while(queue):
        pre = queue.pop(0)
        if(graph[pre][0] == 0) :
            graph[pre][0] = 1
            total += 1
            for i in range(computers):
                if graph[pre][i+1] == 1 and graph[i+1][0] == 0:
                    queue.append(i+1)
    
    print(total)
    return 0
    
virus_2606()