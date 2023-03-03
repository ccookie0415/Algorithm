import sys
sys.stdin = open('stack.txt','r')

def dfs(s):
    for e in adj[s]:
        if visited[e] == 0:
            path.append(e)
            visited[e] = 1
            dfs(e)


T = int(input())

for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    path = []
    stack = []

    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)

    visited[1] = 1
    path.append(1)

    dfs(1)
    print(path)