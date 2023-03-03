import sys
sys.stdin = open('스도쿠검증.txt','r')

T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    new_arr = list(zip(*arr))
    i_cnt = 0
    j_cnt = 0
    else_cnt = 0
    ans = 0

    for i in range(9):
        i_lst = []
        for j in range(9):
            if arr[i][j] not in i_lst:
                i_lst.append(arr[i][j])
            if len(i_lst) == 9:
                i_cnt += 1

    for i in range(9):
        j_lst = []
        for j in range(9):
            if new_arr[i][j] not in j_lst:
                j_lst.append(new_arr[i][j])
            if len(j_lst) == 9:
                j_cnt += 1


    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    for i in range(0,9,3):
        for j in range(0,9,3):
            lst = []
            lst.append(arr[i][j])
            x = i
            y = j
            a = 0
            for k in range(0,8):
                ni = x + di[a]
                nj = y + dj[a]
                x = ni
                y = nj
                if arr[ni][nj] not in lst:
                    lst.append(arr[ni][nj])
                if k % 2 == 1 or k == 6:
                    a = (a+1)%4
                if len(lst) == 9:
                    else_cnt += 1

    # print(i_cnt, j_cnt, else_cnt)
    if i_cnt == 9 and j_cnt == 9 and else_cnt == 9:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')


