# elecCart2.py
# 5265. [파이썬 S/W 문제해결 최적화] 4일차 - 전기카트2
# 완료
# TODO: 비트테이블 관련 설명 더 자세히 포스트해서 velog에 올리기
'''
골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91
e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89

이 경우 최소 소비량은 89가 된다.

N이 최대 16이기 때문에, N=10이 최대일 때의 계산 방법은 시간이 오래 걸릴 수 있음에 유의하라.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. ( 1<=T<=50 )

다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다.  ( 3<=N<=16 )

3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 89
#2 96
#3 139

'''
'''
main idea
D[v0][A] = min(W[v0][vj] + D[vj][A-{vj}])
j = 0 제외한 모든 노드(1~n)
A = 반드시 한번씩만 방문하는 노드의 집합, 1~n번 노드 전체집합의 부분집합
'''

# 비트테이블 이용
# 0번 노드를 출발점으로 생각

INF = 5000


def elecCart(wei):
    # wei: 각 구역 이동할 때의 배터리 사용량을 나타낸 2d 리스트
    # bat: bat[x][y]에서 x는 노드의 번호, y는 x번째 노드와 0번째 노드를 제외한 노드들의 집합의 부분집합을 표현한다. 비트 테이블.

    global INF

    bat = [[INF for i in range(pow(2, len(wei)-1))] for j in range(len(wei))]
    for i in range(1, len(bat)):
        # bat[1][0], bat[2][0], bat[3][0] 초기화해주기
        bat[i][0] = wei[i][0]

    # range(1, pow(2, len(wei)-1)) = 0번 노드 제외한, 1번 노드-n번 노드에 대한 부분집합의 경우
    for A in range(1, pow(2, len(wei)-1)):
        # A = 0x101일 때 1번 노드와 3번 노드가 A 집합에 포함된 것을 의미
        s_can, m_can = sttNodeCand(A, len(wei)-1)
        # start candidate, middle candidate
        for stt in s_can:
            for mid in m_can:
                # k는 1부터이므로
                B = A - pow(2, mid-1)               # B 집합은 mid 노드를 A 집합에서 뺀 집합
                rep = wei[stt][mid] + bat[mid][B]
                bat[stt][A] = rep if bat[stt][A] > rep else bat[stt][A]

    # 마무리
    for l in range(1, len(wei)):
        U = pow(2, len(wei)-1)-1                    # U 집합은 전체 노드를 포함한 집합
        # B 집합은 l번째 노드를 U 집합에서 뺀 나머지
        B = U - pow(2, l-1)
        rep = wei[0][l] + bat[l][B]
        bat[0][U] = rep if bat[0][U] > rep else bat[0][U]

    return bat[0][U]


def sttNodeCand(j, zer):
    # return candidate list of start node icand and candidate list of mid node kcand
    # zer = the length of binary string
    # 1. change j as binary string form
    j2b = '0'*(zer-len(bin(j)[2:])) + bin(j)[2:]
    # print(i2b)
    icand = []
    kcand = []
    for idx in range(len(j2b)):
        # 2. add cand for start node to list icand, for middle node: to list kcand
        if j2b[idx] == '0':
            icand.append(zer - idx)
        else:
            kcand.append(zer - idx)
    return icand, kcand


T = int(input())
for t in range(T):
    N = int(input())
    W = []
    for _ in range(N):
        W.append([int(i) for i in input().split()])
    # elecCart(W)
    print("#%d %d" % (t+1, elecCart(W)))
