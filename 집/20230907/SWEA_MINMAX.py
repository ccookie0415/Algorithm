T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    max_ = 0
    min_ = 9999999999

    for i in range(N):
        if lst[i] > max_:
            max_ = lst[i]

        if lst[i] < min_:
            min_ = lst[i]

    print(f'#{tc} {max_ - min_}')
