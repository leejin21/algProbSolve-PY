# stq_2.py
# 완료
from collections import deque


def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    # 0. 첫번쨰 트럭 올라가기
    sec = 1
    location = deque([1])
    onbridge = deque([waiting.popleft()])
    # 두번째 트럭 대기 타기
    if len(truck_weights) > 1:
        cur = waiting.popleft()
        # 1. 마지막 트럭까지 다리 위에 올리기
        while(True):
            # (1) location 1칸씩 이동: class 사용해서 보완하기(시간 복잡도)
            location = deque(map(lambda x: x+1, location))
            # (2) bridge 이미 건넌 트럭 onbridge에서 빼 주기
            if location[len(location)-1] > bridge_length:
                location.pop()
                onbridge.pop()
            # (3) 대기자 onbridge에 넣어주기: sum 부분 class 사용해서 보완하기(시간 복잡도)
            if sum(onbridge) + cur <= weight:
                onbridge.appendleft(cur)
                location.appendleft(1)
                if len(waiting) == 0:
                    # 마지막 트럭까지 다리 위에 올림
                    sec += 1
                    break
                # 다음 대기자
                cur = waiting.popleft()
            sec += 1

        # 2. 마지막 트럭이 다리를 다 건널 때까지 걸리는 시간: bridge_length이므로
    return sec + bridge_length


print(solution(100, 100, [10]))
print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
