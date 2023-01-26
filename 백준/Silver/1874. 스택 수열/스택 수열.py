import sys

def stack_1874():
    times = int(sys.stdin.readline())
    stack = []
    nums = []
    result = []
    
    for i in range(times) : 
        nums.append(int(sys.stdin.readline()))
    
    if(times == 1):
        print("+")
        print("-")
        return 0
    
    
    i = 1
    flag = 1
    
    for num in nums :
        while(i<=num) :
            result.append("+")
            stack.append(i)
            i += 1
            flag = 1
            #print(stack)
        if num == stack[-1] :
            if flag == 0 :
               print("NO")
               return 0 
            result.append("-")
            stack.pop()
            #print(stack)
        else : 
            flag = 0
    
    if stack : 
        print("NO")
        return 0 

    
    for re in result:
        print(re)
        
    return 0
                

stack_1874()