import sys

def LCS_9251() :
    x = sys.stdin.readline().strip()
    y = sys.stdin.readline().strip()
    
    graph = [[0 for i in range(len(x)+1)] for k in range(len(y)+1)]
    
    for i in range(1, len(y)+1):
        for k in range(1, len(x)+1) :
            if y[i-1] == x[k-1] :
                graph[i][k] = max(graph[i][k-1], graph[i-1][k], graph[i-1][k-1]+1)
            else:
                graph[i][k] = max(graph[i][k-1], graph[i-1][k])

    print(graph[-1][-1])
    return 0
    
LCS_9251()