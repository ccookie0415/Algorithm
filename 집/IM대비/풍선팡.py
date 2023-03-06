T = int(input())

di = [0,1,0,-1]
dj = [1,0,-1,0]

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_ = 0

    for i in range(N):
        total = 0
        for j in range(M):
            total = arr[i][j]
            for k in range(4):
                for l in range(1,arr[i][j]+1):
                    ni = i + l * di[k]
                    nj = j + l * dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        total += arr[ni][nj]

            if total > max_:
                max_ = total

    print(f'#{tc} {max_}')