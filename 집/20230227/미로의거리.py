import sys
sys.stdin = open('미로.txt','r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [[1] * (N+2)] +  [[1] + list(map(int,input())) + [1] for _ in range(N)] + [[1] * (N+2)]
    visited = [[0] * (N+2) for _ in range(N+2)]
    q = []
    start_i = 0
    start_j = 0
    ans = 0

    for i in range(N+2):
        for j in range(N+2):
            if arr[i][j] == 2:
                visited[i][j] = 1
                start_i = i
                start_j = j

    q.append((start_i,start_j))

    while q:
        i,j = q.pop(0)
        if arr[i][j] == 3:
            ans = visited[i][j] - 2
            break

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if arr[ni][nj] == 0 or arr[ni][nj] == 3:
                if visited[ni][nj] == 0:
                    q.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1

    print(f'#{tc} {ans}')





