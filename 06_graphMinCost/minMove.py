# minMove.py
# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리
# 방향 그래프: 방향이 잘못됐음, 출발지랑 도착지로 해야 함



'''
A도시에는 E개의 일방통행 도로 구간이 있으며, 각 구간이 만나는 연결지점에는 0부터 N번까지의 번호가 붙어있다.

구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때, 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력하는 프로그램을 만드시오.

모든 연결 지점을 거쳐가야 하는 것은 아니다.

그림은 입력인 N=2, E=3, 시작과 끝 지점, 구간 거리가 아래와 같은 경우의 예이다.

0 1 1
0 2 6
1 2 1

[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 연결지점 번호 N과 도로의 개수 E가 주어진다.

다음 줄부터 E개의 줄에 걸쳐 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w가 차례로 주어진다. ( 1<=T<=50, 1<=N, s, e<=1000, 1<=w<=10, 1<=E<=1000000 )

3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 2
#2 4
#3 10

'''

'''sol
다익스트라로 해결하기
1. 먼저 노드들 방향 그래프로 받고
2. 0번 노드부터 n번 노드까지 자식 노드 다 들르고 minDis랑 prevNode 배열에 업데이트해 주기
    n번 노드에서 스탑
'''

class Node:
    def __init__(self, num):
        self.num = num
        self.link = {}
        self.visit = False

    def addNode(self, node, weight):
        if node in self.link.keys() and self.link[node] < weight:
            return
        elif node not in self.link.keys():
            self.link[node] = weight


def main():
    T = int(input())
    for t in range(T):
        N, E = (int(i) for i in input().split())
        edgl = []
        for _ in range(E):
            edgl.append([int(i) for i in input().split()])
        print("#%d %d"%(t+1, t))


def makeGraph(N, edgl):
    nodes = []
    for n in range(N+1):
        nodes.append(Node(n))

    for e in edgl:
        v1 = nodes[e[0]]; v2 = nodes[e[1]]
        nodes[v1].addNode(v2, e[2])

    return nodes


def dijkstra(N, edgl):
    nodes = makeGraph(N, edgl)
    minDis = [100000000]*len(nodes)
    prevNod = [-1]*len(nodes)
    # 각 차례로 인덱스번째 노드까지 오는데의 최소 거리, 인덱스번째 노드의 직전 노드
    visited = []
    while(len(visited)== N+1):
        cur = min(minDis)


def _visitNds(cur, prevNod, minDis, N):
    # node들을 들를 때 재귀로 들름
    '''
    * 종결조건: N번 노드 들를 때
    * 방문 노드마다:
        1. visit = True로,
        2. minDis에 업데이트
        3. prevNod에 업데이트
    '''
    if cur.visit == False:

        if cur.num == N:
            # 종결조건
            return

        for nex, wei in cur.link.items():
            if minDis[nex.num] > minDis[cur.num] + wei:
                minDis[nex.num] = minDis[cur.num] + wei
                prevNod[nex.num] = cur

        cur.visit = True

        # 노드 가중치 업데이트 이후에 각자 방문해 주기
        for nex, wei in cur.link.items():
            _visitNds(nex, prevNod, minDis, N)