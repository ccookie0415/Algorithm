def dfs(v, visited):
    global ans

    if len(visited) > ans:
        ans = len(visited)

    for e in adj[v]:
        if e not in visited:
            dfs(e, visited+[e])


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    ans = 0

    for _ in range(M):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    for i in range(1,N+1):
        dfs(i, [i])

    print(f'#{tc} {ans}')