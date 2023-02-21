import sys
sys.stdin = open('input_min_max.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    num_lst = list(map(int,input().split()))

    # for i in range(N-1, 0, -1):
    #     for j in range(0,i):
    #         if num_lst[j] > num_lst[j+1]:
    #             num_lst[j],num_lst[j+1] = num_lst[j+1],num_lst[j]
    #
    # ans = num_lst[-1] - num_lst[0]
    #
    # print(f'#{tc} {ans}')

    max_ = num_lst[0]
    min_ = num_lst[0]

    for i in range(N):
        if num_lst[i] > max_:
            max_ = num_lst[i]
        elif num_lst[i] < min_:
            min_ = num_lst[i]

    ans = max_ - min_
    print(f'#{tc} {ans}')


