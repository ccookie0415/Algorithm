R,C,M = map(int,input().split())
lst = []
catch = []

di = [0,-1,1,0,0]
dj = [0,0,0,1,-1]
dct = {1:2, 2:1, 3:4, 4:3}

for _ in range(M):
    r,c,s,d,z = map(int,input().split())            # r,c : 상어 위치, s : 속력, d: 이동방향 z: 크기
    lst.append([r,c,s,d,z])


print(lst)

for k in range(1,C+1):
    for l in range(len(lst)):
        ni = lst[l][0] + lst[l][2] * di[lst[l][3]]
        nj = lst[l][1] + lst[l][2] * dj[lst[l][3]]
        if 1 <= ni <= R and 1 <= nj <= C:
            lst[l][0] = ni
            lst[l][1] = nj
        else:
            if ni > R:
                lst[l][0] = ni - R
                lst[l][3] = dct[lst[l][3]]
            elif nj > C:
                lst[l][1] = nj - C
                lst[l][3] = dct[lst[l][3]]
            elif ni <= 0:
                lst[l][0] =
print(lst)


# for j in range(1,C+1):
#     for i in range(1,R+1):
#