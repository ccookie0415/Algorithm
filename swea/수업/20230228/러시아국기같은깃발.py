import sys
sys.stdin = open('러시아국기같은깃발.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(N)]
    lst = []
    ans = 9999999999999

    for i in range(1,N-1):
        cnt_W = 0
        cnt_B = 0
        cnt_R = 0
        for j in range(M):
            if arr[i][j] == 'W':
                cnt_W += 1
            if arr[i][j] == 'B':
                cnt_B += 1
            if arr[i][j] == 'R':
                cnt_R += 1
        lst.append([cnt_W,cnt_B,cnt_R])

    for white_line in range(0,N-3+1):
        for blue_line in range(1,N-2-white_line+1):
            cnt = 0
            red_line = N-white_line-blue_line-2

            for i in range(white_line):
                cnt += lst[i][1]
                cnt += lst[i][2]

            for j in range(white_line, white_line + blue_line):
                cnt += lst[j][0]
                cnt += lst[j][2]

            for k in range(white_line+blue_line, white_line+blue_line+red_line):
                cnt += lst[k][0]
                cnt += lst[k][1]

            if ans > cnt:
                ans = cnt

    for j in range(M):
        if arr[0][j] != 'W':
            ans += 1
        if arr[N-1][j] != 'R':
            ans += 1

    print(f'#{tc} {ans}')
