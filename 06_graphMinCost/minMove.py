# minMove.py
# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리
# 방향 그래프

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
방향 그래프이므로: 각 node 객체마다 자식 노드로 둘 수 있게 하기
간선은 n개까지만 허용: cnt로
크루스칼 알고리즘으로 해결하기
'''

class Node:
    def __init__(self, num):
        self.num = num
        self.link = {}

    def addNode(self, node, weight):
        self.link[node] = weight

    def delNode(self, node):
        del self.link[node]


def main():
    T = int(input())
    for t in range(T):
        N, E = (int(i) for i in input().split())
        edgl = []
        for _ in range(E):
            edgl.append([int(i) for i in input().split()])
        print("#%d %d"%(t+1, minMove(N, edgl)))


def minMove(N, edgl):
    nodes = [Node(i) for i in range(N+1)]
    heads = nodes[:]
    edgl = sorted(edgl, key=lambda x: x[2])
    tot = 0; cnt = 0
    
    for ed in edgl:
        v1 = ed[0]; v2 = ed[1]; w = ed[2]
        print(v1, v2, w)
        if not linknCheck(v1, v2, w, nodes, heads):
            # 사이클이 안 생기는 경우
            tot += w
            cnt += 1
            print(cnt)
        if cnt == N+1:
            break
        showHeads(heads)
    return tot


def linknCheck(v1, v2, w, nodes, heads):
    # 1. v1 -> v2 방향으로 추가 먼저 해주기
    if heads[v2] != heads[v1]:
        nodes[v1].addNode(nodes[v2], w)
        tmp = heads[v2]
        heads[v2] = heads[v1]
        # 2. _checkCycle()로 사이클 생기는 지 확인하기
        if _checkCycle(nodes[v1], nodes[v1]) == True:
            # (1) 사이클 생기면 원래 상태로 복구 후 True return
            nodes[v1].delNode(nodes[v2])
            heads[v2] = tmp
            return True
        # (2) 사이클 안 생기면 False return
        return False
    
    return True


def _checkCycle(stt, temp):
    # return True if 사이클 생기면 else False
    # 사이클이 생기거나 이미 연결되어 있는 노드의 경우
    for node, _ in temp.link.items():
        print("stt:", stt.num,"temp:", temp.num,"node:", node.num)
        if node.num == stt.num:
            # 사이클 확인
            print("True1")
            return True
        elif _checkCycle(stt, node):
            print("True2")
            return True
    return False
            

def showHeads(heads):
    print("heads: ", end = " ")
    for i in heads:
        print(i.num, end = " ")
    print(" ")
main()