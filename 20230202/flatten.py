import sys
sys.stdin = open('input_flatten.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    box_lst = list(map(int, input().split()))
    box_cnt = [0] * (N)

    for i in range(0, len(box_lst)):
        box_cnt[box_lst[i]] += 1
print(box_cnt)
