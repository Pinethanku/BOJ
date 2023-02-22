import sys

def fibonacci(n, zeroone) -> list:
    if zeroone[n] != [0,0]:
        return zeroone[n]
    else :
        if (n == 0) :
            return [1, 0]
        elif (n == 1) :
            return [0, 1]
        
        zeroone[n] = [fibonacci(n-1, zeroone)[0] + fibonacci(n-2, zeroone)[0], fibonacci(n-1, zeroone)[1] + fibonacci(n-2, zeroone)[1]]
        return zeroone[n]

def main_9625() -> None :
    zeroone = [[0,0] for i in range(46)]
    num =  int(sys.stdin.readline())
    print(fibonacci(num, zeroone)[0], fibonacci(num, zeroone)[1])
    
if __name__ == "__main__" :
    main_9625()