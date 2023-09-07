T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    max_ = 0
    min_ = 9999999999

    for i in range(0,N-M+1):
        sum_ = 0
        for j in range(M):
            sum_ += lst[i+j]

        if min_ > sum_:
            min_ = sum_

        if max_ < sum_:
            max_ = sum_

    print(f'#{tc} {max_ - min_}')