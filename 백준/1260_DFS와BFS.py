def dfs(adj,s,visited):
    visited[s] = 1
    dfs_lst.append(s)
    for e in adj[s]:
        if visited[e] == 0:
            dfs(adj,e,visited)

def bfs(s):
    q = []
    visited_2 = [0]*(N+1)
    q.append(s)
    visited_2[s] = 1

    while q:
        c = q.pop(0)
        bfs_lst.append(c)

        for n in adj[c]:
            if visited_2[n] == 0:
                q.append(n)
                visited_2[n] = 1

N,M,V = map(int,input().split())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)
bfs_lst = []
dfs_lst = []

for _ in range(M):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1,N+1):
    adj[i].sort()

dfs(adj,V,visited)
bfs(V)

print(*dfs_lst)
print(*bfs_lst)