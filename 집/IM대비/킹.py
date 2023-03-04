king,stone,N = map(str,input().split())
N = int(N)
king = list(king)
stone = list(stone)
dic = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
n = list(dic.keys())
ans = []

king[0] = dic[king[0]]
stone[0] = dic[stone[0]]

j = king[0]
i = 8 - int(king[1])
nj = stone[0]
ni = 8 - int(stone[1])

for _ in range(N):
    k = input()
    if k == 'R':
        i = i
        j = j + 1
        if 0 <= i < 8 and 0 <= j < 8:
            if i == ni and j == nj:
                ni = ni
                nj = nj + 1
                if 0 <= ni < 8 and 0 <= nj < 8:
                    pass
                else:
                    i = i
                    j = j - 1
                    ni = ni
                    nj = nj - 1
            else:
                pass
        else:
            i = i
            j = j - 1
    if k == 'L':
        i = i
        j = j - 1
        if 0 <= i < 8 and 0 <= j < 8:
            if i == ni and j == nj:
                ni = ni
                nj = nj - 1
                if 0 <= ni < 8 and 0 <= nj < 8:
                    pass
                else:
                    i = i
                    j = j + 1
                    ni = ni
                    nj = nj + 1
            else:
                pass
        else:
            i = i
            j = j + 1

    if k == 'B':
        i = i + 1
        j = j
        if 0 <= i < 8 and 0 <= j < 8:
            if i == ni and j == nj:
                ni = ni + 1
                nj = nj
                if 0 <= ni < 8 and 0 <= nj < 8:
                    pass
                else:
                    i = i - 1
                    j = j
                    ni = ni - 1
                    nj = nj
            else:
                pass
        else:
            i = i - 1
            j = j

    if k == 'T':
        i = i - 1
        j = j
        if 0 <= i < 8 and 0 <= j < 8:
            if i == ni and j == nj:
                ni = ni - 1
                nj = nj
                if 0 <= ni < 8 and 0 <= nj < 8:
                    pass
                else:
                    i = i + 1
                    j = j
                    ni = ni + 1
                    nj = nj
            else:
                pass
        else:
            i = i + 1
            j = j

    if k == 'RT':
        i = i - 1
        j = j + 1
        if 0 <= i < 8 and 0 <= j < 8:
            if i == ni and j == nj:
                ni = ni - 1
                nj = nj + 1
                if 0 <= ni < 8 and 0 <= nj < 8:
                    pass
                else:
                    i = i + 1
                    j = j - 1
                    ni = ni + 1
                    nj = nj - 1
            else:
                pass
        else:
            i = i + 1
            j = j - 1

    if k == 'LT':
        i = i - 1
        j = j - 1
        if 0 <= i < 8 and 0 <= j < 8:
            if i == ni and j == nj:
                ni = ni - 1
                nj = nj - 1
                if 0 <= ni < 8 and 0 <= nj < 8:
                    pass
                else:
                    i = i + 1
                    j = j + 1
                    ni = ni + 1
                    nj = nj + 1
            else:
                pass
        else:
            i = i + 1
            j = j + 1

    if k == 'RB':
        i = i + 1
        j = j + 1
        if 0 <= i < 8 and 0 <= j < 8:
            if i == ni and j == nj:
                ni = ni + 1
                nj = nj + 1
                if 0 <= ni < 8 and 0 <= nj < 8:
                    pass
                else:
                    i = i - 1
                    j = j - 1
                    ni = ni - 1
                    nj = nj - 1
            else:
                pass
        else:
            i = i - 1
            j = j - 1

    if k == 'LB':
        i = i + 1
        j = j - 1
        if 0 <= i < 8 and 0 <= j < 8:
            if i == ni and j == nj:
                ni = ni + 1
                nj = nj - 1
                if 0 <= ni < 8 and 0 <= nj < 8:
                    pass
                else:
                    i = i - 1
                    j = j + 1
                    ni = ni - 1
                    nj = nj + 1
            else:
                pass
        else:
            i = i - 1
            j = j + 1

i,j = j,i
ni,nj = nj,ni
j = 8 - j
nj = 8 - nj
i = n[i]
ni = n[ni]
ans.append(str(i)+str(j))
ans.append(str(ni)+str(nj))

for i in ans:
    print(i)