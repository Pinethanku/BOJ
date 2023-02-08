import sys

def dedbojob_1764() :
    ded, bo = tuple(map(int, sys.stdin.readline().split()))
    diction = {}
    result = []
    for i in range(ded) :
        diction[sys.stdin.readline().strip()] = 1
    for i in range(bo) :
        name = sys.stdin.readline().strip()
        try: 
            if diction[name]:
                result.append(name)
        except:
            continue
    
    result.sort()
    print(len(result))
    for re in result:
        print(re)
        
dedbojob_1764()