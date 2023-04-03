import sys
sys.stdin = open('보급로.txt','r')


di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs():

    while q:
        x,y = q.pop(0)

        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                if visited[x][y] + arr[ni][nj] < visited[ni][nj]:
                    visited[ni][nj] = visited[x][y] + arr[ni][nj]
                    q.append((ni,nj))

    return visited[N-1][N-1]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 999999999999
    visited = [[1e9]*N for _ in range(N)]
    q = [(0,0)]
    visited[0][0] = 0

    print(f'#{tc} {bfs()}')