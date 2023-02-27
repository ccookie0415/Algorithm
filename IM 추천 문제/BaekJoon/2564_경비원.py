import sys
sys.stdin = open('testcase/2564_경비원.txt','r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

T = 1

for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = int(input())
    q = []
    ans = []
    arr = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]

    for i in range(1,M-1):
        for j in range(1,N-1):
            arr[i][j] = 1

    for i in range(A+1):
        direction,x = map(int,input().split())

        if i == A:
            if direction == 1:
                arr[0][x] = 2
                q.append((0,x))
            elif direction == 2:
                arr[M - 1][x] = 2
                q.append((M-1, x))
            elif direction == 3:
                arr[x][0] = 2
                q.append((x, 0))
            else:
                arr[x][N - 1] = 2
                q.append((x, N-1))
        else:
            if direction == 1:
                arr[0][x] = 3
            elif direction == 2:
                arr[M-1][x] = 3
            elif direction == 3:
                arr[x][0] = 3
            else:
                arr[x][N-1] = 3

        while q:
            i,j = q.pop(0)

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < M and 0 <= nj < N:
                    if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                        q.append((ni,nj))
                        visited[ni][nj] = visited[i][j] + 1

                    if arr[ni][nj] == 3:
                        if visited[ni][nj] == 0:
                            q.append((ni,nj))
                            visited[ni][nj] = visited[i][j] + 1
                        else:
                            if visited[i][j] + 1 < visited[ni][nj]:
                                visited[ni][nj] = visited[i][j] + 1
                                ans.append(visited[ni][nj])
                                break

    print(visited)


    print(ans)
