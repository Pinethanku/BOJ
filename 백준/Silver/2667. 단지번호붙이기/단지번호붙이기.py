import sys

global save
global num
global dangi
global indangi

sys.setrecursionlimit(10**6)  #파이썬의 최대 재귀 깊이를 높임

def search(n, m) :
    global save
    global num
    global dangi
    global indangi
    
    save[n][m] = dangi
    if m<num-1 and save[n][m+1] == '1' :  #right
        search(n,m+1)
        indangi += 1
    if m>0 and save[n][m-1] == '1' : #left
        search(n,m-1)
        indangi += 1
    if n<num-1 and save[n+1][m] == '1' : #down
        search(n+1,m)
        indangi += 1
    if n>0 and save[n-1][m] == '1' : #up
        search(n-1,m)
        indangi += 1
    
    return 0

def dangi_2667():
    global save
    global num
    global dangi
    global indangi
    num = int(sys.stdin.readline())
    result = []
    save = []
    for i in range(num):
        save.append(list(sys.stdin.readline().strip()))
    
    dangi = 0
    indangi = 1
    
    for i in range(num) :
        for k in range(num) :
            if save[i][k] == '1':
                dangi += 1
                search(i, k)
                result.append(indangi)
                indangi = 1
    print(dangi)
    result.sort()
    for re in result:
        print(re)            
    return 0

dangi_2667()