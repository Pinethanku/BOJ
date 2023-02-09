import sys

def poketmon_1620() :
    poket, test = tuple(map(int, sys.stdin.readline().split()))
    poket_dict_name = {}
    poket_dict_num = {}
    result = []
    for i in range(poket) :
        read = sys.stdin.readline().strip()
        poket_dict_name[read] = i+1
        poket_dict_num[i+1] = read

    for i in range(test) :
        ques = sys.stdin.readline().strip()
        try: 
            ques = int(ques)
            print(poket_dict_num[ques])
            
        except:
            print(poket_dict_name[ques])
    
    return 0
   
poketmon_1620()