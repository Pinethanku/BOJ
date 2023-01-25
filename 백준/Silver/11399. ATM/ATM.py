import sys

def ATM_11399():
    people = int(sys.stdin.readline())
    peoplelist = list(map(int, sys.stdin.readline().split()))
    
    peoplelist.sort()
    
    total = 0
    tototal = 0
    for pp in peoplelist:
        total += pp
        tototal += total
    
    print(tototal)
    
ATM_11399()