arr = [list(map(int,input().split())) for _ in range(5)]
check = []
i_check = 0
j_check = 0
cross_check = 0
cnt = 0
di = [1,1]
dj = [-1,1]

for _ in range(5):
    a,b,c,d,e = map(int,input().split())
    check.append(a)
    check.append(b)
    check.append(c)
    check.append(d)
    check.append(e)

for a in check:
    if (i_check + j_check + cross_check) == 3:
        print(cnt)
        break
    cnt += 1
    for i in range(5):
        for j in range(5):
            if arr[i][j] == a:
                arr[i][j] = 0

    for i in range(5):
        i_total = 0
        for j in range(5):
            i_total += arr[i][j]
        if i_total == 0:
            i_check += 1

    for j in range(5):
        j_total = 0
        for i in range(5):
            j_total += arr[i][j]
        if j_total == 0:
            j_check += 1

    # for j in range(5):
    #     if arr[0][j] == 0:
    #         cross_cnt = 1
    #         cross_cnt_2 = 1
    #         for k in range(1,5):
    #             ni = 0 + k * di[0]
    #             nj = j + k * dj[0]
    #             ni_2 = 0 + k * di[1]
    #             nj_2 = j + k * dj[1]
    #             if 0 <= ni < 5 and 0 <= nj < 5 and arr[ni][nj] == 0:
    #                 cross_cnt += 1
    #             if 0 <= ni_2 < 5 and 0 <= nj_2 < 5 and arr[ni_2][nj_2] == 0:
    #                 cross_cnt_2 += 1
    #         if cross_cnt == 5:
    #             cross_check += 1
    #         if cross_cnt_2 == 5:
    #             cross_check += 1


