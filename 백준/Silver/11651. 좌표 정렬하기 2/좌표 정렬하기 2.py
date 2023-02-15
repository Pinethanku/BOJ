import sys

def main_11651():
    times = int(sys.stdin.readline())
    cordi = []
    for i in range(times):
        temp = list(map(int, sys.stdin.readline().split()))
        cordi.append(temp)
    cordi.sort(key=lambda x: (x[1], x[0]))
    for cor in cordi:
        print(cor[0], cor[1])
    
if __name__ == "__main__":
    main_11651()