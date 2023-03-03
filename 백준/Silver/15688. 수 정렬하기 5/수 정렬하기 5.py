import sys

def main_15688():
    times = int(sys.stdin.readline())
    data_list = []
    for i in range(times):
        data_list.append(int(sys.stdin.readline()))
    data_list.sort()
    for data in data_list:
        print(data)
        
if __name__ == '__main__':
    main_15688()