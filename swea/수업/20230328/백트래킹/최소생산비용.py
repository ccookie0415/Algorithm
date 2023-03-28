import sys
sys.stdin = open('최소생산비용.txt','r')

def find(row, sum_):
    global ans

    if sum_ > ans:
        return

    if row == N:
        if sum_ < ans:
            ans = sum_

    for col in range(N):
        if visited[col] == 0:
            visited[col] = 1
            find(row+1,sum_+arr[col][row])
            visited[col] = 0


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 999999
    visited = [0] * N

    find(0,0)
    print(f'#{tc} {ans}')

