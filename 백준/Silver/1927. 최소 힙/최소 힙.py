import heapq
import sys

def minheap_1927():
    times = int(sys.stdin.readline())
    minheap = []
    result = []
    for i in range(times) :
        calcul = int(sys.stdin.readline())
        if calcul==0:
            if minheap:
                result.append(heapq.heappop(minheap))
            else:
                result.append(0)
        else:
            heapq.heappush(minheap, calcul)
    
    for re in result:
        print(re)
        
minheap_1927()