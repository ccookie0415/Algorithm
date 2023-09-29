def dfs(s):
    for e in adj[s]:
        if visited[e] == 0:
            visited[e] = 1
            path.append(e)
            dfs(e)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    path = []

    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)

    S, G = map(int, input().split())

    visited[S] = 1
    path.append(S)

    dfs(S)

    if G in path:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')