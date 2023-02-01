import sys

def findratio_1193():
    num = int(sys.stdin.readline())
    i = 0
    sum = 0
    while(sum<num):
        i += 1 #n번째 줄
        sum += i
    
    find = num-sum+i
    if(i%2!=0):
        print("{}/{}".format(i+1-find, find))
    else:
        print("{}/{}".format(find, i+1-find))
            
findratio_1193()