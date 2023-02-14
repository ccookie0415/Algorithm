import sys
sys.stdin = open('그래프경로.txt', 'r')

T = int(input())

def dfs_stk(start):
    visited = [0] * (V+1)
    stack = []
    s = S
    visited[s] = 1
    path.append(s)

    while True:
        for e in range(1, V+1):
            if visited[e] == 0 and adj[s][e] == 1:
                stack.append(s)
                s = e
                visited[s] = 1
                path.append(s)
                break
        else:   # 더 이상 연결된 방문노드 없는 경우
            if stack:
                s = stack.pop()
            else:
                break


for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        s, e = map(int,input().split())
        adj[s][e] = adj[s][e] = 1


    S, G = map(int,input().split())

    path = []
    dfs_stk(S)


    if S and G in path:
        ans = 1
    else:
        ans = 0
    print(f'#{tc}', ans)