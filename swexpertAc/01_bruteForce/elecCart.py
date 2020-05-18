# eleCart.py
# swexpertacademy programming advanced course 5189. 전자카트
# 파이썬 SW문제해결 응용_구현 - 02 완전 검색 2일차 4차시
# 성공한 코드

'''
골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

**=> 이 경우 (len(inpList)-1)!의 경우를 각 구하기

e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91

e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89

[입력]

3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 
'''
import itertools
import sys

def main():
    # 입력 받으면서 동시에 출력하기
    T = int(input())
    for t in range(T):
        inpList = []
        N = int(input())
        for n in range(N):
            inpList.append([int(i) for i in input().split()])
        print("#%d"%(t+1), makeMinSum(inpList))

def makeMinSum(inpList):
    # return the minimum sum of the using battery if 
    perL = permMake(len(inpList))
    min = sys.maxsize
    for i in range(len(perL)):

        sum = 0
        fi = 0  # fi is the first index of inpList when adding to sum

        for j in range(len(perL[i])):
            la = perL[i][j]
            sum += inpList[fi][la]
            fi = la

        # last add is going back to #0
        sum += inpList[fi][0]
        # when min > sum, then sum is min
        min = sum if min > sum else min
        # print(min)
    return min


def permMake(n):
    # returns 2d list of (n-1)! of the permutations but customized to this problem(range part)
    if n > 1:
        # if need to use this in other code: change the range part
        m = map(list, itertools.permutations(range(1, n)))
        return list(m) 
    else:
        print("ERROR permMake n<=1")
        exit(1)


main()