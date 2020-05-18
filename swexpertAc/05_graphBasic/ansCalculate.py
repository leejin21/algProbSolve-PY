# 분석 필요
# 정답
# 출처: https://tothefullest08.github.io/algorithm/2019/08/31/5_5247_%EC%97%B0%EC%82%B0/

from collections import deque


def BFS():
    global start_num, end_num, result, tc
    while Q:
        num, cnt = Q.popleft()
        if num == end_num:
            result = cnt
            return

        for i in range(4):
            num2 = 0
            if i == 0:
                num2 = num + 1
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt+1))
                    num_lst[num2] = tc

            elif i == 1:
                num2 = num - 1
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt+1))
                    num_lst[num2] = tc

            elif i == 2:
                num2 = num*2
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt+1))
                    num_lst[num2] = tc

            elif i == 3:
                num2 = num - 10
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt+1))
                    num_lst[num2] = tc


TC = int(input())
num_lst = [0] * 1000001
for tc in range(1, TC+1):
    start_num, end_num = map(int, input().split())
    Q = deque()
    Q.append((start_num, 0))
    num_lst[start_num] = tc
    result = 0
    BFS()
    print('#%d %d' % (tc, result))
