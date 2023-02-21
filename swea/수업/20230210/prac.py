import sys
sys.stdin = open('input_정사각형.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 'yes'

    si, sj, ei, ej = N, N, 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                if si > i: si = i
                if sj > j: sj = j
                if ei < i: ei = i
                if ei < j: ej = j

    if (ei - si) != (ej - sj):
        ans = 'no'
    else:
        for i in range(si, ei+1):
            for j in range(sj, ej+1):
                if arr[i][j] != '#':
                    ans = 'no'
                    break
            if ans == 'no':
                break
    print(f'#{tc} {ans}')