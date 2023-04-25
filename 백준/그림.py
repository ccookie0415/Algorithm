import sys
sys.setrecursionlimit(10**7)

def dfs(i,j):
    global max_
    global cnt

    if 0 <= i < n and 0 <= j < m and arr[i][j] == 1 and visited[i][j] == 0:
        visited[i][j] = 1
        arr[i][j] = 0
        cnt += 1
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

        if cnt > max_:
            max_ = cnt

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
max_ = 0
ans_ = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt = 0
            ans_ += 1
            dfs(i,j)


if n==1 and m==1:
    ans_ = 0
    max_ = 0
    print(ans_)
    print(max_)

else:
    print(ans_)
    print(max_)