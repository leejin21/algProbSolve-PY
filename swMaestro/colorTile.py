'''입력
1
3 3
1 1 1
1 1 1
0 1 1

> YES
2
3 3
1 0 1
1 0 1
0 0 0
3 2
0 0
0 0
0 0

> NO

# 무조건 거기서 2*2는 다 1이어야 함
                if tile[x+1][y] == 0 or tile[x][y+1] == 0 or tile[x+1][y+1] == 0 and :
                    print(x, y)
                    return "NO"
'''
def okcolor(tile):
    hist = [[-1]*len(tile[0])]*len(tile)
    cnt = 0

    for x in range(len(tile)-1):
        for y in range(len(tile[x])-1):
            if tile[x][y] == 1 and tile[x+1][y] == 1 and tile[x][y+1] == 1 and tile[x+1][y+1] == 1:
                    hist[x][y] = hist[x][y+1] = hist[x+1][y] = hist[x+1][y+1] = cnt
                    cnt += 1
    # print(hist)
    # hist 기준으로 보기
    for x in range(len(tile)):
        for y in range(len(tile[x])):
            if hist[x][y] == -1 and tile[x][y] == 1:
                return "NO"
            
    return "YES"
            

T = int(input())
ans_list = []
for t in range(T):
    # 검사하지 않아도 되는 건 오른쪽 끝, 아래 끝
    inp = []
    x, y = (int(i) for i in input().split())
    for _ in range(x):
        inp.append([int(i) for i in input().split()])
    ans_list.append(okcolor(inp))

for ans in ans_list:
    print(ans)

