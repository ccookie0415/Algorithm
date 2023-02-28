import sys
sys.stdin = open('정사각형판정.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(str,input())) for _ in range(N)]
    si = N
    sj = N
    ei = 0
    ej = 0
    ans = ''

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                if si > i: si = i
                if sj > j: sj = j
                if ei < i: ei = i
                if ej < j: ej = j

    if (ei-si) != (ej-sj):
        ans = 'no'
    else:
        ans = 'yes'
        for i in range(si,ei+1):
            for j in range(sj,ej+1):
                if arr[i][j] == '.':
                    ans = 'no'

    print(f'#{tc} {ans}')

