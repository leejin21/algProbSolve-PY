# calculate.py
# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산
# 도전정신!!

'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.


[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

3
2 7
3 15
36 1007

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 3
#2 4
#3 8
'''

def main():
    T = int(input())
    for t in range(T):
        n, m = (int(i) for i in input().split())
        print("#%d %d"%(t+1, t))


def calHowMany(n, m, cnt):
    # 최소 몇 번의 연산을 거쳐야 하는 지: 꼭 prunning 작업 거쳐야 할 것 같음.
    global min_cnt
    cnt += 1
    print(n,m, cnt)
    if n==m:
        # 1. 만약 n=m 이면, min_cnt랑 비교해보고 업데이트해주기
        min_cnt = cnt if min_cnt > cnt else min_cnt
        print(cnt, min_cnt)
        
    elif cnt < min_cnt:
        # 2. 만약 n>m 이면, -10, -1 +1 *2 순으로 우선순위 정해 주기
        if n>m: pri = [-10, -1, +1, 2]
        # 3. 만약 n<m 이면, *2, +1, -10, -1 순으로 우선순위 정해 주기
        elif n<m: pri = [2, +1, -10, -1]

        for x in pri:
            # 우선순위에 따라 재귀함수 호출
            if x==2:
                print(x)
                calHowMany(n*2, m, cnt)
            else:
                print(x)
                calHowMany(n+x, m, cnt)


min_cnt = 1000001
calHowMany(5, 23, 0)