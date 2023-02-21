import sys
sys.stdin = open('input_회문1.txt', 'r')

T= 10

for tc in range(1, T + 1):
    M = int(input())
    str_lst = []
    cnt = 0
    N = 8

    for _ in range(N):
        str_lst.append(list(input()))

    for i in range(N):
        for j in range(N - M + 1):
            row = str_lst[i][j:j + M]
            col = [str_lst[x][i] for x in range(j, (j + M))]
            if row == row[::-1]:
                cnt += 1
            if col == col[::-1]:
                cnt += 1
    #
    print(f'#{tc} {cnt}')
