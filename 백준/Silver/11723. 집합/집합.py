import sys

def main_11723() -> None:
    times = int(sys.stdin.readline())
    S_dict = {}
    x = 0
    func = []
    for i in range(1, 21) :
       S_dict[i] = 0 
    for i in range(times):
        func = list(sys.stdin.readline().split())
        if len(func)==1:
            if func[0] == 'all':
                S_dict.update({}.fromkeys(S_dict, 1))
            else:
                S_dict.update({}.fromkeys(S_dict, 0)) 
        else:
            x = int(func[1])
            if func[0] == 'add':
                S_dict[x] = 1
            elif func[0] == 'remove' :
                S_dict[x] = 0
            elif func[0] == 'check':
                print(S_dict[x])
            else:
                S_dict[x] = int(not S_dict[x]) 
            
main_11723()