# calculate.py
# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산
# 미완

'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.


[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

3
2 7
3 15
36 1007

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 3
#2 4
#3 8
'''


'''sol
bfs 이용: 큐 이용
'''




from collections import deque
def calculate():
    global ans, t, res
    while(que):
        # 큐에 최초로 삽입된 것 순서대로 하기: 따지고 보면 BFS
        can, cnt = que.popleft()
        if can == ans:
            # BFS이기 때문에 가장 빨리 can == ans일 때
            res = cnt
            return
        for i in range(4):
            # 케이스별로 can2 만들어주기
            can2 = 0
            if i == 0:
                can2 = can + 1
            elif i == 1:
                can2 = can - 1
            elif i == 2:
                can2 = can * 2
            elif i == 3:
                can2 = can - 10
            # 모든 케이스에 대해 큐에 삽입할/말 결정하기
            if 0 < can2 <= 1000000 and tl[can2] != t:
                que.append((can2, cnt+1))
                tl[can2] = t

                # tl의 can2 부분이 t번째 테스트케이스에서 이미 구한 값이라고 표시해두기(중복 제거)


T = int(input())
tl = [0]*1000001
for t in range(1, T+1):
    # FIXED: t가 0부터 시작하면 tl에서 초기화한 0이랑 혼동되므로 1부터 시작하게 함
    N, ans = (int(i) for i in input().split())
    que = deque()
    que.append((N, 0))
    tl[N] = t
    res = 0
    calculate()
    print("#%d %d" % (t, res))
