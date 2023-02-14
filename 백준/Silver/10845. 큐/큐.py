import sys

def main_10845():
        times = int(sys.stdin.readline())
        stack = []
        for i in range(times):
            function = sys.stdin.readline().strip()
            if(not function.isalpha()) :
                function, num = tuple(function.split())
                stack.append(num)
            else:
                if function == 'pop':
                    if stack:
                        print(stack.pop(0))
                    else :
                        print(-1)
                elif function == 'size':
                    print(len(stack))
                elif function == 'empty':
                    if stack:
                        print(0)
                    else :
                        print(1)
                elif function == 'front':
                    if stack:
                        print(stack[0])
                    else:
                        print(-1)
                elif function == 'back':
                    if stack:
                        print(stack[-1])
                    else:
                        print(-1)
            
    
if __name__ == "__main__":
    main_10845()