# partStr.py
# 5254. [파이썬 S/W 문제해결 최적화] 1일차 - 부분 문자열
# 제한시간 초과
# 답지를 봐야 할 듯: 
'''
길이가 K인 문자열 S가 있을 때, S의 연속된 일부분을 부분 문자열이라고 한다.

부분 문자열은 원래의 순서가 바뀌거나 중간에 있는 글자가 빠져서는 안된다.

주어진 문자열의 부분 문자열을 사전순으로 정렬한 후, N번째 부분 문자열의 첫 글자와 글자 수를 출력하는 프로그램을 완성하시오.

예를 들어 abac의 부분 문자열은 사전순으로 정렬하면 다음과 같다.

a ab aba abac ac b ba bac c

3번째 부분 문자열은 aba가 된다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 다음 줄부터 각 줄에 N과 문자열이 주어진다.

문자열의 길이는 4글자 이상 1000글자 이내이고, N은 문자열의 길이 이내이다. ( 1<=T<=50 )

3
5 abac
9 ltsodjxzyc
21 jldgovukjf

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 a 2
#2 j 2
#3 j 4
'''
class Node:
    # 미완성
    def __init__(self, depth, pas):
        self.nodl = [None]*26
        self.depth = depth
        self.pas = pas
        

    def addNod(self, st):
        # 해당 노드의 nodl에 st[0] 추가해주고 재귀 호출해서 다음 노드에도 추가.,, 계속해서.
        if len(st) > 0:
            c = st[0]
            idx = ord(c) - ord('a')
            self.nodl[idx] = Node(self.depth+1, self.pas + c) if self.nodl[idx] == None else self.nodl[idx]
            self.nodl[idx].addNod(st[1:])
    
    def showchild(self):
        for alp, n in enumerate(self.nodl):
            if n != None:
                a = chr(alp+ord('a'))
                print(a, n.depth, end = " ")
        print(" ")
        for n in self.nodl:
            if n != None:
                n.showchild()

def findPart(n, word):
    # 트라이 이용
    # 1. 먼저 단어를 하나 받았을 때 해당 단어의 0번째, 1번째까지, ..
    head = Node(0, '')
    for i in range(len(word)):
        for j in range(i+1):
            # 단어의 j번째부터 i번째까지 트라이에 저장
            # print(j, i)
            head.addNod(word[j:i+1])
    # head.showchild()
    return _searchNode(head, n)

cnt = 0

def _searchNode(node, n):
    # 노드 검색하기
    global cnt, ch
    cnt += 1
    for i, nod in enumerate(node.nodl):
        if nod != None:
            if nod.depth == 1: ch = chr(i+ord('a'))
            # print(cnt, chr(i+ord('a')), nod.depth, ch, n)
            if n == cnt:
                # print(ch, nod.depth)
                return ch, nod.depth
            ans = _searchNode(nod, n)
            if ans != None:
                return ans

    return None



T = int(input())
for t in range(T):
    cnt = 0
    _input = input().split()
    n = int(_input[0]); word = _input[1].strip()
    # print(n, '"'+word+'"')
    cha, dep = findPart(n, word)
    print("#%d %s %d"%(t+1, cha, dep))

