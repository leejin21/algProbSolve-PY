# colGraph.py
# 5286. [파이썬 S/W 문제해결 최적화] 5일차 - 그래프 색칠하기
# 성공
'''

N개의 노드로 구성된 그래프의 노드를 M개의 색상을 이용해 칠하려고 한다.

그래프에 대한 정보가 주어지면 모든 인접한 노드 쌍에 대해, 두 노드를 서로 다른 색으로 칠하는 것이 가능한지 알아내는 프로그램을 만드시오.

노드 번호는 1에서 N번까지이고, M은 2, 3, 4 중 하나이다. 칠할 수 있는 경우 1, 칠할 수 없는 경우 0을 출력한다.

다음은 2가지 색으로 칠할 수 있는 그래프와 칠할 수 없는 그래프의 예이다.

왼쪽의 경우 1, 오른 쪽의 경우 0을 출력한다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 노드의 개수 N, 간선의 개수 E, 사용할 수 있는 색상수 M이 주어지고, E개의 줄에 걸쳐 간선의 양끝 노드 번호가 주어진다.

3<=N<=20, 2<=E<=100, 2<=M<=4

2
4 4 2
1 2
1 3
2 4
3 4
4 5 2
1 2
1 3
2 4
3 4
2 3
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 1
#2 0
'''


'''sol
1. 최대 인접 노드의 개수 찾기
2. 이를 M과 비교

'''


class Node:
    def __init__(self, num):
        self.num = num
        self.adjNode = []
        self.color = None

    def saveAdj(self, node):
        # 노드의 인접 노드 self.adjNode에 추가
        if node not in self.adjNode:
            # 중복되는 간선이 있을 경우를 대비해
            self.adjNode.append(node)

    def findColor(self, co_l):
        # 인접 노드들의 color을 제외한 color로 색칠하기 if 더이상 color가 없으면 return False, else return True
        # co_l은 [0]*M 이런 리스트
        for node in self.adjNode:
            if node.color != None:
                co_l[node.color] = 1

        if 0 in co_l:
            self.color = co_l.index(0)
            return True
        else:
            return False


def colorGraph(N, M, edges):
    # main function: color the graph until there are no colors left
    # save nodes in graph
    graph = [Node(i+1) for i in range(N)]

    # save edges in graph
    for e in edges:
        n1 = e[0]
        n2 = e[1]
        graph[n1-1].saveAdj(graph[n2-1])
        graph[n2-1].saveAdj(graph[n1-1])

    # 노드에 color 넣어주기
    for n in graph:
        suc = n.findColor([0]*M)
        if suc == False:
            return 0

    return 1


T = int(input())
for t in range(T):
    N, E, M = (int(i) for i in input().split())
    edges = []
    for e in range(E):
        edges.append([int(i) for i in input().split()])
    print("#%d %d" % (t+1, colorGraph(N, M, edges)))
