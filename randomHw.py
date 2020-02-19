# Random(0,1) 함수만을 가지고 Random(0, n-1)을 구현해보시오(단, n은 3이상의 정수). 또한, 본인이 만든 함수의 평균 수행시간은 어떻게 되는가?
# This was for algorithm lecture in SMWU assignment
import math
from random import randint

def Random1(n):
    # 0부터 n까지의 random number를 구현
    if n >= 3:
        sum = 0
        p = int(math.log(n-1,2))

        for i in range(p,-1,-1):
            # print(i)
            sum = int(sum + randint(0,1)*math.pow(2,i))
            # print(sum)

        if sum>=n:
            return Random1(n)
        else: return sum


def Random2(a,b):
    if b-a>=3:
        sum = a
        p = int(math.log((b-a-1),2))

        for i in range(p, -1, -1):
            sum = int(sum + randint(0,1)*math.pow(2,i))

        if sum >= b:
            return Random2(a,b)
        else: return sum

while(True):
    # ans = int(input("Random(0,n-1)에서 n을 입력하시오(그만은 0)"))
    # if ans == 0:
    #     break
    # print("Random(n-1) = ", Random1(ans))

    ans2 = list(int(i) for i in input("Random(a,b)에서 a b 차례로 입력").split(" "))
    if ans2[0] == -1:
        break
    r = Random2(ans2[0], ans2[1])
    # while(r==5):
    print("Random(a,b) = ", r)
