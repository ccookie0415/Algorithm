import sys
sys.stdin = open('미로.txt','r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    visited = [([0] * N) for _ in range(N)]
    ans = 0
    q = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i,j)

    visited[start[0]][start[1]] = 1
    q.append(start)

    while q:
        i,j = q.pop(0)
        if arr[i][j] == 3:
            ans = 1
            break
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                if arr[ni][nj] == 0 or arr[ni][nj] == 3:
                    visited[ni][nj]=1
                    q.append((ni,nj))

    print(f'#{tc} {ans}')
