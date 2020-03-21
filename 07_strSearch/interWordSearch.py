# interWordSearch.py
# 5252. [파이썬 S/W 문제해결 최적화] 1일차 - 공통 단어 검색

'''

A와 B는 각자 만든 영어 단어장에 같은 단어가 얼마나 있는지 확인하려고 한다.

두 사람이 만든 단어장에 공통으로 들어있는 단어의 개수를 알아내는 프로그램을 만드시오. 단, 모든 단어는 소문자로 되어 있다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 A의 단어 개수 N과 B의 단어개수 M이 주어진다. 다음 줄부터 N개의 단어와 M개의 단어가 주어진다.

(1<=T<=50, 3<=N, M<=3000)

단어의 길이는 20글자 이내이다.

2
3 3
book
home
study
right
home
study
3 5
people
water
night
water
hand
country
night
people

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''

def dicSearch(a_dic, b_dic):
    cnt = 0
    if len(a_dic) >= len(b_dic):
        for word in b_dic:
            if word in a_dic:
                cnt += 1
    else:
        for word in a_dic:
            if word in b_dic:
                cnt += 1
    return cnt

    
T = int(input())
for t in range(T):
    A, B = (int(i) for i in input().split())
    a_dic = []; b_dic = []
    for _ in range(A):
        a_dic.append(input())
    for _ in range(B):
        b_dic.append(input())
    a_dic = set(a_dic); b_dic = set(b_dic)
    print("#%d %d"%(t+1, dicSearch(a_dic, b_dic)))


