import sys
sys.stdin = open('전자카트.txt','r')

def find(n,total,current):
    global ans

    if n == N-1:
        if ans > total+arr[current][0]:
            ans = total + arr[current][0]
            return

    for j in range(1,N):
        if visited[j] == 0:
            visited[j] = 1
            find(n+1, total+arr[current][j],j)
            visited[j] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 99999999
    visited = [0] * N

    find(0, 0, 0)

    print(f'#{tc} {ans}')