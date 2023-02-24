import sys

def main_1439():
    input_num = sys.stdin.readline().strip()
    num_dict = {'0':0, '1':0}
    if len(input_num) == 1:
        print(0)
        return 0
    
    num_dict[input_num[0]] = 1
    for i in range(len(input_num)-1):
        if input_num[i] != input_num[i+1] :
            num_dict[input_num[i+1]] = num_dict[input_num[i+1]] + 1
    print(num_dict['0'] if num_dict['0']<=num_dict['1'] else num_dict['1'])
    
if __name__ == '__main__':
    main_1439()
                