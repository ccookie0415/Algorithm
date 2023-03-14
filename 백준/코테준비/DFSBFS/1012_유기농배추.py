import sys
sys.setrecursionlimit(10**7)

def bfs(i,j):
    if 0<=i<N and 0<=j<M and arr[i][j] == 1:
        arr[i][j] = 0
        bfs(i-1, j)
        bfs(i+1, j)
        bfs(i, j-1)
        bfs(i, j+1)

T = int(input())

for tc in range(1,T+1):
    M,N,K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        j,i = map(int,input().split())
        arr[i][j] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i,j)

    print(cnt)
