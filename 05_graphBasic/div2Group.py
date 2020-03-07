# div2Group.py
# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

'''문제

수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출하였다.

한 조의 인원에 제한을 두지 않았기 때문에, 한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 된다.

예를 들어 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다. 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

1번부터 N번까지의 출석번호가 있고, M 장의 신청서가 제출되었을 때 전체 몇 개의 조가 만들어지는지 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M, 다음 줄에 M 쌍의 번호가 주어진다. 2<=N<=100, 1<=M<=100

3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

class Node:
    def __init__(self, num, head):
        self.num = num
        self.head = head
        if head == None:
            self.nodel = []

    def addNode(self, node):
        self.nodel.append(node)

    def exist(self, num):
        # return True if 해당 헤드 노드의 자식 노드 중 num 값을 가지는 경우 else False
        for i in range(len(self.nodel)):
            if self.nodel[i].num == num:
                return True
        return False


def main():
    T = int(input())
    for t in range(T):
        num, pap = (int(i) for i in input().split())
        inp = [int(i) for i in input().split()]
        pairs = []
        for i in range(pap):
            pairs.append([inp[2*i], inp[2*i+1]])
            # print(pairs)
            # pairs는 2차원 리스트

        print("#%d %d"%(t+1, assign2Grp(num, pairs)))


def assign2Grp(num, pairs):
    # 그룹에 배정하기
    # return 그룹 수

    heads = []
    cnt = num
    # 0. 적히지 않은 번호의 경우는 cnt로 처리: cnt는 신청서에 적히지 않은 번호 개수

    for p in pairs:
        # 신청서에 적힌 번호1, 번호2가 기존 그룹들 중 존재하는 지
        ex1 = existInGrp(heads, p[0]); ex2 = existInGrp(heads, p[1])
        if p[0] == p[1]:
            # 1. 신청서에 적힌 번호가 서로 같은 경우
            heads.append(Node(p[0], None))
            cnt -= 1
        elif ex1==None and ex2==None:
            # 2. 기존 그룹들 중 존재하지 않는 케이스: 새로 그룹을 배정해 줌 이 중 p[0]을 head node로 삼음
            n = Node(p[0], None); n.addNode(Node(p[1], n))
            heads.append(n)
            cnt -= 2
        elif ex1 != None and ex2 == None:
            # 3. (1) 신청서에 적힌 쌍 중 번호1 이미 있는 경우: 번호1 그룹에 추가해주기
            ex1.addNode(Node(p[1], ex1))
            cnt -= 1
        elif ex1 == None and ex2 != None:
            # 3. (2) 신청서에 적힌 쌍 중 번호2 이미 있는 경우: 번호2 그룹에 추가해주기
            ex2.addNode(Node(p[0], ex2))
            cnt -= 1
        elif ex1 != ex2:
            # 4. 서로 다른 그룹 2개를 합칠 때: 같은 그룹일 수 있으니까 그 부분 생각해줘야 함.
            ex1.addNode(ex2)
            ex2.head = ex1
            for node in ex2.nodel:
                node.head = ex1
                ex1.addNode(node)
            ex2.nodel = []
            cnt -= 1

    return len(heads) + cnt


def existInGrp(heads, num):
    # O(n) 수행시간: 해시 탐색 이용하면 더 나아질 듯
    # return head node if 기존 그룹에서 num을 가지는 노드 찾음 else None
    for i in range(len(heads)):
        if heads[i].num == num or heads[i].exist(num) == True:
            # head 중 하나거나 head의 그룹 구성원 중 하나면 head node 반환
            return heads[i]
    return None

def showHeads(heads):
    for i in range(len(heads)):
        print(heads[i].num)


main()