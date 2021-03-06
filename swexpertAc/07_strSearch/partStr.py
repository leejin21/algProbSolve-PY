# partStr.py
# 5254. [파이썬 S/W 문제해결 최적화] 1일차 - 부분 문자열
# 제한시간 초과
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

def findPart(n, word):
    # 1. abac에서 차례로 하나씩, 둘씩,,, 끝까지
    part = []
    for i in range(len(word)):
        for j in range(1, len(word)-i+1):
            if word[i:i+j] not in part:
                part.append(word[i:i+j])
    part = sorted(part)
    return part[n-1]


T = int(input())
for t in range(T):
    _input = input().split()
    n = int(_input[0]); word = _input[1].strip()
    ans = findPart(n, word)
    print("#%d %s %d"%(t+1, ans[0], len(ans)))