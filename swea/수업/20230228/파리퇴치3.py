import sys
sys.stdin = open('파리퇴치3.txt','r')

di = [1,0,-1,0]
dj = [0,1,0,-1]

di_2 = [-1,-1,1,1]
dj_2 = [-1,1,-1,1]

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_ = 0

    for i in range(N):
        for j in range(N):
            a = 1
            total = arr[i][j]
            total_2 = arr[i][j]
            while True:
                if a == M:
                    break
                for k in range(4):
                    ni = i + a * di[k]
                    nj = j + a * dj[k]
                    ni_2 = i + a * di_2[k]
                    nj_2 = j + a * dj_2[k]

                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]

                    if 0 <= ni_2 < N and 0 <= nj_2 < N:
                        total_2 += arr[ni_2][nj_2]

                a += 1
            if total > max_:
                max_ = total
            if total_2 > max_:
                max_ = total_2

    print(f'#{tc} {max_}')