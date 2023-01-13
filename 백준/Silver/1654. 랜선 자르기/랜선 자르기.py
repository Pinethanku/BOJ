import sys

def lan_1654():
    lan_ori, aim = (map(int, sys.stdin.readline().split()))  #기존 랜선, 목표 개수
    lans = []
    for i in range(lan_ori):
        lans.append(int(sys.stdin.readline()))
    
    high = max(lans)
    if aim == 1:
        print(high)
        return 0
    
    lo = 1
    lansum = 0
    mid = (lo + high)//2
    while(lo<=high) :
        lansum = 0
        if mid==0:
            mid=1
        for lan in lans:  #랜선 개수 계산
            lansum += lan//mid
        if lansum < aim :
            high = mid-1
        else :
            lo = mid+1
        mid = (lo + high)//2
    print(mid)
    return 0

lan_1654()
