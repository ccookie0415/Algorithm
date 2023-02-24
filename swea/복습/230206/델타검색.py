import sys
sys.stdin = open('델타검색.txt','r')

di = [-1,0,1,0]
dj = [0,-1,0,1]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    total = 0

    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    tmp += abs(arr[i][j] - arr[ni][nj])
            total += tmp

    print(f'#{tc} {total}')