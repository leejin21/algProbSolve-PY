# binarySearch.py
# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색
# *문제를 잘 읽어야 한다는 걸 일꺠워줌*

'''
서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다. 그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.

전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m=(l+r)//2 이고, 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.

이때 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.

다음은 10개의 정수가 저장된 리스트 A에서 이진 탐색으로 6을 찾는 예이다.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 A와 B에 속한 정수의 개수 N, M이 주어지고, 두 줄에 걸쳐 N개와 M개의 백만 이하의 양의 정수가 주어진다.

1<=N, M<=500,000

3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

# list A에서 B에 들어 있는 원소 검색하기(이진 검색)
def main():
    T = int(input())
    for t in range(T):
        _a, _b = (int(i) for i in input().split())
        alist = sorted([int(i) for i in input().split()])
        blist = [int(i) for i in input().split()]
        
        # print("alist=",alist)
        print("#%d %d"%(t+1, binarySearch(alist, blist)))


def binarySearch(alist, blist):
    # return blist의 요소 중 alist에도 포함되는 게 얼마나 있는 지
    # 반복문 이용
    cnt = 0
    for e in blist:
        # use recursive function _bS
        cnt += loop_bS(alist, e)
        
    return cnt


def loop_bS(alist, e):
    # loop function
    l = 0; r = len(alist)-1
    turn = 0
    while(l<=r):
        med = (r+l)//2
        # print(l, med, r)
        if alist[med] == e:
            return 1
        elif alist[med] < e:
            l = med + 1
            if turn == 1: break
            turn = 1
        else:
            r = med - 1
            if turn == -1: break
            turn = -1

    return 0



main()
# print(loop_bS([2,4,6,8,10,12,14,16,18], 18))