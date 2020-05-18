# binary.py
# swexpertacademy programming advanced course 5185. 이진수
# 파이썬 SW문제해결 응용_구현 - 01 시작하기 1일차 6차시
# 성공 코드

'''[문제]
16진수 1자리는 2진수 4자리로 표시된다.
N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.
단, 2진수의 앞자리 0도 반드시 출력한다.
예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

0100011111111110

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100
16진수 A부터 F는 대문자로 표시된다.
 
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

'''[해결]
15->7->3->1
1
'''
class Binary:
    def __init__(self):
        # main()
        self.four = 4
        self.main()
        # self.showBin(1, ['FFFF'])

    def main(self):
        # main function: 입력 받고 출력 하기
        n = int(input())
        sixt = []
        for i in range(n):
            sixt.append(input())
        sixt = [s.split()[1] for s in sixt]
        # print(sixt)
        self.showBin(n, sixt)

    def showBin(self, n, sixt):
        # 출력하는 주요 함수, 재귀함수인 sixt2bin 함수 호출
        # print(sixt)
        sixt = [int(s, 16) for s in sixt]
            
        for i in range(n):
            print('#'+str(i+1), end = ' ')
            s = str(bin(sixt[i]))[2:]
            i = 4-len(s)%4+len(s) if len(s)%4 > 0 else len(s)
            k = '%0'+str(i)+'d'
            # print(k)
            print(k%int(s))
            # for j in sixt[i]:
            #     j = 10 + ord(j) - 65 if ord(j) >= 65 else int(j)
            #     # print('\n'+str(j))
            #     self.four = 4
            #     self.sixt2bin(j)
            
            # print()

    def sixt2bin(self, num):
        # 실패한 함수: 왜 실패했는 지는 모름!!
        # num이 0~9, A~F = 10~15
        # 16진수에서 바이너리로 변환하는 재귀함수
        # self.four는 16진수 자리 하나를 2진수 자리 4개로 바꾸기 위해 쓰인 포인터 개념의 변수(클래스를 쓴 이유)
        self.four -= 1
        # print(self.four)
        if num == 0: 
            # 몫이 0이면 중단, but self.four가 0이상인 경우 0일때까지 0을 출력(자릿수 4개 차지하기 위해)
            print('0', end = '')
            if self.four != 0: 
                for i in range(self.four, -1, -1):
                    print('0', end = '')
        else: 
            # 몫이 0 초과일 경우, num에서 2 나눈 몫을 재귀로 또 돌리기
            if self.four != 0: self.sixt2bin(num//2)
            # 이때 num의 나머지로 재귀해서 돌아온 차례에 출력(0 or 1)
            if num%2 == 0:
                print('0', end = '')
            else:
                print('1', end = '')
        
        
binary = Binary()
'''
3
4 47FE
5 79E12
8 41DA16CD


#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101

#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101

'''


