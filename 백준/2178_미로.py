di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i,j):
    visited[i][j] = 1
    q.append((i,j))

    while q:
        i,j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni,nj))


N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = []

bfs(0,0)

print(visited[N-1][M-1])