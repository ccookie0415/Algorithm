import sys
sys.stdin = open('input_회문.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N,M = map(int,input().split())
    str_lst = []

    for _ in range(N):
        str_lst.append(list(input()))
    # print(str_lst)

    for i in range(N):
        for j in range(N-M+1):
            row = str_lst[i][j:j+M]
            col = [str_lst[x][i] for x in range(j,(j+M))]
            if row == row[::-1]:
                ans = (''.join(row))
            elif col == col[::-1]:
                ans = (''.join(col))

    print(f'#{tc} {ans}')
