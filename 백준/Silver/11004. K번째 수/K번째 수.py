import sys

def main_11004():
    N, K = (map(int, sys.stdin.readline().split()))
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    print(data[K-1])
    
    
if __name__=="__main__":
    main_11004()