import sys

def main_14916() -> int:
    
    trg = int(sys.stdin.readline())

    setfive = trg//5
    remain = trg%5

    while(remain<=trg) :
        if remain % 2 == 0 :
            print(setfive+(remain//2))
            return 0
        else :
            remain += 5
            setfive -= 1

    print(-1)
    return 0

if __name__ == "__main__":
    main_14916()