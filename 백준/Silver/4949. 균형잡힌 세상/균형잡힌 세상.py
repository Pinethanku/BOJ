import sys

def balance_4949():
    result = []
    
    while(True) :
        sentence = sys.stdin.readline().rstrip()
        if sentence == ".":
            break
        else :
            que = []
            flag = 0
            for char in sentence :
                if char == "(" or char == "[":
                    que.append(char)
                    #print(que)
                elif char == ")" :
                    if que :
                        pop = que.pop()
                        #print("pop :", pop)
                        if pop != "(" :
                            flag = 1
                            break
                    else :
                        flag = 1
                        break
                elif char == "]" :
                    if que : 
                        pop = que.pop()
                        #print("pop :", pop)
                        if pop != "[" :
                            flag = 1
                            break
                    else:
                        flag = 1
                        break
                    
            if flag or que:
                result.append("no")
            else:
                result.append("yes")
                
    for re in result:
        print(re)
    
balance_4949()
