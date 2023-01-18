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
    nums = list(map(int, sys.stdin.readline().split()))
    
    total = 0
    for nu in nums :
        if isPrime(nu) :
            total += 1
    print(total)
    return 0
    
prime_1929()