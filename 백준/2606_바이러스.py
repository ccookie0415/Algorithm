def dfs(s):
    visited[s] = 1
    path.append(s)

    for e in adj[s]:
        if visited[e] == 0:
            dfs(e)


N = int(input())
V = int(input())
visited = [0] * (N+1)
adj = [[] for _ in range(N+1)]
path = []
cnt = 0

for _ in range(V):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

dfs(1)

for i in path:
    if i != 1:
        cnt += 1

print(cnt)
