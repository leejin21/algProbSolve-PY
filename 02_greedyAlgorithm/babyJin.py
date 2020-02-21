# babyJin.py
# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임

'''

0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.

두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.

이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 각 줄에 0에서 9사이인 12개의 숫자가 주어진다.

3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
 
[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 0
#2 1
#3 2
'''

def main():
    T = int(input())
    for t in range(T):
        card_set = [int(card) for card in input().split()]
        print("#%d %d"%(t+1,findWinner(card_set)))

def findWinner(card_set):
    # 승자를 알아내는 함수:
    ply1 = []; ply2 = []
    # 1. ply1, ply2에게 카드 분배해 주면서 run, triplet인지 확인하기
    winner = 0
    for i in range(len(card_set)):
        if i % 2 == 0:
            # 1.(1) i가 짝수일 경우: ply1이 뽑은 카드
            ply1.append(card_set[i])
            if checkRT(ply1):
                winner = 1
                break
            
        else:
            # 1.(2) i가 홀수일 경우: ply2이 뽑은 카드
            ply2.append(card_set[i])
            if checkRT(ply2):
                winner = 2
                break
    return winner

    
def checkRT(ply_set):
    # returns True if checks run or triplet, else False
    # 현재 ply_set=카드 세트에서 run, triplet가 있는 지 알아내는 함수
    # 문제점: triplet 카운트할 때 3번 연속으로 kind >= 1인 걸 해야 함
    if len(ply_set) < 3:
        # 전체 카드 수가 3개 미만이면 run, triplet 될 수 없으므로
        return False

    card_kind = [0]*10
    # 각 인덱스번호별로 ply_set의 숫자별 몇개 있는 지
    # 예: ply_set=[0,1,2], card_kind=[1,1,1,0,,]
    for num in ply_set:
        card_kind[num] += 1

    tri_cnt = 0 # 연속 세는 변수(for triplet)
    for kind in range(len(card_kind)):
        if card_kind[kind] == 3:
            # 1. check if run
            # triplet과 run 둘 다 해당되는 경우 생각할 필요 없음
            return True
        elif card_kind[kind] >= 1:
            if tri_cnt == 0:
                # 2.(1) triplet check: card_kind에서 1 이상인 첫 kind일 때
                tri_cnt += 1
            
            elif (tri_cnt >= 1 and card_kind[kind-1]>=1):
                # 2.(2) card_kind: card_kind에서 직전 kind(=kind-1)이 1개 이상이었을 때
                tri_cnt += 1
                
            if tri_cnt == 3:
                # 2.(3) triplet이 되는 경우
                return True
        else:
            # 연속이 끊길 경우 tri_cnt = 0(처음부터 다시 세기)
            tri_cnt = 0

    return False
    


main()