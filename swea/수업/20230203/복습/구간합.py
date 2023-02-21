import sys
sys.stdin = open('input_구간합.txt', 'r')

T = int(input())

for tc in range(T):
    N,M = map(int,input().split())
    nums = list(map(int,input().split()))

    min_value = 999999
    max_value = 0

    for i in range(N-M+1):
        tmp = 0
        for j in range(M):
            tmp += nums[i+j]

        if tmp > max_value:
            max_value = tmp

        if tmp < min_value:
            min_value = tmp

    answer = max_value - min_value

    print(f'#{tc+1} {answer}')



