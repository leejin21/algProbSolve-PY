# 위장
# 실패: 재귀?
from collections import Counter


def solution(clothes):
    cl_d = Counter()
    for c in clothes:
        cl_d[c[1]] += 1
    # 이제 cl_d를 기반으로 조합의 경우를 생각해보기.
    print(cl_d)
    i = 0
    cl = [[key, cl_d[key]] for key in cl_d]
    style = 0
    while(i < len(cl)):
        for k in range(len(cl)-i):
            temp = cl[k][1]
            for j in range(k, k+i+1):
                temp *= cl[j][1]
            style += temp
        i += 1
    return style


print(solution([['yellow_hat', 'headgear'], [
      'blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'eye'], ['smoky_makeup', 'remover'], [
      'haha', 'remover'], ['lenze', 'eye'], ['crow_mask2', 'face'], ['bla', 'bla2']]))
# face:2, eye:2, remover:2, bla:1
