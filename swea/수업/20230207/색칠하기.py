import sys
sys.stdin = open('input_색칠하기.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    ans = 0
    arr = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        R1, C1, R2, C2, color = map(int, input().split())
        for i in range(R1, R2 + 1):
            for j in range(C1, C2 + 1):
                arr[i][j] += color

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                ans += 1

    print(f'#{test_case} {ans}')