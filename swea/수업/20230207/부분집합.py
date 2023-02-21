import sys
sys.stdin = open('input_부분집합.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split(" ")))
    n = len(nums)
    ans = 0

    for i in range(1, 1<<n):
        sm = 0
        for j in range(n):
            if i & (1<<j):
                sm += nums[j]
        if sm == 0:
            ans = 1
            break

    print(f'#{tc} {ans}')