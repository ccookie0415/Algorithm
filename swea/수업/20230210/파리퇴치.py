import sys
sys.stdin = open('input_파리퇴치.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N,M = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]
    max_ = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_ = 0
            for k in range(M):
                for l in range(M):
                    sum_ += lst[i+k][j+l]
                    if max_ < sum_:
                        max_ = sum_

    print(f'#{tc} {max_}')