import sys
sys.stdin = open('algo1_sample_in.txt', 'r')

T =int(input())                         # 테스트케이스 input

di = [0,1]                              # 나아갈 방향 설정(행)
dj = [1,0]                              # 나아갈 방향 설정(열)

for tc in range(1, T+1):
    N, M = map(int,input().split())         # N : 도화지 크기, M : 도장 찍은 횟수
    arr = [[0] * N for _ in range(N)]       # N * N 크기의 배열 선언함


    for _ in range(M):                                          # 도장 찍은 횟수 M만큼, 케이스 입력받음
        col, row, width, height = map(int,input().split())

        for i in range(col,col+height):                 # col (행) 범위를 col+height 만큼 설정해줌 (행 + 높이만큼)
            for j in range(row,row+width):              # row (열) 범위를 row+width 만큼 설정해줌 (열 + 너비만큼)
                if 0 <= i < N and 0<= j < N:            # i, j의 범위가 배열을 벗어나지 않았는지 확인함
                    if arr[i][j] == 0:                  # 만약 도장을 찍었을 때, 그 범위에 있는 곳이 0이 되어있다면
                        arr[i][j] += 1                  # 1으로 만들어 주어서, 도장을 찍었다는 표시를 해줌.


        cnt = 0                                         # 배열의 1 개수를 카운트하기 위해 cnt라는 변수를 선언함
        for i in range(N):                              # N 크기 배열 i만큼 확인하고
            for j in range(N):                          # N 크기 배열 j만큼 확인하면 되니까
                if arr[i][j] == 1:                      # 만약 그 부분이 1이 되어있다면
                    cnt += 1                            # 카운트 += 1을 해줌

    print(f'#{tc} {cnt}')

