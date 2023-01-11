import sys

def checkpal(palch, yusa):
    if (yusa == 1):  #유사회문 체크인 경우
        if palch == palch[::-1]:
            return 1 #유사회문 체크에서 회문인 경우
        else:
            return 0
    else: #처음 체크인 경우
        start = 0
        end =len(palch)-1
        while(start<end):
            if(palch[start] != palch[end]):
                if((checkpal(palch[start+1:end+1], 1)) or (checkpal(palch[start:end], 1))):
                    return 1
                else:
                    return 2
            start += 1
            end -= 1
    return 0
        
lenth = int(sys.stdin.readline())
lis = [sys.stdin.readline().strip() for i in range(lenth)]

for palin in lis:
    print(checkpal(palin, 0))