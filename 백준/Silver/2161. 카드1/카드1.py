import sys

def card2_2164() -> int:
    num = int(sys.stdin.readline())
    if num==1:
        print(1)
        return 0
    
    result = []
    cards = [i for i in range(1, num+1)]
    while(len(cards) > 1):
        if len(cards)%2:
            result += cards[0:-2:2]
            cards = [cards[-1]] + cards[1::2]
        else :
            result += cards[0::2]
            cards = cards[1::2]
    for re in result:
        print(re, end=" ")
    print(cards[0])
    
    return 0
    
if __name__ == "__main__":
    card2_2164()
    