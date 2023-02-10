import sys

def main_9012() -> None:
    times = int(sys.stdin.readline())
    for i in range(times) :
        sentence = sys.stdin.readline().rstrip()
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
        if flag or que:
            print("NO")
        else:
            print("YES")

if __name__ == '__main__' :
    main_9012()
