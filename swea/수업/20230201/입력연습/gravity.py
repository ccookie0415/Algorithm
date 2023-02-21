import sys
sys.stdin = open('input_gravity.txt', 'r')

T = int(input())

for tc in range(0, T):
    N = int(input())
    M = list(map(int, input().split()))
    max_value = 0

    for i in range(N):
        cnt = 0
        for j in range(i + 1, N):
            if M[i] > M[j]:
                cnt += 1

        if cnt > max_value:
            max_value = cnt

    print(f'#{tc+1} {max_value}')