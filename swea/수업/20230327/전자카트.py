def dfs(n, sum_, current):
    global min_

    if min_ <= sum_:
        return

    if n == N:
        min_ = min(min_, sum_ + arr[current][1])
        return

    for j in range(2, N + 1):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n + 1, sum_ + arr[current][j], j)
            visited[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    min_ = 99999999
    visited = [0] * (N + 1)

    dfs(1, 0, 1)
    print(f'#{tc} {min_}')