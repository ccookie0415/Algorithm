import sys
sys.stdin = open('깊이우선탐색.txt', 'r')

def dfs_stk(start):
    visited = [0] * (V+1)
    stk = []
    s = start
    visited[s] = 1
    path.append(s)

    while True:
        # s에서 연결된, 미방문의 노드 발견시 이동 (다만, 낮은번호부터)
        for e in range(1,V+1):
            if visited[e] == 0 and adj[s][e]:
                stk.append(s)     # 주의 : 되돌아올 위치
                s = e
                visited[s] = 1
                path.append(s)
                #찾았으면 즉시, 그곳을 기준으로 탐색
                break
        else:   # 더 이상 연결된 방문노드 없는 경우
            if stk:
                s = stk.pop()
            else:
                break

T = int(input())
for tc in range(1, T+1):
    V,E = map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]


    # [1] 연결 행렬에 연결표시(1)
    for _ in range(E):
        s,e = map(int,input().split())
        adj[s][e] = adj[e][s] = 1

    path = []
    dfs_stk(1)

    print(f'#{tc}',*path)
