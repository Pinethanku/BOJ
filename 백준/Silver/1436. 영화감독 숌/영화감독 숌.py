import sys
def setname(num):
    count=0
    i=666
    while True:
        stri = str(i)
        if "666" in stri:
            count += 1
            if count==num:
                return i
        i += 1

N = int(sys.stdin.readline())
print(setname(N))
