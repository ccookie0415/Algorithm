'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(v,N):
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(t,end = ' ')

        for i in adjL[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

    print()
    print(visited)


V,E = map(int,input().split())
data = list(map(int,input().split()))
adjL =[[] for _ in range(V+1)]

for i in range(E):
    n1,n2 = data[i*2], data[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)

bfs(1,V)    #시작정점 1, V 마지막 정점
