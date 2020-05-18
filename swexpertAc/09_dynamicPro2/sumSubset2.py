# sumSubset2.py
# 5260. [파이썬 S/W 문제해결 최적화] 3일차 - 부분 집합의 합
# 성공

cnt = 0
# FIXED: 내림차순으로 수정(cur_dep에서 cur_h로)
# FIXED: class 안 쓰고 그냥 재귀만 씀 그랬더니 마지막 테케도 통과(그전까진 마지막 1개가 제한시간 초과였음)


def _dp(s, r, cur_h):
    # use recursion: 하향식
    global cnt, K
    if s > K or s + r < K:
        # 0. 종결조건(prunning): 현재까지 추가한 원소의 합이 K를 이미 넘어가는 경우
        return
    elif s == K:
        # 1. 종결 조건: 현재까지 추가한 원소의 합 == K일 경우: cnt 추가해줌
        cnt += 1
        return

    # 2. 아직 가능성이 남은 경우
    # (1) temp.left 재귀
    _dp(s+cur_h, r-cur_h, cur_h-1)
    # (2) temp.right 재귀
    _dp(s, r-cur_h, cur_h-1)


T = int(input())
for t in range(T):
    cnt = 0
    N, K = (int(i) for i in input().split())
    _dp(0, N*(N+1)//2, N)
    print("#%d %d" % (t+1, cnt))
