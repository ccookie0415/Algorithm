import sys
sys.stdin = open('sum.txt', 'r')

T = 10

for tc in range(1,T+1):
    tc_num = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    max_ = 0

    for i in range(100):
        sum_ = 0
        for j in range(100):
            sum_ += arr[i][j]
        if sum_ > max_:
            max_ = sum_

    for j in range(100):
        sum_ = 0
        for i in range(100):
            sum_ += arr[i][j]
        if sum_ > max_:
            max_ = sum_

    print(f'#{tc} {max_}')