import sys

def bomul_1026():
    N = int(sys.stdin.readline())
    A_list = list(map(int, sys.stdin.readline().split()))
    B_list = list(map(int, sys.stdin.readline().split()))
    
    A_list.sort(reverse=True)
    B_list.sort()
    
    total = 0
    
    for i in range(N):
        total += A_list[i]*B_list[i]
    
    print(total)
    
if __name__ == '__main__':
    bomul_1026()
    