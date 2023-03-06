T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[0] * N for _ in range(N)]

    for _ in range(M):
        x1,y1,x2,y2 = map(int,input().split())

        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                arr[i][j] = 1

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1

    print(f'#{tc} {cnt
    }')



