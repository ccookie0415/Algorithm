import sys
sys.stdin = open('오목판정.txt', 'r')

T = int(input())

di = [1,1]
dj = [1,-1]


for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    arr_2 = list(zip(*arr))
    ans = 'NO'

    # 가로

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
            else:
                cnt = 0
        if cnt == 5:
            ans = 'YES'
            break
    #세로

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr_2[i][j] == 'o':
                cnt += 1
            else:
                cnt = 0
        if cnt == 5:
            ans = 'YES'
            break

    # 대각선
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(2):
                    ni = i
                    nj = j
                    cnt = 0
                    while 0<= ni < N and 0<= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += di[k]
                        nj += dj[k]
                    if cnt == 5:
                        ans = 'YES'
                        break

    print(f'#{tc} {ans}')


