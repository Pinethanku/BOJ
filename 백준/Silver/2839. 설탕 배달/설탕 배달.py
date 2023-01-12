import sys

def suga_2839():
    
    kg = int(sys.stdin.readline())

    setfive = kg//5
    remain = kg%5

    while(remain<=kg) :
        if remain % 3 == 0 :
            print(setfive+(remain//3))
            return 0
        else :
            remain += 5
            setfive -= 1

    print(-1)
    return 0

suga_2839()