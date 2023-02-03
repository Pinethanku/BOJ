import heapq
import sys

def minheap_1927():
    times = int(sys.stdin.readline())
    minheap = []
    for i in range(times) :
        calcul = int(sys.stdin.readline())
        if calcul==0:
            if minheap:
                print(heapq.heappop(minheap))
            else:
                print(0)
        else:
            heapq.heappush(minheap, calcul)
    return 0
        
minheap_1927()