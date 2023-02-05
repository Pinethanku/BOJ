import sys

def AC_5430():
    times = int(sys.stdin.readline())
    for i in range(times):
        p = list(sys.stdin.readline().strip())
        n = int(sys.stdin.readline())
        if n:
            num_list = list(map(int,(sys.stdin.readline().strip("[" "]" "\n").split(","))))
        else :
            sys.stdin.readline()
            num_list = []
        flag = 1
        rever = False
        R_count = 0
        for fun in range(len(p)):
            if p[fun]=='D' :
                if not num_list :
                    flag = 0
                    print("error")
                    break
                else:
                    if R_count%2 == 0:
                        if rever:
                            num_list.pop(-1)
                        else:
                            num_list.pop(0)
                    else:
                        if rever:
                            num_list.pop(0)
                        else:
                            num_list.pop(-1)
                        rever = not(rever)
                    R_count = 0
            else:
                R_count += 1
                
        if R_count%2:
            rever = not(rever)
            
        if flag:
            result = "["
            if rever :
                for i in range(len(num_list)-1,-1,-1):
                    if i:
                        result += str(num_list[i])+","
                    else:
                        result += str(num_list[i])
                
            else :
                for i in range(len(num_list)):
                    if i==len(num_list)-1:
                        result += str(num_list[i])
                    else:
                        result += str(num_list[i])+","
                        
            print(result + "]")
    
AC_5430()