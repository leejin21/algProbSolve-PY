# 스택/큐 1
# 탑
# 완료
from collections import deque

# O(n^2) 풀이: 다소 복잡하게 푼 듯.


def solution(heights):
    heights = [200] + heights
    towers = deque(heights)
    ans = deque()
    cnt1 = len(towers) - 1
    while(len(towers) > 0):
        t1 = towers.pop()
        cnt2 = len(towers) - 1
        while(len(towers) > 0):
            t2 = towers.pop()
            if t1 < t2:
                ans.appendleft(cnt2)
                break
            cnt2 -= 1
        towers = deque(heights[:cnt1])
        cnt1 -= 1

    return list(ans)

# 실행시간은 비슷하지만 list 이용: 저장공간 아끼기
def solution1(heights):
    towers = [200] + heights
    ans = deque()
    for i in range(len(towers)-1, 0, -1):
        for j in range(i, -1, -1):
            if towers[i] < towers[j]:
                ans.appendleft(j)
                break
    return list(ans)


def solution2(heights):
    pass


heights = [1, 5, 3, 6, 7, 6, 5]
solution1(heights)
