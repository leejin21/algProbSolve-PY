# minMove2.py
# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

'''sol
유향 그래프, 가중치 존재
우선순위 큐 이용?
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

#1 2
#2 4
#3 10
'''
INF = 90000000000

class Node:
    def __init__(self, i):
        self.num = i
        self.next = []
        # self.visit = False

def minMove(N):
    global INF
    nodel = [Node(i) for i in range(N+1)]

    unvisited = nodel[:]
    minCost = [INF]*(N+1)
    for k in inp:
        n1 = k[0]
        n2 = k[1]
        e = k[2]
        nodel[n1].next.append([nodel[n2], e])
    
    minCost[0] = 0
    while(len(unvisited)!=0):
        # unvisited 노드 중에서 비용이 가장 작은 노드를 골라야 함.
        cur = selectCur(unvisited, minCost)
        for nx in cur.next:
            nd = nx[0]; w = nx[1]
            if minCost[nd.num] > minCost[cur.num] + w:
                minCost[nd.num] = minCost[cur.num] + w
            
        unvisited.remove(cur)
    return minCost[len(minCost)-1]

def selectCur(unvisited, minCost):
    min = INF
    for n in unvisited:
        if min >= minCost[n.num]:
            min = minCost[n.num]
            cur = n
    return cur

T = int(input())    
for t in range(T):
    N, E = (int(i) for i in input().split())
    inp = []
    for _ in range(E):
        inp.append([int(i) for i in input().split()])
    print("#%d %d" % (t+1, minMove(N)))

