# [1] 최대값 찾기(i~끝)
# [2] i~ i_mx 차이 누적
# [3] i <- i_mx +1
# [4] 최대이익출력

import sys
sys.stdin = open('백만장자프로젝트.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())        # N 일
    price_lst = list(map(int,input().split()))
    max_price = 0
    i = 0
    total = 0

    while i < N:
        i_mx = i
        for j in range(i+1, N):
            if price_lst[i_mx] < price_lst[j]:
                i_mx = j

        for j in range(i, i_mx):
            total += price_lst[i_mx] - price_lst[j]

        i = i_mx + 1

    print(f'#{tc} {total}')