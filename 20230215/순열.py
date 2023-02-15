# {1,2,3}을 포함하는 모든 순열을 생성하는 함수
for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)


# 백트래킹을 이용하여 순열 구하기

def construct_candidates(a,k,input,c):
    in_perm = [False] * NMAX

    for i in range(1,k):
        in_perm[a[i]] = True

    ncandidates = 0

    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

