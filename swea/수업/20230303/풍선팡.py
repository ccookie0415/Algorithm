import sys
sys.stdin = open('풍선팡.txt','r')

di = [1,-1,0,0]
dj = [0,0,-1,1]

T = int(input())


for tc in range(1,T+1):
    N,M =map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_ = 0

    for i in range(N):
        for j in range(M):
            total = arr[i][j]
            for k in range(4):
                for l in range(1,arr[i][j]+1):
                    ni = i + l * di[k]
                    nj = j + l * dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        total += arr[ni][nj]
            if max_ < total:
                max_ = total

    print(f'#{tc} {max_}')
