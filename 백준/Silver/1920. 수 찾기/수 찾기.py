import sys

def find_1920() :
    sys.stdin.readline()
    numlist = list(map(int, sys.stdin.readline().split()))
    dic = {}
    for nums in numlist:
        dic[nums] = 1
    
    sys.stdin.readline()
    find_list = list(map(int, sys.stdin.readline().split()))
    for find in find_list:
        try:
            if dic[find]:
                print(1)
        except:
            print(0)

find_1920()