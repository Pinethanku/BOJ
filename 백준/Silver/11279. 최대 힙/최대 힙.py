import heapq, sys

def main_maxheap() -> None:
    times = int(sys.stdin.readline())
    maxheap = []
    for i in range(times):
        num = int(sys.stdin.readline())
        if num :
            heapq.heappush(maxheap, -num)
        else:
            if maxheap:
                print(-heapq.heappop(maxheap))
            else:
                print(0)
    
if __name__ == '__main__':
    main_maxheap()