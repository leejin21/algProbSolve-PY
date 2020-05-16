# minCost.py
# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용
# 완료
'''
출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에, 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.

다음은 각 지역의 높이를 기록한 표의 예로, 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래이며, 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.

(표에 표시되지 않은 지역이나 대각선 방향으로는 이동 불가.)

0 2 1
0 1 1
1 1 1

인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.

색이 칠해진 칸을 따라 이동하는 경우(0-0-1-1-1) 기본적인 연료 소비량 4에, 높이가 0에서 1로 경우만큼 추가 연료가 소비되므로 최소 연료 소비량 5로 목적지에 도착할 수 있다.

이동 가능한 지역의 높이 정보에 따라 최소 연료 소비량을 출력하는 프로그램을 만드시오.

[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 표의 가로, 세로 칸수N, 다음 줄부터 N개 지역의 높이 H가 N개의 줄에 걸쳐 제공된다.

1<=T<=50, 3<=N<=100, 0<=H<1000


3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''
INF = 9000000


def dijkstra():
    global INF
    # 1. 쓸 리스트 초기화시키기
    visited = [[False for i in range(len(graph))] for j in range(len(graph))]
    unvisited = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            unvisited.append((i, j))
    minCost = [[INF for i in range(len(graph))] for j in range(len(graph))]
    minCost[0][0] = 0

    # 2. 본격 dijkstra 알고리즘
    while(len(unvisited) != 0):
        cur = selectCur(unvisited, minCost)
        c_i, c_j = cur
        for i, j in nextNod(cur):
            # FIXED: graph[i][j]<= graph[c_i][c_j]의 경우를 생각: 만약 높이 차이가 음수일 경우, 비용은 0으로 취급.
            diff = 0 if graph[i][j] <= graph[c_i][c_j] else graph[i][j] - \
                graph[c_i][c_j]
            cand = minCost[c_i][c_j] + diff + 1
            if visited[i][j] == False and minCost[i][j] > cand:
                minCost[i][j] = cand

        unvisited.remove((c_i, c_j))
        visited[c_i][c_j] == True

    return minCost[len(graph)-1][len(graph)-1]


def selectCur(unvisited, minCost):
    # 이번 노드 정하기: O(k^2)
    min = INF
    for i, j in unvisited:
        if min >= minCost[i][j]:
            min = minCost[i][j]
            cur = (i, j)
    return cur


def nextNod(cur):
    # cur와 연결된 노드 찾기: O(1)
    i, j = cur
    # 차례로 위, 오, 아래, 왼
    nex = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
    if i == 0:
        # 맨 위 위치: 위 삭제
        nex.remove((i-1, j))
    if j == 0:
        # 맨 왼쪽 위치: 왼 삭제
        nex.remove((i, j-1))
    if i == len(graph)-1:
        # 맨 아래 위치: 아래 삭제
        nex.remove((i+1, j))
    if j == len(graph)-1:
        # 맨 오른쪽 위치: 오 삭제
        nex.remove((i, j+1))
    return nex


T = int(input())
for t in range(T):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append([int(i) for i in input().split()])
    # print(reg)
    print("#%d %d" % (t+1, dijkstra()))
