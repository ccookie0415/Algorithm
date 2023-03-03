import sys
sys.stdin = open('contact.txt','r')

T = 10

for tc in range(1,T+1):
    N,S = map(int,input().split())
    data = list(map(int,input().split()))
    adj = [[] for _ in range(101)]
    visited = [0] * 101
    q = []
    q.append(S)
    visited[S] = 1
    max_ = 0
    max_idx = 0

    for i in range(0,N,2):
        s = data[i]
        e = data[i+1]
        adj[s].append(e)


    while q:
        t = q.pop(0)
        for i in adj[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

    for i in range(len(visited)):
        if visited[i] >= max_:
            max_ = visited[i]
            max_idx = i

    print(f'#{tc} {max_idx}')





