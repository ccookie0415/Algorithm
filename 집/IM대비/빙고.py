bingo = [list(map(int,input().split())) for _ in range(5)]
call = []
bingo_cnt = 0
i_check = 0
j_check = 0
cross_check = 0

for i in range(5):
    a,b,c,d,e = map(int,input().split())
    call.append(a)
    call.append(b)
    call.append(c)
    call.append(d)
    call.append(e)

for a in call:
    if i_check + j_check + cross_check >= 3:
        break
    i_check = 0
    j_check = 0
    cross_check = 0
    bingo_cnt += 1
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == a:
                bingo[i][j] = 0

    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[i][j] == 0:
                cnt += 1
        if cnt == 5:
            i_check += 1

    for j in range(5):
        cnt = 0
        for i in range(5):
            if bingo[i][j] == 0:
                cnt += 1
        if cnt == 5:
            j_check += 1

    di = [1,1]
    dj = [1,-1]

    if bingo[0][0] == 0:
        cnt = 0
        for k in range(1,5):
            ni = 0 + k * di[0]
            nj = 0 + k * dj[0]
            if bingo[ni][nj] == 0:
                cnt += 1
        if cnt == 4:
            cross_check += 1

    if bingo[0][4] == 0:
        cnt = 0
        for k in range(1,5):
            ni = 0 + k * di[1]
            nj = 4 + k * dj[1]
            if bingo[ni][nj] == 0:
                cnt += 1
        if cnt == 4:
            cross_check += 1

print(bingo_cnt)

