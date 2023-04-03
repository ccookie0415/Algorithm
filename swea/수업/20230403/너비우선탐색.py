def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        t = q.pop(0)
        path.append(t)

        for e in adj[t]:
            if visited[e] == 0:
                q.append(e)
                visited[e] = 1


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    path = []

    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    bfs(1)
    print(f'#{tc}', *path)