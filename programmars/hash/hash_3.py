# 위장
# 성공
from collections import Counter
from functools import reduce


def solution(clothes):
    clothes = [i[1] for i in clothes]
    kinds = [v for k,v in Counter(clothes).items()]
    tot = 0
    for i in range(len(kinds)-1, -1, -1):
        tot += kinds[i]*(1+tot)
    return tot


def solution1(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer




print(solution([['yellow_hat', 'headgear'], [
      'blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))

