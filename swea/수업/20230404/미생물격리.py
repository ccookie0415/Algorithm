import sys
sys.stdin = open('미생물격리.txt','r')

di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]

def find(arr,CNT):
    global ans

    if CNT == M+1:
        for i in range(N):
            for j in range(N):
                if arr[i][j] != 0:
                    ans += arr[i][j][0]

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:                                  # 0 , 1                           # c, di
                ni = i + di[arr[i][j][1]]
                nj = j + dj[arr[i][j][1]]
                # if 1 <= ni <= N-2 and 1 <= nj <= N-2:
                #     arr[i][j] = 0
                #     arr[ni][nj] = (arr[ni][nj][0] + arr[i][j][0], arr[i][j][1])
#
            #     else:
            #         arr[i][j] = 0
            #
            #         if arr[i][j][1] == 1:
            #             new_di = 2
            #
            #         elif arr[i][j][1] == 2:
            #             new_di = 1
            #
            #         elif arr[i][j][1] == 3:
            #             new_di = 4
            #
            #         elif arr[i][j][1] == 4:
            #             new_di = 3
            #
            #         arr[ni][nj] = (arr[ni][nj][0] + arr[i][j][0]//2, new_di)
            #
            # elif arr[i][j][0] == 0:
            #     arr[i][j] = 0

    find(arr, CNT+1)

T = int(input())

for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [[[0] * N for _ in range(N)]]





