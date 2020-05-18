# prefixSearch.py
# 5253. [파이썬 S/W 문제해결 최적화] 1일차 - 접두어 검색

'''
문자열 about에서 첫 글자부터 이어지는 a, ab, abo, abou, about은 접두어이다.

단, abu 같이 첫 글자부터 계속 이어지는 경우가 아니면 접두어가 아니다.

문자열 그룹 A와 B가 주어질 때, *B에 속한 문자열 중 A의 접두어인 문자열의 개수*를 알아내는 프로그램을 만드시오. 모든 단어는 소문자로 이루어져 있다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 A의 단어 개수 N과 B의 단어개수 M이 주어진다.

다음 줄부터 N개의 단어와 M개의 단어가 주어진다.

( 1<=T<=50, 3<=N, M<=3000 ) 

단어의 길이는 20글자 이내이다.

2
3 3
able
abl
abroad
ab
abo
a
3 5
people
water
night
wa
h
country
ni
people

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 2
#2 3
'''

def prefixCnt(al, bl):
    cnt = 0
    for pref in bl:
        # 접두어 pref
        for word in al:
            if pref == word[:len(pref)]:
                cnt += 1
                break
        # print(pref, cnt)
    return cnt


T = int(input())
for t in range(T):
    A, B = (int(i) for i in input().split())
    a_grp = []; b_grp = []
    for _ in range(A):
        a_grp.append(input().strip())
    for _ in range(B):
        b_grp.append(input().strip())
    print("#%d %d"%(t+1, prefixCnt(a_grp,b_grp)))

