# 배열 나누기
'''
6 3
4 8 15 16 23 42
> 12


'''
# 재귀로 제대로 풀기!! 틀린 문제

def divArr(arr, k):
    ptt = [0]*len(k)
    tot = 0; min_cost = 3000000000
    for i in range(1, len(arr)-(k-1)+1): 
        for j in range(i+1, len(arr)):
            
            tot = arr[i-1] - arr[0] + arr[j-1] - arr[i] + arr[len(arr)-1] - arr[j]
            if min_cost > tot: min_cost = tot

    return min_cost



N, K= (int(i) for i in input().split())
arr = [int(i) for i in input().split()]
print(divArr(arr, K))