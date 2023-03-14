di = [1,2,2,1,-1,-2,-2,-1]
dj = [-2,-1,1,2,2,1,-1,-2]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visited =[[0] * N for _ in range(N)]
    start_i,start_j = map(int,input().split())
    end_i,end_j = map(int,input().split())
    tmp = 0
    q = []
    q.append((start_i,start_j))
    visited[start_i][start_j] = 1

    while True:
        i,j = q.pop(0)
        if i == end_i and j == end_j:
            break

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni,nj))

    print(visited[end_i][end_j]-1)







