#DFS와 BFS
import sys
Q = []

def DFS(table, start):
    print(start, end=" ")
    table[0][start-1] = 1
    for line in table[start]:
        if(table[0][line-1]==0):
            DFS(table, line)
    return 0   

def BFS(table, start):
    while(len(Q)):
        start = Q[0]
        del Q[0]
        table[0][start-1] = 1
        print(start, end=" ")
        for line in table[start]:
            if(table[0][line-1]==0):
                Q.append(line)
                table[0][line-1]=1
    return 0
        

dot, line, first = map(int, input().split())
table = [[] for row in range(dot+1)]
table[0] = list(0 for i in range(dot))
Q.append(first)

for i in range(line):
    s, e = map(int, sys.stdin.readline().split())
    table[s].append(e)
    table[e].append(s)
    table[s].sort()
    table[e].sort()

DFS(table, first)
table[0] = list(0 for i in range(dot))
print("")
BFS(table, first)