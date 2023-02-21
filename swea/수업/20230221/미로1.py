import sys
sys.stdin = open('미로1.txt' ,'r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

T = 10

for tc in range(1,T+1):
    tc_num = int(input())
    N = 16
    arr = [list(map(int,input())) for _ in range(N)]
    visited = [([0] * N) for _ in range(N)]
    q = []
    ans = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_i = i
                start_j = j

    q.append((start_i,start_j))
    visited[start_i][start_j] = 1


    while q:
        i,j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni,nj))
            if arr[ni][nj] == 3 and visited[ni][nj] == 0:
                ans = 1
                break
    print(f'#{tc} {ans}')

