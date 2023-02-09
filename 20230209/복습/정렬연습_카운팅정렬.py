import sys
sys.stdin = open('input_정렬연습.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    num_lst = list(map(int,input().split()))
    max_ = max(num_lst)+1

    cnt = [0] * max_

    for i in num_lst:
        cnt[i] += 1

    i = 0
    for j in range(max_):
        for _ in range(cnt[j]):
            num_lst[i] = j
            i += 1

    print(num_lst)
