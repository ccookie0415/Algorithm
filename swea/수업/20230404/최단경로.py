def dijkstra(s, e):
    D = adj[s][::]  # 복사
    visited = [0] * N
    visited[s] = 1

    for _ in range(N - 1):
        min_, i_min = 100000000, 0
        for j in range(N):
            if visited[j] == 0 and min_ > D[j]:
                min_, i_min = D[j], j

        visited[i_min] = 1

        for j in range(N):
            D[j] = min(D[j], D[i_min] + adj[i_min][j])

    return D[e]


T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[100000000] * N for _ in range(N)]

    for _ in range(E):
        s, e, p = map(int, input().split())
        adj[s][e] = p

    for i in range(N):
        adj[i][i] = 0

    ans = dijkstra(0, N - 1)

    print(f'#{tc} {ans}')