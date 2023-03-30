import sys
sys.stdin = open('전자카트.txt','r')

def find(n,total,current):
    global ans

    if total >= ans:
        return

    if n == N-1:
        if total + arr[current][0] < ans:
            ans = total + arr[current][0]
        return

    for j in range(1,N):
        if visited[j] == 0:
            visited[j] = 1
            find(n+1, total + arr[current][j], j)
            visited[j] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 999999999
    find(0,0,0)

    print(f'#{tc} {ans}')