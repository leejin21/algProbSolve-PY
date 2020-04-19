# sortedSubset.py
# 5262. [파이썬 S/W 문제해결 최적화] 4일차 - 정렬된 부분 집합
# 완료

'''
N개의 서로 다른 자연수를 원소로 갖는 집합에서, 부분집합을 만들었다.

이때 원소 사이의 순서가 원래 집합에서의 순서와 일치하고, 오름 차순 정렬을 해도 원소의 순서가 바뀌지 않는 경우가 있다.

이 중 원소의 개수가 가장 많은 부분집합의 원소 개수를 출력하는 프로그램을 만드시오.

예를 들어 처음 주어진 집합이 {1, 3, 2, 4}인 경우 조건에 해당하는 부분 집합은 {1, 3, 4}와 {1, 2, 4}이므로, 원소의 개수는 3이 된다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로, 원소의 개수 N과 N개의 자연수 ai가 한 줄에 주어진다.

1<=T<=50, 1<=N, i<=1000, 1<=ai<=N

3
5 1 5 3 4 2
5 4 3 5 1 2
10 2 9 5 1 10 6 3 4 8 7

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.

#1 3
#2 2
#3 4
'''

# 최장증가수열(LSP) 문제


def sorSub(eles):
    lis = [0]*len(eles)
    c_list = [0]
    # c_list는 index에 수열 원소가 가지는 lis 값을 구하는 데 도움을 주는 역할
    for i, e in enumerate(eles):
        si = bsforSorSub(c_list, e)     # save용 index
        if len(c_list) <= si:
            # c_list의 길이 확인하고 늘려야 하면 늘리기(최대 수열의 원소)
            c_list.append(e)
        else:
            # 늘릴 필요 없으면 si 부분에 저장
            c_list[si] = e
        # lis는 동일 idx에서 eles의 val의 최장증가수열의 길이 저장하는 리스트
        lis[i] = si

    return max(lis)


def bsforSorSub(c_list, e):
    # binarySearch function
    # return c의 index+1 which index의 val가 val < e인 최대 수일 때
    l = 0
    r = len(c_list)-1
    med = (l+r)//2
    while(l <= r):
        if c_list[med] > e:
            r = med - 1
        elif c_list[med] < e:
            l = med + 1
        else:
            return med
        med = (l+r)//2
    # different with general binarySearch: med"+1"
    return med + 1


T = int(input())
for t in range(T):
    eles = [int(i) for i in input().split()]
    print("#%d %d" % (t+1, sorSub(eles)))
