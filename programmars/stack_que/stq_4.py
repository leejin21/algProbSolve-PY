# 프린터
# 완료
from collections import deque


def solution(priorities, location):
    cnt = 0
    pr_cur = True
    que = deque(priorities)
    while(pr_cur == False or location != -1):
        cur = que.popleft()
        location -= 1
        pr_cur = True
        for val in que:
            if cur < val:
                que.append(cur)
                pr_cur = False
                break
        if pr_cur == True:
            cnt += 1
        elif location == -1:
            location = len(que) - 1

    return cnt


def solution1(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


# priorities = [2, 1, 3, 2]; location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
