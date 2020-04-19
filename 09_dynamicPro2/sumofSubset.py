# sumofSubset.py
# 5260. [파이썬 S/W 문제해결 최적화] 3일차 - 부분 집합의 합
# TODO: 모든 원소의 합에 더 가까울 때에 대해서 따로 케이스 분류하기

'''
1부터 N까지 양의 정수를 원소로 갖는 집합이 있다. 이 집합의 모든 부분 집합에 대해 원소의 합이 K인 경우의 수 M을 알아내려고 한다.

부분 집합의 개수는 2N개이기 때문에 모든 부분 집합을 만들어 확인하려면 시간이 오래 걸리지만, 정수 i를 부분 집합에 포함시킬지 고려할 때 이미 부분 집합에 포함시킨 원소의 합 S와 아직 고려하지 않은 숫자들의 합 R을 동시에 활용하면 시간을 단축할 수 있다고 한다.

이를 활용해 M을 출력하는 프로그램을 만드시오.

[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로, N과 K가 주어진다.

( 3<=N<=100, 6<=K<=모든 원소의 합 )

3
10 7
10 53
100 5050

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 5
#2 1
#3 1
'''


'''sol
K가 부분집합의 합일 때 부분집합의 경우는
case 1. Ak = j=1~j=k-1(j + Ak-j)
case 2. 자기 자신

따라서 부분집합 = cnt(case1 + case2)
'''


def sumSubset(N, K):
    # 상향식 접근
    cons = []               # idx=k-1번째일 때 합이 k인 부분집합의 경우들(list라 0번째부터 시작)
    sma = N if N < K else K   # sma는 K와 N 중에서 더 작은 수
    for k in range(1, K+1):
        # k는 고려하는 수: 1~k까지 고려했을 때 k가 부분집합의 해일 경우, 부분집합의 경우들 구하기
        if k <= N:
            cons.append([[k]])
        else:
            cons.append([])
        for j in range(1, sma):
            # j는 pivot: j를 기준으로 나누기: k = j + (k-j)
            # 이때 k-j 자리에 저장된 부분집합의 경우까지 포함해야 함.
            stt = j
            end = k-j
            if stt >= end:
                break
            else:
                # print(k, stt, end)
                addCons(k, stt, end, cons)
                # print(*cons, sep='\n')
    return len(cons[K-1])


def addCons(k, stt, end, cons):
    for subset in cons[end-1]:
        if len(subset) > 0 and subset[0] > stt:
            cons[k-1].append([stt]+subset)


T = int(input())
for t in range(T):
    N, K = (int(i) for i in input().split())
    print("#%d %d" % (t+1, sumSubset(N, K)))
 