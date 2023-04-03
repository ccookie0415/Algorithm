def dfs(v):

    visited[v] = 1
    path.append(v)

    for e in adj[v]:
        if visited[e] == 0:
            dfs(e)

T = int(input())

for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    path = []

    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    dfs(1)
    print(f'#{tc}', *path)
