import sys

def main_coin0():
    coins, aim = tuple(map(int,sys.stdin.readline().split()))
    coin_list = []
    for i in range(coins):
        coin_list.append(int(sys.stdin.readline()))
    result = 0
    for i in range(coins-1,-1,-1):
        if coin_list[i]>aim:
            continue
        result += aim//coin_list[i]
        aim = aim % coin_list[i]
        
    print(result)
        
    
if __name__ == '__main__':
    main_coin0()