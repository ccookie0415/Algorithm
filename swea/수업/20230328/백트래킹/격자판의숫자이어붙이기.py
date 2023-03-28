import sys
sys.stdin = open('격자판의숫자이어붙이기.txt', 'r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

def find(i,j,cnt,number):
    global result

    if cnt == 7:
        if number in result:
            return
        else:
            result.append(number)

    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 4 and 0 <= nj < 4:
                find(ni, nj, cnt + 1, number + arr[ni][nj])


T = int(input())

for tc in range(1,T+1):
    arr = [list(map(str,input().split())) for _ in range(4)]
    result = []

    for i in range(4):
        for j in range(4):
            find(i, j, 1, arr[i][j])

    print(f'#{tc} {len(result)}')