s, e = 시작노드, 도착노드

E = 순서쌍 개수
adj = [[] for _ in range(V+1)]

for _ in range(E):
    adj[s].append(e)
    adj[e].append(s)



def dfs_stk(start):
    visited = [0] * (V+1)
    stack = []

    s = start
    visited[s] = 1
    path.append(s)

    while True:
        for e in adj[s]:
            if visited[e] == 0:
                stack.append(s)

                s = e
                visited[s] = 1
                path.append(s)
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break


