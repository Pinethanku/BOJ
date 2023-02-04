import sys

def isPrime(n) :
    if(n<2) :
        return 0
    i = 2
    while((i*i) <= n):
        if n%i==0 :
            return 0
        i+=1
    return 1

def prime_1929():
    num = int(sys.stdin.readline())
    if num == 1:
        print(2)
        return 0
    
    total = 1
    start = 2
    while(total<num) :
        start+=1
        if isPrime(start) :
            total += 1
    print(start)
    return 0
    
prime_1929()