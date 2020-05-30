# 쇠막대기
# 완료
from collections import deque

def solution(arrangement):
    cnt = 0; prb = arrangement[0]
    outline = deque()
    open_cnt = 0

    for b in arrangement:
        outline.append(b)
        if b == '(': open_cnt += 1
        else:
            if prb == '(':
                cnt += open_cnt - 1
            elif outline[-2] == '(':
                cnt += 1
            outline.pop(); outline.pop()
            open_cnt -= 1
        
        prb = b
        
    return cnt

# replace 쓸 생각을 못했는데 진짜 괜찮은 듯.
def solution1(arrangement):
    answer = 0
    sticks = 0
    rasor_to_zero = arrangement.replace('()','0')

    for i in rasor_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer

arrangement = "()(((()())(())()))(())"
print(solution(arrangement))