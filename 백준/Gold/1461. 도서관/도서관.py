import sys

def lib_1461():
    books, handle = (map(int, sys.stdin.readline().split()))
    loc = list(map(int, sys.stdin.readline().split()))
    
    if books==1:
        print(loc[0])
        return 0

    loc.sort()
    #print(loc)
    i = 0
    
    while( i < len(loc) and loc[i]<0) :
        i += 1
        
    neloc = loc[0:i]
    loc = loc[i:]
    #print(neloc)
    #print(loc)
    i=len(loc)-1
    nei = 0
    
    sum = 0
    if neloc and loc and neloc[0] + loc[-1] < 0 : #음수 절댓값 최대가 양수 최대보다 큰 경우
        sum += neloc[0]*(-1)
        nei = handle
        
    elif loc :
        sum += loc[-1]
        i = len(loc)-handle-1
    
    elif neloc :
        sum += neloc[0]*(-1)
        nei = handle
        
    while(nei<len(neloc)) :
        #print(neloc[nei])
        sum += neloc[nei]*(-2)
        nei += handle
    
    while(i>=0) :
        #print(loc[i])
        sum += loc[i]*(2)
        i -= handle
    
    print(sum)            
    
lib_1461()