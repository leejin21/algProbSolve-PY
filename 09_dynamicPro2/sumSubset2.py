# sumSubset2.py
# 5260. [파이썬 S/W 문제해결 최적화] 3일차 - 부분 집합의 합
# 미완2

'''
[입력]
첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로, N과 K가 주어진다.
( 3<=N<=100, 6<=K<=모든 원소의 합 )

3
10 7
10 53
100 5050

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 5
#2 1
#3 1
'''
cnt = 0


class Node:
    def __init__(self, S, R):
        self.left = None
        self.right = None
        self.S = S
        # 이미 포함시킨 원소의 합
        self.R = R
        # 고려하지 않은 원소의 합


def dp(N, K):
    head = Node(0, N*(N+1)//2)
    _dp(head, 1, K)


def _dp(temp, cur_dep, K):
    # use recursion: 하향식
    global cnt
    if temp.S > K:
        # 0. 종결조건
        return
    elif temp.S == K:
        # 1. 종결 조건
        cnt += 1
        print("cnt: ", cnt)
        return
    elif temp.S < K and temp.S + temp.R >= K:
        # 2. 아직 가능성이 남은 경우
        # (1) temp.left 재귀
        print(cur_dep, "left:", temp.S+cur_dep, temp.R-cur_dep, 'cnt=', cnt)
        temp.left = Node(temp.S+cur_dep, temp.R - cur_dep)
        _dp(temp.left, cur_dep+1, K)

        # (2) temp.right 재귀
        print(cur_dep, "right:", temp.S, temp.R-cur_dep, 'cnt=', cnt)
        temp.right = Node(temp.S, temp.R - cur_dep)
        _dp(temp.right, cur_dep+1, K)


T = int(input())
for t in range(T):
    cnt = 0
    N, K = (int(i) for i in input().split())
    dp(N, K)
    print("#%d %d" % (t+1, cnt))
