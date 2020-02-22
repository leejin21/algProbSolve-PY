# mergeSort.py
# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬
'''
알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.

정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.

N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.

병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.

정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.

알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.


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

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,  N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력한다.
'''
class mergeSort:
    def __init__(self):
        self.main()

    def main(self):
        # main function
        T = int(input())
        for t in range(T):
            _N = int(input())
            nums = [int(i) for i in input().split()]
            self.cnt = 0
            print("#%d %d %d"%(t+1, self.mergeSort(nums)[len(nums)//2], self.cnt))

    def mergeSort(self, nums):
        # returns sorted nums as list
        # recursive function
        if len(nums)==1: return nums
        # 0. if 원소==1: return 그거 하나(형태는 리스트)
        else:
        # 1. divide the nums into left and right
            left = self.mergeSort(nums[0:len(nums)//2])
            right = self.mergeSort(nums[len(nums)//2:len(nums)])
            return self.merge(left, right)

    def merge(self, left, right):
        # left, right가 정렬되어있는 상태이므로 둘 합치면서 오름차순으로 정렬
        tot = []
        i=0; j=0
        while(i<=len(left)-1 and j<=len(right)-1):
            # print("i=%d, j=%d"%(i,j))
            # 1. i, j는 아직 안 담은 값을 가리키는 인덱스, 각각 left, right list 담당
            if left[i] <= right[j]:
                tot.append(left[i])
                i+=1
            else:
                # 교수가 지시한 사항: 크거나 같 X, 크다
                tot.append(right[j])
                j+=1
        # 2. 남은 left, right tot에 append해주기
        while(i<=len(left)-1):
            # left의 마지막 부분이 남은 것(right보다 크기 때문)
            # left의 마지막이 right의 마지막보다 큰 경우: cnt에 추가
            if i == len(left)-1:
                self.cnt += 1
            tot.append(left[i])
            i+=1
        while(j<=len(right)-1):
            # right의 마지막 부분이 남은 것(left보다 크거나 같기 때문)
            tot.append(right[j])
            j+=1
        # print(tot)
        return tot

            
mg = mergeSort()


'''
여기서 좀 더 꼬으면 머지소트라는 걸 힌트로 안 주고 그냥 구하라고 할 수 도 있을 것 같다.
'''


