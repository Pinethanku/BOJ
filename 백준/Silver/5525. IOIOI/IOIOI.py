import sys

def main_IOI() -> None:
    NofP = int(sys.stdin.readline())
    lenth = int(sys.stdin.readline())
    
    Plenth = NofP*2 + 1
    total = 0
    readIOI = list(sys.stdin.readline().strip("O""\n").replace("II","I I").replace("OO", " ").split(" "))
    for ioi in readIOI:
        if len(ioi)>Plenth:
            total += (len(ioi) - Plenth)//2 + 1
        elif len(ioi) == Plenth:
            total += 1
    print(total)
    
    
if __name__ == '__main__':
    main_IOI()