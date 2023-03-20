import sys
sys.setrecursionlimit(10**7)

M,N,K = map(int,input().split())
arr = [[0]*N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ans = []
total = 0

def dfs(i,j):
    global cnt
    if 0<= i < M and 0 <= j < N and arr[i][j] == 0 and visited[i][j] == 0:
        visited[i][j] = 1
        cnt += 1
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())

    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1

for i in range(M):
    for j in range(N):
        cnt = 0
        if arr[i][j] == 0:
            dfs(i,j)
            if cnt != 0:
                ans.append(cnt)
ans.sort()
print(len(ans))
print(*ans)


