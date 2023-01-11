import sys
import math

zerohun = []
otherlis = []
zerosum = 0
hun = int(input())
for i in range(hun):
    zerohun.append(list(map(float,sys.stdin.readline().split())))

#점수계산
for grade in zerohun:
    zerosum += grade[0]*(1+1/grade[1])*(1+grade[3]/grade[2])/4

other = int(input())
for i in range(other):
    otherlis.append(float(sys.stdin.readline()))
otherlis.sort()
if(zerosum > otherlis[math.ceil((other+1)*0.85)-1]):
    print("The total score of Younghoon \"The God\" is %.2f." %(zerosum))
else:
    print("The total score of Younghoon is %.2f." %(zerosum))