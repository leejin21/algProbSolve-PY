# elecBus2.py
# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2
# 성공

'''
충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.

충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.

정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.

다음은 1번에서 출발 5번이 종점인 경우의 예이다.

1번에서 장착한 충전지 용량이 2이므로, 3번 정류장까지 운행할 수 있다. 그러나 2번에서 미리 교체하면 종점까지 갈 수 있다.

마지막 정류장에는 배터리가 없다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 한 줄에 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi가 주어진다. 3<=N<=100, 0 ＜ Mi ＜ N

3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다

#1 1
#2 2
#3 5
'''

# global 변수
MAX = 110


class ElecBus2:
    def __init__(self):
        self.main()

    def main(self):
        T = int(input())
        for t in range(T):
            self.minCnt = MAX
            _list = [int(i) for i in input().split()]
            _num = _list[0]; bat_l = _list[1:] + [0]
            self.calMinRep(bat_l)
            # 1번에서의 장착은 횟수에서 제외.
            print("#%d %d"%(t+1, self.minCnt-1))


    def calMinRep(self, bat_l):
        # return 교체횟수
        # call recursive function
        rep_l = [0]*(len(bat_l))
        # 1. 일단 첫 정류장에서는 무조건 배터리 장착하기
        b_cnt = bat_l[0]; rep_l[0] = 1
        # 2. 다음 정류장부터는 b_cnt에서 -1씩 해주고 보내주기, 전역 변수는 b_cnt가 재귀를 부르거나 부모노드로 갈 때마다 달라질 수 있으므로 안 씀

        return self._minRep(bat_l, b_cnt, rep_l, 1)


    def _minRep(self, bat_l, b_cnt, rep_l, depth):
        # print(rep_l, sum(rep_l), self.minCnt)
        if depth == len(bat_l):
            cnt = sum(rep_l)
            self.minCnt = cnt if self.minCnt > cnt else self.minCnt
            # print(rep_l, self.minCnt)
        elif b_cnt >= 1 and sum(rep_l) < self.minCnt:
            # print(rep_l, self.minCnt)
            # 마지막에도 되는 지 체크하기
            b_cnt -= 1
            # 1. 이번 정류장에서 배터리 교체 안하는 경우: b_cnt에서 -1만 해서 다음 recursion 부르기
            rep_l[depth:] = [0]*(len(rep_l)-depth)
            self._minRep(bat_l, b_cnt, rep_l, depth+1)
            # 2. 이번 정류장에서 배터리 교체 하는 경우: b_cnt 자리에 새 배터리 넣어주기
            # 마지막 정류장 제외
            rep_l[depth:] = [0]*(len(rep_l)-depth)
            if depth != len(bat_l)-1:
                rep_l[depth] = 1
                self._minRep(bat_l, bat_l[depth], rep_l, depth+1)
            
ElecBus2()