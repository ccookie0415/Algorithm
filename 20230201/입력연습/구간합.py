# 첫 줄에 테스트 케이스 개수 T
# 정수의 개수 N과 구간의 개수 M

import sys
sys.stdin = open('input_구간합.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_value = 0
    min_value = 999999

    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += nums[i+j]

        if temp > max_value:
            max_value = temp
        if temp < min_value:
            min_value = temp

    answer = max_value - min_value

    print('#{} {}'.format(tc, answer))