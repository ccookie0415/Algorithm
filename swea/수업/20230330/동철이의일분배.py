import sys
sys.stdin = open('동철이의일분배.txt','r')

def find(n, total):
    global ans

    if ans >= total:
        return

    if n == N:
        if ans < total:
            ans = total
            return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            find(n+1, total*arr[n][j]*0.01)
            visited[j] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0
    find(0,1)

    print(f'#{tc} {ans*100:.6f}')
