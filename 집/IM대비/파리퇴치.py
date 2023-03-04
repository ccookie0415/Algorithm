import sys
sys.stdin = open('파리퇴치.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_ = 0

    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(M):
                for l in range(M):
                    ni = i + k
                    nj = j + l
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]

            if max_ < total:
                max_ = total

    print(f'#{tc} {max_}')