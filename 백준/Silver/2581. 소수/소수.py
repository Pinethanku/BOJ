import sys
from unittest import result

def isPrime(n) :
    if(n<2) :
        return 0
    i = 2
    while((i*i) <= n):
        if n%i==0 :
            return 0
        i+=1
    return 1

def prime_2581():
    start = int(sys.stdin.readline())
    end = int(sys.stdin.readline())
    result = []
    
    for i in range(start, end+1) :
        if isPrime(i) :
            result.append(i)
    
    if result :
        print(sum(result))
        print(result[0])
        
    else:
        print(-1)
    return 0
    
prime_2581()
