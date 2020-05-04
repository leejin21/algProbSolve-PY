# binary2.py
# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

'''
0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.

N = 0.625
0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625

N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 소수점 아래가 12자리 이내인 N이 주어진다.


3
0.625
0.1
0.125

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 101
#2 overflow
#3 001
'''

'''sol
0.625
= 0.5*1 + 0.25*0 + 0.125*1

'''

# 여기서 어떻게 중복된 코드를 더 줄일 수 있을 지 모르겠음.
def binary2(num):
    # return '0.을 제외한 이진수' if num을 12자리 이내의 이진수로 표시 가능 else 'overflow'
    b = ''
    for i in range(1, 13):
        # 미리 dif 값 구해 보기
        dif = num - pow(2, -1*i)
        if dif > 0:
            num = dif
            b += '1'
        elif dif == 0:
            # dif 값이 0이 되는 경우 1 추가해주고 반복문 끝내기
            b += '1'
            return b
        else:
            b += '0'
    if num > 0:
        # 12자리 이내의 이진수로 표시 불가한 경우
        return 'overflow'


T = int(input())
for t in range(T):
    num = float(input())
    print("#%d %s" % (t+1, binary2(num)))
