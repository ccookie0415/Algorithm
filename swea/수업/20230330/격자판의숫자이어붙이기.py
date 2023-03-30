di = [1,0,-1,0]
dj = [0,-1,0,1]

def find(i,j,n,num):
    global ans
    global check

    if n == 7:
        if num not in check:
            check.append(num)
            ans += 1

    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 4 and 0 <= nj < 4:
                find(ni,nj,n+1,num + arr[i][j])

T = int(input())

for tc in range(1,T+1):
    arr = [list(map(str,input().split())) for _ in range(4)]
    check = []
    ans = 0

    for i in range(4):
        for j in range(4):
            find(i, j, 0, arr[i][j])

    print(f'#{tc} {ans}')


