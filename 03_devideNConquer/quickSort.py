# quickSort.py
# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬

'''
퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.

5<=N<=1,000,000, 0 <= ai <= 1,000,000

2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, , N/2번 원소를 출력한다.

#1 2
#2 6
'''

import random 

def main():
    T = int(input())
    for t in range(T):
        _n = int(input)
        nums = [int(n) for n in input().split()]
        print("#%d %d"%(_n, quickSort(nums)[len(nums)//2]))

def quickSort(nums):
    # sort nums list and returns n//2 th value of the list
    # recursive function

    pi, nums = partition(nums)

    return nums


def partition(nums):
    idx = random.randint(len(nums))      # pivot index
    # devide to left, right group(smaller, bigger), 기준은 pivot
    i=0; j=0
    while(True):
        
        while(nums[idx] >= nums[i] and i<len(nums)):
            i+=1
        while(nums[idx] <= nums[j] and j>=0):
            j+=1

        nums[i], nums[j] = nums[j], nums[i]

        if j==i:
            # i==idx or j==idx일 경우 piv까지 간 것이므로 끝.
            nums[i], nums[idx] = nums[idx], nums[i]
            break
    

    return nums

main()