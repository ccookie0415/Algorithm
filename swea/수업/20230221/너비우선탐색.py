import sys
sys.stdin = open('너비우선탐색.txt','r')

T = int(input())

for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    q = []
    path = []
    start = 1

    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)

    visited[start] = 1
    q.append(start)

    while True:
        if not q:
            break
        else:
            t = q.pop(0)
            path.append(t)
            for i in adj[t]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[t] + 1

    print(f'#{tc}', *path)