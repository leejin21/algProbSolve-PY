# attachTile.py
# 5255. [파이썬 S/W 문제해결 최적화] 2일차 - 타일 붙이기

'''
다음과 같이 2x1, 2x2, 2x3 크기의 타일을 2xN 크기의 공간에 붙이려고 한다. N이 주어지면 붙이는 방법이 모두 몇 가지가 경우가 있는지 출력하는 프로그램을 만드시오.

예를 들어 N이 3인 경우 타일을 붙이는 방법은 다음과 같다.

[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 N이 주어진다. 3<=N<=30

3
5
8
10

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 28
#2 277
#3 1278

'''
tiles = [0]*5


def saveTile(k):
    if k == 0 or k == 1:
        tiles[k] = 1
    elif k == 2:
        tiles[k] = 2
    elif tiles[k] != 0:
        return
    else:
        saveTile()


T = int(input())
for t in range(T):

    tiles = [0]*n
    print("#%d %d"%(t, t))
