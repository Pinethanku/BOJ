import sys
from collections import Counter

def statistics_2108():
    times = int(sys.stdin.readline())
    nums = []
    for i in range(times) :
        nums.append(int(sys.stdin.readline()))
    nums.sort()
    if times==1:
        print(nums[0])
        print(nums[0])
        print(nums[0])
        print(0)
        return 0
        
    
    print(round(float(sum(nums))/times))
    print(nums[times//2])
    cnt = Counter(nums).most_common()
    most = cnt[0][1]
    save = []
    for num in cnt :
        if num[1] == most:
            save.append(num[0])
    
    if len(save) > 1:
        save.sort()
        print(save[1])
    else:
        print(save[0])
    
    print(nums[-1]-nums[0])
    
    
    
statistics_2108()