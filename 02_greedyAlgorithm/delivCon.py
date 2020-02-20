# delivConv.py
# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

'''
화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.

트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.

컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.

이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.

화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 컨테이너 수 N과 트럭 수 M이 주어지고, 다음 줄에 N개의 화물이 무게wi, 그 다음 줄에 M개 트럭의 적재용량 ti가 주어진다.

1<=N, M<=100, 1<=wi, ti<=50

3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 8
#2 45
#3 84	
'''

def main():
    # 입력 받으면서 동시에 출력하기
    T = int(input())
    for _t in range(T):
        numL = [int(n) for n in input().split()]
        wiL = [int(w) for w in input().split()]
        tiL = [int(t) for t in input().split()]
        # print("numL=",numL,"wiL=",wiL,"tiL=", tiL)
        print("#%d"%(_t+1), makeMaxWeight(numL, wiL, tiL))

def makeMaxWeight(numL, wiL, tiL):
    # 쪼갤 수 없는 화물이므로 완전 탐색을 이용해서 구하기
    # numL은 안 쓰일 듯
    # wiL: 화물의 무게, tiL: 트럭의 적재용량
    wiL.sort(reverse=True)
    tiL.sort(reverse=True)
    # 트럭, 화물 큰->작은 순으로 정렬
    recL = [0]*len(tiL)
    # recL: 인덱스=트럭, 값=해당 트럭이 옮기는 화물의 무게

    wf_cnt = 0
    # 들어가야 할 화물 앞에서부터: wf_cnt, 뒤에서부터: wb_cnt
    r=0     # 트럭 번호
    while(r<len(recL) and wf_cnt < len(wiL)):
        # print("r=",r,"wf_cnt=", wf_cnt)
        if tiL[r] >= wiL[wf_cnt]:
            # 해당 트럭 용량 >= 화물 무게
            recL[r] = wiL[wf_cnt]
            wf_cnt += 1
            # 다음 화물로 넘어가기
            r+=1
            # 다음 트럭으로 넘어가기
        else:
            wf_cnt += 1
            # 다음 화물로 넘어가기


    return sum(recL)



main()