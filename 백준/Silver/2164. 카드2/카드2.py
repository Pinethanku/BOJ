import sys

def card2_2164():
    num = int(sys.stdin.readline())
    if num==1:
        print(1)
        return 0
    
    cards = [i for i in range(1, num+1)]
    while(len(cards) > 1):
        if len(cards)%2:
            cards = [cards[-1]] + cards[1::2]
        else :
            cards = cards[1::2]
    print(cards[0])
    
    return 0
    
card2_2164()
    