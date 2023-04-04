di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]

import sys
sys.stdin = open('미생물격리.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(K)]        # i,j,cnt,direction
    ans = 0


    for _ in range(M):
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]

            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                arr[i][2] = arr[i][2] // 2

                if arr[i][3] == 1:
                    arr[i][3] = 2
                elif arr[i][3] == 2:
                    arr[i][3] = 1
                elif arr[i][3] == 3:
                    arr[i][3] = 4
                elif arr[i][3] == 4:
                    arr[i][3] = 3

        arr.sort(reverse=True)

        a = 1
        while True:
            if a >= len(arr):
                break
            else:
                if arr[a-1][0] == arr[a][0] and arr[a-1][1] == arr[a][1]:
                    arr[a-1][2] += arr[a][2]
                    arr.pop(a)

                else:
                    a += 1

    for i in arr:
        ans += i[2]

    print(f'#{tc} {ans}')
