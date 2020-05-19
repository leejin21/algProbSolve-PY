# 완주하지 못한 선수
'''sol
comp의 원소의 개수가 part의 원소의 개수와 같은 지 판단
1. part를 기준으로 딕셔너리 만들기
2. comp와 part에 존재하는 원소의 개수 구하기
3. 각 원소의 개수가 맞지 않는 원소 리턴

'''
import collections


def solution(participant, completion):
    cand = {p: [] for p in participant}
    for p in participant:
        if len(cand[p]) == 0:
            cand[p].append(1)
        else:
            cand[p][0] += 1
    for c in completion:
        if len(cand[c]) == 1:
            cand[c].append(1)
        else:
            cand[c][1] += 1
    for key, value in cand.items():
        if value[0] != value[1]:
            return key


def ansSolution(participant, completion):
    # FIXED: part-comp는 카운터 딕셔너리 형태. part[key]-comp[key] > 0 인 key값을 반환해 가짐.
    part = collections.Counter(participant)
    comp = collections.Counter(completion)
    return list((part-comp).keys())[0]


def ansSolution2(participant, completion):
    # hash는 해당 데이터값이 담겨져 있는 공간을 말하는 듯. 리터럴마다 그게 담긴 공간 주소가 다름.
    # 예: a = 'a'; hash('a') == hash(a)
    temp = 0
    cand = {}
    for p in participant:
        cand[hash(p)] = p
        temp += hash(p)
    for c in completion:
        temp -= hash(c)
    return cand[temp]


print(ansSolution2(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))
