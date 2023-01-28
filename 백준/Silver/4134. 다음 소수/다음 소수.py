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
    times = int(sys.stdin.readline())
    result = []
    for k in range(times) :
        start = int(sys.stdin.readline())
        i=0
        while(True) :
            if isPrime(start+i) :
                result.append(start+i)
                break
            i += 1
    for re in result:
        print(re)
    
prime_2581()
