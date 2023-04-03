import sys
sys.stdin = open('보급로.txt','r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

def find(x,y,total):
    global ans

    if total > ans:
        return

    if x == N-1 and y == N-1:
        if ans > total:
            ans = total

    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            find(ni, nj, total + arr[ni][nj])
            visited[ni][nj] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 999999999

    find(0,0,0)
    print(f'#{tc} {ans}')