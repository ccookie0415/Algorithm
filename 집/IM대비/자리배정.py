M,N = map(int,input().split())
arr = [[0] * M for _ in range(N)]
A = M*N
find = int(input())
ans = [0]

if A < find:
    print(0)

else:

    di = [1,0,-1,0]
    dj = [0,1,0,-1]

    x = 0
    y = 0
    a = 0

    for k in range(1,A+1):
        arr[x][y] = k
        ni = x + di[a%4]
        nj = y + dj[a%4]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            x = ni
            y = nj
        else:
            a += 1
            x = x + di[a%4]
            y = y + dj[a%4]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == find:
                ans.append(j+1)
                ans.append(i+1)
                print(j + 1, i + 1)
                break



