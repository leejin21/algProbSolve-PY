# minpcost.py
# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
# 완료
'''
A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.

각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.

예를 들어 3개의 제품을 생산하려는 경우 각 공장별 생산비용은 다음과 같이 주어진다..

   A  B  C
1 73 21 21
2 11 59 40
3 24 31 83

이때 1-C, 2-A, 3-B로 제품별 생산 공`장을 정하면 생산 비용이 21+11+31=63으로 최소가 된다.


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

'''sol
1. 다음 for문 늘 고려하기
(1) sum += inp_list[dep][j]
(2) visited[j] = False

2. 재귀함수: 종료조건 생각하기
(1) prunning(백트래킹 고려)
(2) leaf 노드일 때

3. 종료는 빨리 할 수록 좋음

'''

INF = 10000000
min = INF


def minCost(dep, sum):
    global min
    # 종료조건 1: prunning
    if sum > min:
        return
    # 종료조건 2: 깊이가 트리의 높이만큼일 때: 최대한 종료를 빨리 할 수 있으면 좋음.
    # FIXED: return문을 dep == len(inp_list) 바로 밑에 위치하니까 런타임 에러 해결, 리프 노드에서 for문 도는 게 생각보다 큰 시간을 소요하나 봄
    if dep == len(inp_list):
        if min > sum:
            min = sum
        return

    for j in range(len(inp_list[dep])):
        if visited[j] == False:
            # 자식 노드 중 미방문 노드만 방문하기
            visited[j] = True

            # 재귀 호출: FIXED: sum += inp_list[dep][j]는 오류 코드, 그러면 다음 for문에서도 sum이 이대로 반영됨
            minCost(dep+1, sum + inp_list[dep][j])

            # **다시 돌아왔을 때 다른 자식 노드 방문 가능하게 하는 밑작업(for문: 이미 방문한 자식 노드는 제외하고 다른 노드 방문하려고 함)**
            visited[j] = False


T = int(input())
for t in range(T):
    n = int(input())
    inp_list = []
    for _ in range(n):
        inp_list.append([int(i) for i in input().split()])
    visited = [False]*n
    min = INF
    minCost(0, 0)
    print("#%d %d" % (t+1, min))
