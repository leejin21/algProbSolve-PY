# 내가 만든 알고리즘이 아님
# https://tothefullest08.github.io/algorithm/2019/08/31/4_5209_%EC%B5%9C%EC%86%8C%EC%83%9D%EC%82%B0%EB%B9%84%EC%9A%A9/
# 위 링크가 출처

def DFS(y, sum):
    global result, cnt
    cnt += 1
    print(y, sum, result, cnt)
    if y == N:
        if result > sum:
            result = sum
        return

    if result < sum:
        return

    for x in range(N):
        if not visited[x]:
            visited[x] = True
            DFS(y+1, sum + Data[y][x])
            visited[x] = False


TC = int(input())
for tc in range(1, TC+1):
    cnt = 0
    N = int(input())
    Data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    result = 987654321

    DFS(0, 0)
    print('#%d %d'%(tc, result))