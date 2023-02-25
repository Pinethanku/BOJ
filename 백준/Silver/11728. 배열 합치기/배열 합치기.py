import sys

def main_11728():
    N, M = (map(int, sys.stdin.readline().split()))
    result = []
    for i in range(2):
        result.extend(list(map(int, sys.stdin.readline().split())))
    result.sort()
    
    for re in result:
        print(re, end=" ")
    
    
if __name__=='__main__':
    main_11728()