import sys

def main_10876() -> None:
    lenth = int(sys.stdin.readline())
    data = list(set((map(int, sys.stdin.readline().split()))))
    data.sort()
    for d in data:
        print(d, end=" ")

if __name__=="__main__":
    main_10876()