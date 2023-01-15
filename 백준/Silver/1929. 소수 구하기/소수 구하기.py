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
    start, end = (map(int, sys.stdin.readline().split()))
    if start==end:
        print(start)
        return 0
    
    for i in range(start, end+1) :
        if isPrime(i) :
            print(i)
    return 0
    
prime_1929()
