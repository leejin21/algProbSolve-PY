# happyBox.py
'''
일정액을 내면 크기가 정해진 박스가 가득 찰 때까지 마음대로 물건을 골라 담을 수 있는 해피박스 이벤트가 열린다고 한다.

A씨는 박스에 담긴 물건의 가격합계가 최대가 되도록 물건을 담으려고 한다.

A씨 차례에 남은 물건의 크기와 가격이 주어질 때, A씨가 담을 수 있는 물건 가격은 최대 얼마인지 알아내는 프로그램을 작성하시오.

담긴 상품 크기의 합이 박스 크기를 초과할 수 없고, 각 상품은 1개씩 있다. A씨가 고르는 동안 다른 사람이 가져갈 수는 없다.

예를 들어 박스의 크기가 10이고 상품의 크기와 가격이 다음과 같다면, 최대로 담을 수 있는 가격 합계는 2번과 3번을 담았을 때인 25이다.

상품 | 크기 | 가격
  1     6     12
  2     5     10
  3     5     15
  4     4     6


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로, 첫 줄에 박스의 크기 N과 상품의 개수 M이, 이후 M개의 줄에 걸쳐 상품 i의 크기Si와 가격Pi가 주어진다.
10<=N<=100, 1<= Si, Pi, M<=20

2
10 4
6 12
5 10
5 15
4 6
12 5
7 20
3 10
5 3
3 8
6 15

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''

# 점화식 이용
'''식
K[i][w]: w 크기의 가방에 물건 i까지의 물건들을 최대 이익으로 넣었을 때의 최대 이익
case 1) K[i-1][w-wi] + vi
case 2) K[i-1][w]
K[i][w] = max(case 1, case 2)
'''


def happyBox(bag, item):
    max_prof = [[0 for j in range(bag+1)] for i in range(len(item)+1)]
    # print(len(max_prof), len(max_prof[0]))
    # print('item=', item)
    for i in range(1, len(item)+1):
        # i는 item의 i번째 물건
        # FIXED: item은 인덱스가 0부터 시작하므로 -1씩 해 줘야 함.
        cur_size = item[i-1][0]
        cur_val = item[i-1][1]
        for j in range(1, bag+1):
            # j는 bag에서 1,2,3,..bag (가방이 j만큼의 허용 공간이 있을 때를 생각)
            if j-cur_size >= 0:
                case1 = max_prof[i-1][j-cur_size]+cur_val
                case2 = max_prof[i-1][j]
                max_prof[i][j] = max(case1, case2)
            else:
                # 가방에 cur_size만큼의 공간이 없을 때 최대 이익은 0으로.
                max_prof[i][j] = max_prof[i-1][j]

    return max_prof[len(item)][bag]


T = int(input())
for t in range(T):
    N, M = (int(i) for i in input().split())
    item = []
    for m in range(M):
        item.append([int(j) for j in input().split()])
    # happyBox(N, item)
    print("#%d %d" % (t+1, happyBox(N, item)))
