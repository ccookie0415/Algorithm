def find(s):
    key[0] = 0

    for _ in range(V):
        i_min = -1
        min_ = 1000000
        for i in range(V+1):
            if visited[i] == 0 and key[i] < min_:
                i_min = i
                min_ = key[i]

        visited[i_min] = 1

        for i in range(V+1):
            if adj[i_min][i] != 0 and visited[i] == 0:
                if adj[i_min][i] < key[i]:
                    key[i] = adj[i_min][i]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    ans = 0

    for _ in range(E):
        n1,n2,w = map(int,input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w


    key = [1000000] * (V+1)
    find(0)

    for i in key:
        ans += i

    print(f'#{tc} {ans}')
