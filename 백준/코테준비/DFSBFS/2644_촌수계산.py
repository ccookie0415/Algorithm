def dfs(s,cnt):
    cnt += 1
    visited[s] = 1

    if s == B:
        ans.append(cnt)

    for e in adj[s]:
        if visited[e] == 0:
            dfs(e,cnt)


N = int(input())
A,B = map(int,input().split())
M = int(input())
adj = [[] for _ in range(N+1)]
visited=[0] * (N+1)
ans=[]
cnt = -1

for _ in range(M):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

dfs(A,cnt)

if len(ans) == 0:
    print(-1)
else:
    print(*ans)
