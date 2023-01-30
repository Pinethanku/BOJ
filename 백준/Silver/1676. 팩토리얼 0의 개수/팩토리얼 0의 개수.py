import sys
import math

def facto_1676():
    num = int(sys.stdin.readline())
    num = math.factorial(num)
    
    result = 0
    while(not num%10):
        result += 1
        num = num//10
    
    print(result)
    return 0
    
facto_1676()