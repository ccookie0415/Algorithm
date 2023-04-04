import sys
sys.stdin = open('최소비용.txt','r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs():

    while q:
        x,y = q.pop(0)

        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                plus = 0
                if arr[x][y] < arr[ni][nj]:
                    plus = arr[ni][nj] - arr[x][y]

                if visited[ni][nj] > visited[x][y] + plus + 1:
                    visited[ni][nj] = visited[x][y] + plus + 1
                    q.append((ni,nj))


    return visited[N-1][N-1]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[1e9]*N for _ in range(N)]
    q = [(0,0)]
    visited[0][0] = 0

    print(f'#{tc} {bfs()}')