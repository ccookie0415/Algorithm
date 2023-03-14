def bfs(i,j):
    global total
    if 0 <= i < N and 0 <= j < N and arr[i][j] == 1 and visited[i][j] == 0:
        arr[i][j] = 0
        visited[i][j] = 1
        bfs(i, j+1)
        bfs(i, j-1)
        bfs(i+1, j)
        bfs(i-1, j)
        total += 1

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
ans = []
cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            total = 0
            cnt += 1
            bfs(i,j)
            ans.append(total)

ans.sort()
print(cnt)
for i in ans:
    print(i)