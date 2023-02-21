import sys
sys.stdin = open('contact.txt', 'r')

T = 10

for tc in range(1,T+1):
    L, S = map(int,input().split())
    data = list(map(int,input().split()))
    adj = [[] for _ in range(101)]
    visited = [0] * 101
    q = []
    q.append(S)
    visited[S] = 1

    for i in range(0,L,2):
        s = data[i]
        e = data[i+1]
        adj[s].append(e)

    while q:
        t = q.pop(0)
        for i in adj[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

    max_ = 0
    ans = 0
    for i in range(101):
        if visited[i] >= max_:
            ans = i
            max_ = visited[i]

    print(f'#{tc} {ans}')



