import sys

sys.stdin = open('input_flatten.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    box_lst = list(map(int, input().split()))

    sorted_level = sorted(box_lst)

    for j in range(N):
        sorted_level[-1] -= 1
        sorted_level[0] += 1
        sorted_level = sorted(sorted_level)

    flatten_level = sorted_level[-1] - sorted_level[0]

    print(f'#{tc + 1} {flatten_level}')