import sys

def main_5800():
    times = int(sys.stdin.readline())
    for i in range(times):
        data_list = list(map(int, sys.stdin.readline().split()))[1:]
        data_list.sort()
        max = data_list[-1]
        min = data_list[0]
        max_diff = data_list[1]-data_list[0]
        for num in range(len(data_list)-1):
            if data_list[num+1] - data_list[num] > max_diff:
                max_diff = data_list[num+1] - data_list[num]
        print("Class", i+1)
        print("Max {0}, Min {1}, Largest gap {2}".format(max, min, max_diff))
        
    
if __name__ == "__main__":
    main_5800()