import sys

def isPrime(n) :
    i = 2
    while((i*i) <= n):
        if n%i==0 :
            return 0
        i+=1
    return 1

def isPal(n) :
    if n < 10:
        return 1
    else :
        strn = str(n)[::-1]
        if n==int(strn) :
            return 1
        return 0
    
def prime_1929():
    start = int(sys.stdin.readline())
    if start <= 2:
        print(2)
        return 0
    
    while(True) :
        if isPrime(start) :
            if(isPal(start)):
                print(start)
                return 0
        start += 1
    
prime_1929()