import sys
sys.stdin = open('input_flatten.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    box_lst = list(map(int, input().split()))

    while N:
        max_box = max(box_lst)
        min_box = min(box_lst)
        max_idx = box_lst.index(max(box_lst))
        min_idx = box_lst.index(min(box_lst))
        box_lst[max_idx] -= 1
        box_lst[min_idx] += 1

        N -= 1
        answer = max(box_lst) - min(box_lst)

    print(f'#{tc+1} {answer}')