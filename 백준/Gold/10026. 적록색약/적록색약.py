import sys
global pic
global save
global num
global no_glory

sys.setrecursionlimit(10**6)

def search(n, m) :
    global pic
    global save
    global num
    global no_glory
    
    save[n][m] = no_glory
    if m<num-1 and save[n][m+1] == 0 and pic[n][m+1] == pic[n][m] :  #right
        search(n,m+1)
    if m>0 and save[n][m-1] == 0 and pic[n][m-1] == pic[n][m] : #left
        search(n,m-1)
    if n<num-1 and save[n+1][m] == 0 and pic[n+1][m] == pic[n][m] : #down
        search(n+1,m)
    if n>0 and save[n-1][m] == 0 and pic[n-1][m] == pic[n][m] : #up
        search(n-1,m)
    return 0

def theglory_10026():
    global pic
    global save
    global num
    global no_glory
    num = int(sys.stdin.readline())
    pic = []
    save = [[0 for i in range(num)] for i in range(num)]
    for i in range(num):
        pic.append(list(sys.stdin.readline().strip()))
        
    if num==1:
        print("1 1")
        return 0
    
    no_glory = 0
    
    for i in range(num) :
        for k in range(num) :
            if save[i][k] == 0:
                no_glory += 1
                search(i, k)
    print(no_glory, end=" ")
    
    for i in range(num) :
        for k in range(num) :
            save[i][k] = 0
            if pic[i][k]=='R':
                pic[i][k] = 'G'
                
    no_glory=0
    for i in range(num) :
        for k in range(num) :
            if save[i][k] == 0:
                no_glory += 1
                search(i, k)
    print(no_glory)
    return 0

theglory_10026()