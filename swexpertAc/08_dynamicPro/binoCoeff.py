# binoCoeff.py
# 5256. [파이썬 S/W 문제해결 최적화] 2일차 - 이항계수
# 성공

'''
n, a, b가 주어지면 (x+y)n에서 xayb의 계수를 구하는 프로그램을 작성하라.

예를 들어 n, a, b가 2, 1, 1인 경우 (x+y)2 = x2 + 2xy + y2이 되고, xy의 계수는 2이다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 n, a, b가 주어진다. 입력으로 존재하지 않는 xayb의 계수는 주어지지 않는다. (입력은 항상 a+b=n을 만족)
 ( 0<=n, a, b<=70 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''


def bino(n, a):
    # used combination(조합: nCa)
    tot = 1
    for i in range(n, n-a, -1):
        tot *= i
    for j in range(a, 0, -1):
        tot /= j

    return tot


T = int(input())
for t in range(T):
    n, a, b = (int(i) for i in input().split())
    # nCa = nCn-a 이기 때문에 연산을 더 적게 하는 방법을 택함.
    print("#%d %d" % (t+1, bino(n, min(a, b))))
