T = 1

for tc in range(1,T+1):
    N = 4


    arr = [[0] * 101 for _ in range(101)]
    cnt = 0

    for _ in range(4):
        left_x,left_y,right_x,right_y = map(int,input().split())

        for i in range(left_x,right_x):
            for j in range(left_y,right_y):
                if arr[i][j] == 0:
                    arr[i][j] = 1

    for i in range(101):
        for j in range(101):
            if arr[i][j] == 1:
                cnt += 1
    print(cnt)