# quickSort.py
# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬
# 실패
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

# import random


def quickSort(nums, left, right):
    # recursive function
    # 1. partition을 통해 pivot의 올바른 idx를 구하고, pivot의 왼쪽에 pivot보다 작은 원소들, 오른쪽에 pivot보다 큰 원소들을 배치해 준  nums를 구한다.
    if left <= right:
        pi = partition(nums, left, right)
        # 2. nums의 left부터 pi-1, pi+1부터 right까지 다시 quickSort를 수행해서 재귀 수행.
        quickSort(nums, left, pi-1)
        quickSort(nums, pi+1, right)


def partition(nums, left, right):
    # sort nums list and returns n//2 th value of the list
    # end = random.randint(0, len(nums)-1)      # pivot index

    # 1. idx 설정해 주기(끝 원소로)
    end = right
    # 2. devide to left, right group(smaller, bigger), 기준은 pivot
    low = left
    high = right
    while(low <= high):
        # print(low, high, nums[low:high+1])
        while(nums[end] >= nums[low] and low < right):
            low += 1
        while(nums[end] <= nums[high] and high >= left):
            high -= 1
        # print(low, high)
        if low > high:
            break
        nums[low], nums[high] = nums[high], nums[low]

    # 3. 끝 원소랑 high+1번째 원소랑 swap
    nums[end], nums[high+1] = nums[high+1], nums[end]
    return high+1


T = int(input())
for t in range(T):
    _n = int(input())
    nums = [int(n) for n in input().split()]
    quickSort(nums, 0, len(nums)-1)
    print("#%d %d" % (t+1, nums[len(nums)//2]))


