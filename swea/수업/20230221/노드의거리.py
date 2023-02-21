import sys
sys.stdin = open('노드의거리3.txt','r')

T = int(input())

for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    q = []
    ans = 0

    for _ in range(E):
        s,e = map(int,input().split())
        adj[s].append(e)
        adj[e].append(s)
    S,G = map(int,input().split())

    q.append(S)
    visited[S] = 1

    while True:
        if not q:
            break
        else:
            t = q.pop(0)
            for i in adj[t]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[t] + 1
                    if i == G:
                        ans = visited[G] - 1
                        break


    print(f'#{tc} {ans}')
