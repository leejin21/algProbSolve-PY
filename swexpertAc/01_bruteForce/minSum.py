# minSum.py
# swexpertacademy programming advanced course 5188. 최소합
# 파이썬 SW문제해결 응용_구현 - 02 완전 검색 2일차 3차시
# 성공한 코드, 테스트케이스 1개 기준 O(n^2)

'''
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 **오른쪽이나 아래로만** 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 **이때의 합계가 얼마인지** 출력하는 프로그램을 만드시오.
 
1 2 3
2 3 4
3 4 5


그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13

3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1

 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''

import copy as cp

def main():
    # 입력 받으면서 동시에 출력하기
    T = int(input())
    for t in range(T):
        inpList = []
        N = int(input())
        for n in range(N):
            inpList.append([int(i) for i in input().split()])
        print("#%d"%(t+1), makeMinSum(inpList)[N-1][N-1])

def makeMinSum(inpList):
    # return minSuml: 해당 자리까지 오는 최소 비용들 써 둔 리스트
    minSuml = cp.deepcopy(inpList)
    for i in range(len(inpList)):
        for j in range(len(inpList[i])):
            if i==0 and j==0:
                # 위, 왼쪽 경로가 막힌 경우(=start 지점일 때): 지금자리
                minSuml[i][j] = inpList[i][j]
            elif i==0:
                # 위 경로가 막힌 경우: 왼쪽 + 지금자리
                minSuml[i][j] = minSuml[i][j-1] + inpList[i][j]
            elif j==0:
                # 왼쪽 경로가 막힌 경우: 위쪽 + 지금자리
                minSuml[i][j] = minSuml[i-1][j] + inpList[i][j]
            else:
                # 아무것도 안 막힌 경우: min(왼쪽,위쪽) + 지금자리
                minSuml[i][j] = min(minSuml[i][j-1], minSuml[i-1][j]) + inpList[i][j]
    # print("minSuml")
    # showList(minSuml)
    return minSuml

def showList(minSuml):
    # not used: only for checking the function makeMinList
    for i in range(len(minSuml)):
        for j in range(len(minSuml[i])):
            print(minSuml[i][j], end = " ")
        print("")


main()