import sys
sys.stdin = open('input_minmax.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

    answer = num[-1]-num[0]
    print(f'#{t + 1} {answer}')
