arr = [list(map(int,input().split())) for _ in range(5)]
check = []
cnt = 0
i_check = 0
j_check = 0
cross_check = 0
di = [1]
dj = [1]
di_2 = [1]
dj_2 = [-1]

for _ in range(5):
    a,b,c,d,e = map(int,input().split())
    check.append(a)
    check.append(b)
    check.append(c)
    check.append(d)
    check.append(e)

for k in check:
    if i_check + j_check + cross_check == 3:
        break
    for i in range(5):
        cnt_0 = 0
        cnt_1 = 0
        cnt_2 = 0
        cnt_3 = 0
        for j in range(5):
            if arr[i][j] == k:
                arr[i][j] = 0
            if arr[i][j] == 0 or arr[j][i] == 0:
                if arr[i][j] == 0:
                    cnt_0 += 1
                elif arr[j][i] == 0:
                    cnt_1 += 1
            if arr[0][j] == 0:
                for l in range(1,5):
                    ni = i + l*di[0]
                    nj = j + l*dj[0]
                    ni_2 = i + l*di_2[0]
                    nj_2 = j + l*dj_2[0]
                    if 0 <= ni < 5 and 0 <= nj < 5 and arr[ni][nj] == 0:
                        cnt_2 += 1
                    else:
                        break
                    if 0 <= ni_2 < 5 and 0 <= nj_2 < 5 and arr[ni_2][nj_2] == 0:
                        cnt_3 += 1
                    else:
                        break
        if cnt_0 == 5 or cnt_1 == 5:
            if cnt_0 == 5:
                i_check += 1
            if cnt_1 == 5:
                j_check += 1
        if cnt_2 == 4 or cnt_3 == 4:
            cross_check += 1
        print(cross_check)
    cnt += 1

print(cnt)