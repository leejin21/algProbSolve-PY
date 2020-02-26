# minProdCost.py
# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
# used backtracking
# 제한시간 초과,, 왜 안되는 지 모르겠음 ㅠ

'''
A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.

각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.

예를 들어 3개의 제품을 생산하려는 경우 각 공장별 생산비용은 다음과 같이 주어진다..

이때 1-C, 2-A, 3-B로 제품별 생산 공장을 정하면 생산 비용이 21+11+31=63으로 최소가 된다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 제품 수 N이 주어지고, 이후 제품당 한 줄 씩 N개의 줄에 걸쳐 공장별 생산비용 Vij가 주어진다. 3<=N<=15,   1<=Vij<=99

3
3
73 21 21
11 59 40
24 31 83
5
93 4 65 31 66
63 12 60 60 84
87 57 44 35 20
12 9 40 12 40
60 21 3 49 54
6
55 83 32 79 53 70
77 88 80 93 42 29
54 26 5 10 25 94
77 92 82 83 11 51
84 11 21 62 45 58
37 88 13 34 41 4


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 63
#2 78
#3 129

'''


def main():
    global min_cost, MAX, cnt
    
    T = int(input())
    for t in range(T):
        N = int(input())
        costs = []; min_cost = MAX; cnt = 0
        # 매번 새로운 t마다 min_cost 초기화해주기
        for _n in range(N):
            costs.append([int(i) for i in input().split()])
        print("#%d %d"%(t+1, findMinCost(costs)))


def findMinCost(costs):
    # find minimum cost of costs list
    global min_cost

    _findMinCost(costs, 0, [0]*len(costs), 0)
    return min_cost

def _findMinCost(costs, depth, slt, tot):
    # depth is the depth of the tree(what depth is now)
    # slt is the selected number of the route
    # if costs[i][j]라고 하면, depth-1 == i, slt == j 이렇게 대응되는 개념으로.
    global min_cost, cnt
    cnt += 1
    org_tot = tot
    # print(depth+1, slt, tot, min_cost, cnt)

    if depth == len(costs):
        # 엣지 노드에 도달했을 때 tot가 min_cost보다 작은 경우 min_cost 새로 업데이트해 주기
        min_cost = tot if tot < min_cost else min_cost
    
    for j in findIndexs(slt, 0):
        slt_fake = slt[:]
        # slt를 해당 함수 동안 유지해 주고 slt_fake로 깊은 복사해서 다음 재귀(같은 케이스)는 slt_fake로 돌리기 위해 -> 이는 slt가 다음 for문의 케이스에 영향을 주지 않기 위해서 설정해 둔 것.
        slt_fake[j] = 1
        tot = org_tot
        # for문 돌면서 새로운 케이스이므로, tot도 새로 대입해줘야 함.
        tot += costs[depth-1][j]
        
        if tot < min_cost:
            # 제한시간 개선용: prunning 작업
            _findMinCost(costs, depth+1, slt_fake, tot)


def findIndexs(l, num):
    # l이라는 list에서 num이라는 게 어떤 인덱스에 있는지
    # returns list of indexs of num inside list l if l.count(num) > 0 else empty list
    pre_cnt = -1
    where = []
    for _i in range(l.count(num)):
        temp = l[pre_cnt+1:].index(num) + 1 + pre_cnt
        where.append(temp)
        pre_cnt = temp
    return where


MAX = 9223372036854775807
min_cost = MAX
cnt =0
main()
