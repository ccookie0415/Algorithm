def dfs(i, j):
    if 0 <= i < N and 0 <= j < N and arr[i][j] != 0:
        if visited[i][j] == 0:
            arr[i][j] = 0
            visited[i][j] = 1
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i - 1, j + 1)
            dfs(i - 1, j - 1)
            dfs(i + 1, j)
            dfs(i + 1, j + 1)
            dfs(i + 1, j - 1)
            return True
    return False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [([0] * N) for _ in range(N)]
    cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            start_i = i
            start_j = j
            if dfs(start_i, start_j) == True:
                cnt += 1
print(f'#{tc} {cnt}')