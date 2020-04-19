# graMinCost.py
# 5263. [파이썬 S/W 문제해결 최적화] 4일차 - 그래프 최소 비용
# 완료

'''
N개의 노드로 구성된 유향 그래프에 대해 인접 노드로 이동하는 비용을 기록한 인접 행렬이 주어진다.

모든 노드 i에 대해 다른 노드 j로 이동하는 경로가 있는 경우 최소 이동 비용을 구했을 때, 이 중 가장 큰 값을 출력하는 프로그램을 만드시오.

i에서 j로 이동할 때 다른 모든 노드를 지나야 하는 것은 아니며, 인접한 노드 사이 비용이 음수인 경우는 있으나 출발한 노드로 돌아왔을 때의 비용이 음수인 사이클은 존재하지 않는다.

다음과 같은 그래프가 있을 때 인접 행렬과 이동 비용은 다음과 같다.

[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 노드의 개수 N, 다음 줄부터 출발 노드 i에 대해 다른 노드 j까지의 비용인 N개의 aij가 N 줄에 걸쳐 주어진다.

1<=T<=50, 3<=N <=100, -99<=aij<=99 (단 i != j 면서 aij==0인 경우는 인접하지 않음을 나타낸다.)

3
3
0 27 44
-5 0 62
0 99 0
5
0 0 1 0 0
88 0 39 0 75
71 56 0 43 0
23 0 -21 0 92
22 -1 48 0 0
10
0 94 98 0 23 0 31 0 85 0
10 0 78 19 83 0 91 0 82 -7
70 0 0 24 0 66 0 0 46 0
0 40 90 0 82 77 0 0 0 0
72 0 61 16 0 99 0 58 -9 44
82 84 61 76 29 0 30 28 20 72
39 78 76 0 0 11 0 54 58 39
0 0 25 40 10 0 57 0 19 38
68 5 81 78 87 54 60 -7 0 0
67 56 83 74 0 36 0 55 0 0

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 99
#2 132
#3 92
'''

# 모든 쌍 최단 경로 알고리즘
# 플로이드 워샬 알고리즘

# 0번 노드부터 있다고 생각하기


def dijkstra(costs):
    prevs = makePrevs(costs)
    for mid in range(len(costs)):
        # mid번 노드는 중간 노드
        for end in range(len(costs)):
            # end번 노드는 끝 노드
            if prevs[mid][end] != None:
                for stt in range(len(costs)):
                    # stt번 노드는 시작 노드
                    if prevs[stt][mid] != None and stt != end:
                        # 갱신해주기
                        # print(costs[stt][end], costs[stt][mid], costs[mid][end])
                        via_cost = costs[stt][mid] + costs[mid][end]
                        if costs[stt][end] > via_cost:
                            costs[stt][end] = via_cost
                            prevs[stt][end] = mid
                        # print('stt=',stt,'mid=', mid,'end=', end)
                        # print(*costs, sep = '\n')
                        # print(*prevs, sep = '\n')

    return findMax(costs)


def findMax(costs):
    # costs에서 cost = 100000을 제외한 나머지 val 중 최대 값 구하기
    m = 0
    for i in range(len(costs)):
        for j in range(len(costs)):
            if costs[i][j] != 100000 and m < costs[i][j]:
                m = costs[i][j]
    return m


def makePrevs(costs):
    # prevs 만들어주기: prevs[i][j]는 실제 그래프의 j번째 노드에 i번째 노드가 직전 노드이면.
    prevs = [[None for j in range(len(costs))] for k in range(len(costs))]
    for i in range(len(costs)):
        for j in range(len(costs)):
            prevs[i][j] = None if costs[i][j] == 100000 else i
    return prevs


def change2Inf(c):
    # 여기서 inf = 100000으로 두기
    c = int(c)
    return 100000 if c == 0 else c


T = int(input())
for t in range(T):
    N = int(input())
    costs = []
    for _ in range(N):
        costs.append([change2Inf(i) for i in input().split()])
    print("#%d %d" % (t+1, dijkstra(costs)))
