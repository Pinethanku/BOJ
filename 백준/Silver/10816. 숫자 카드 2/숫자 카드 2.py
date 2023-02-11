import sys

def main_10816() -> None:
    times = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    num_dict = {}
    for num in num_list:
        try : 
            num_dict[num] += 1
        except :
            num_dict[num] = 1
    times = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    for num in num_list:
        try:
            print(num_dict[num], end=" ")
        except:
            print(0, end=" ")
    
if __name__== '__main__':
    main_10816()