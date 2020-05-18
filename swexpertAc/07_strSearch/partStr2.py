# partStr.py
# 5254. [파이썬 S/W 문제해결 최적화] 1일차 - 부분 문자열
# 완료!!
'''
길이가 K인 문자열 S가 있을 때, S의 연속된 일부분을 부분 문자열이라고 한다.

부분 문자열은 원래의 순서가 바뀌거나 중간에 있는 글자가 빠져서는 안된다.

주어진 문자열의 부분 문자열을 사전순으로 정렬한 후, N번째 부분 문자열의 첫 글자와 글자 수를 출력하는 프로그램을 완성하시오.

예를 들어 abac의 부분 문자열은 사전순으로 정렬하면 다음과 같다.

a ab aba abac ac b ba bac c

3번째 부분 문자열은 aba가 된다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 다음 줄부터 각 줄에 N과 문자열이 주어진다.

문자열의 길이는 4글자 이상 1000글자 이내이고, N은 문자열의 길이 이내이다. ( 1<=T<=50 )

3
5 abac
9 ltsodjxzyc
21 jldgovukjf

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 a 2
#2 j 2
#3 j 4

'''


class Node:
    # 트라이의 기본 단위
    def __init__(self):
        self.link = [None]*26


def save2Trie(word):
    # 1. word를 트라이에 저장: abac, bac, ac, c 이런 방식으로.
    trie = Node()
    i = 0
    while(i < len(word)):
        temp = trie
        for j in range(i, len(word)):
            idx = alp2idx(word[j])
            if temp.link[idx] == None:
                temp.link[idx] = Node()
            temp = temp.link[idx]
        i += 1
    return trie

# TODO: 2. 전역변수 => return문으로 바꾸기


def dfs(temp, dep):
    # 2. dfs 통해서 n번째 부분수열 찾기
    global n, cnt, alp, g_dp, trie
    for i in range(len(temp.link)):
        if temp.link[i] != None and n < cnt:
            # n번째 부분 문자열까지만 찾고 && 트라이 리스트에 채워져 있는 부분만.
            if temp == trie:
                # 첫 글자 alp에 저장해 두기
                alp = idx2alp(i)
            # 몇번째 부분 문자열인 지 정하기
            n += 1
            if n == cnt:
                # n번째 부분 문자열일 때, dep 전역변수에 저장해 두기
                g_dp = dep
                return
            else:
                # n번째 부분 문자열까지만 재귀함수 돌리기
                dfs(temp.link[i], dep+1)


def alp2idx(alp):
    return ord(alp) - 97


def idx2alp(idx):
    return chr(idx+97)


T = int(input())
for t in range(T):
    n = 0
    g_dp = 0
    alp = None
    # alp, g_dp를 답으로 삼고 하기
    _input = input().split()
    cnt = int(_input[0])
    word = _input[1].strip()
    trie = save2Trie(word)
    dfs(trie, 1)
    print("#%d %s %d" % (t+1, alp, g_dp))
