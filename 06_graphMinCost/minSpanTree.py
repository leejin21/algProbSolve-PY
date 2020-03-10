# minSpanTree.py
# [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리
# 크루스칼 알고리즘 이용, 무방향 그래프: 이걸 어떻게 구현해야 할까...
'''
*무방향 그래프인 듯

그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.

다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다. 

1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000

3
2 3
0 1 1
0 2 1
1 2 6
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

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 2
#2 13
#3 22

'''

'''sol
1. 크루스칼 알고리즘으로, 간선 선택을 기반으로
2. 간선을 오름차순으로 정렬 후 간선 하나씩
    (1) 사이클 생성 확인
    (2) if 사이클=False:
        heads에서 해당 노드 찾아낸 후 상대 노드와 이어주기
3. 사이클 생기는 경우 케이스
    (1) 노드들에 간선이 또 부여됐을 때 => 어떻게 할 지 고민
    (2) 한바퀴 돌아와서 또 그 노드가 나타날 때

'''

class Node:
    def __init__(self, num):
        self.visit = False
        self.num = num
        self.nexd = {}

    def addNode(self, node, weight):
        # self 노드와 node 노드를 서로 연결해 줌: 가중치 포함
        self.nexd[node] = weight
        node.nexd[self] = weight

    def delNode(self, node):
        # self 노드와 node 노드 분리해 줌
        del self.nexd[node]
        del node.nexd[self]

    def showNextlist(self):
        # 해당 노드에 연결된 노드들 print해주기(테스트 위해)
        print(self.num, end = ": ")
        for n, w in self.nexd.items():
            print("%d:%d"%(n.num, w), end = " ")
        print("")

def main():
    # 메인 함수
    T = int(input())
    for t in range(T):
        num, edge = (int(i) for i in input().split())
        edgl = []
        for _e in range(edge):
            edgl.append([int(i) for i in input().split()])
        print("#%d %d"%(t+1, kruskal(num, edgl)))


def kruskal(n, edgl):
    # return 총 가중치
    heads = makeNodes(n)
    # heads는 각 노드들을 담은 리스트
    edgl = sorted(edgl, key=lambda x: x[2]) # 가중치의 오름차순으로 edgl 정렬해 줌
    tot = 0; cnt = 0
    # 연결한 간선의 수가 노드의 수를 넘어갈 경우
    for e in edgl:
        v1 = e[0]; v2 = e[1]; w = e[2]
        if not linknCheck(v1, v2, w, heads):
            tot += w
            cnt += 1
        if cnt == n:
            break
        
    # for node in heads:
        # node.showNextlist()
    return tot


def makeNodes(n):
    nodel = [Node(i) for i in range(n+1)]
    return nodel


def linknCheck(v1, v2, w, heads):
    # return True if 사이클 생성될 때, else False
    '''
    * 기능 1. 사이클 생성 안하는 경우 노드끼리 연결도 해 줌
    * 기능 2. 사이클 생성 확인: v1 => v2를 연결했을 때, v1에서 시작한 게 v1으로 되돌아오는 지 체크: use recursive function
    '''
    # 0. 기존에 이미 연결된 간선인 경우: 간선의 가중치가 같거나 클 것이기 때문에 무시.
    if heads[v2] not in list(heads[v1].nexd.keys()):
        # 1. 연결 먼저 하고 _checkCycle 이용해서 사이클 생기는 지 확인
        heads[v1].addNode(heads[v2], w)
        ans = _checkCycle(heads[v1], heads[v1], heads[v1])
        # 2. 연결 해제할 지 말지도 결정해 줌
        if ans == True:
            # (1). if 사이클이 생기면: 원상대로 복구
            heads[v1].delNode(heads[v2])
            return True
        # (2). else: 복구 안 해 줌
        return False

def _checkCycle(first, temp, pre):
    # return True if 현재/다음 노드에서 사이클 발견, else False
    ''' 재귀 함수 항상 확인할 것
    * 종결 조건 확인
    * 객체 이름 가리키는 변수가 그대로 가리키는 듯. 아무 무리 없이 잘 작동: 아마 지역 변수로 적용되어서 그런 듯?
    '''
    for node, _weig in temp.nexd.items():
        if node.num != pre.num:
            # 무방향 그래프이므로 연결된 노드들에는(nexd) 전에 방문했던 노드도 포함됨. 해당 노드를 제외시켜야 함
            # ==> temp에 연결된 노드들 중 직전 방문 노드(pre) 제외한 노드 방문하기
            if first.num == node.num:
                # (1) 지금 turn에서 처음 노드로 다시 돌아간 경우 즉 지금 turn에서 사이클 확인
                return True
            elif _checkCycle(first, node, temp):
                # (2) 다음 turn에서 이미 처음 노드로 돌아간다는 걸 확인한 경우 or 다음 turn에서 사이클 생기는 것 이미 확인한 것
                return True
    return False

def showHeads(heads):
    print("heads list: ", end = " ")
    for i in heads:
        print(i.num, end = " ")
    print(" ")

main()

