import sys
sys.setrecursionlimit(10**7)

def bfs(i,j):
    global max_
    global total
    if 0 <= i < N and 0 <= j < M and arr[i][j] == 1 and visited[i][j] == 0:
        total += 1
        visited[i][j] = 1
        arr[i][j] = 0
        bfs(i+1, j)
        bfs(i-1, j)
        bfs(i, j+1)
        bfs(i, j-1)
        if total > max_:
            max_ = total

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
max_ = 0
cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            total = 0
            cnt += 1
            bfs(i,j)

if N==1 and M==1:
    cnt = 0
    max_ = 0
    print(cnt)
    print(max_)
else:
    print(cnt)
    print(max_)
