import sys

def sort_11931():
    num = int(sys.stdin.readline())
    resul = []
    for i in range(num) :
        resul.append(int(sys.stdin.readline()))
    resul.sort(reverse=True)
    
    for re in resul:
        print(re)
    
sort_11931()