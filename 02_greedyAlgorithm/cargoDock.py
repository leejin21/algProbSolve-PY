# cargoDock.py
# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크



'''
24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.

0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.

신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고, 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 신청서 N이 주어지고, 다음 줄부터 N개의 줄에 걸쳐 화물차의 작업 시작 시간 s와 종료 시간 e가 주어진다.

1<=N<=100, 0<=s<24, 0 ＜ e ＜= 24 


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''


def main():
    # 입력 받으면서 동시에 출력하기
    # 메인 함수
    T = int(input())
    for _t in range(T):
        totWork = []
        # 2d list of total work
        N = int(input())
        for n in range(N):
            totWork.append([int(x) for x in input().split()])
        
        print("#%d"%(_t+1), manyWork(totWork))

def manyWork(totWork):
    # used greedy algorithm to solve this problem
    # returns how many truck can use the dock

    # 1. sort totWork by endtime(1st idx) and secondly by start time(2nd idx)
    # start time에 대해서도 정렬을 진행했기 때문에 같은 end time을 가져도 start time을 비교해서 굳이 그걸 저장할 필요가 없었음.
    totWork.sort(key=lambda x: (x[1], x[0]))
    print(totWork)
    # 2. select work which end time is the earliest
    cnt = 0; las_end = -1; n = 0
    # cnt: returning number of total work, las_end: the end time of last work, n: for the while loop
    while(n<len(totWork)):
        # 다른 end time을 가지게 되면 min_stt에 마지막으로 저장된 것 쳐서 cnt에 추가하고 min_stt 초기화
        if las_end <= totWork[n][0]:
            # save this work's starting time in min_stt and compare to other works which has same ending time
            las_end = totWork[n][1]
            print(totWork[n], las_end)
            cnt += 1
        n += 1
    return cnt

main()

'''
zip(*list) 배움: 이거 쓰면 리스트 transpose 가능
lambda x: (x[1], x[0])
이거 진짜...
관련 링크: https://dailyheumsi.tistory.com/67

'''