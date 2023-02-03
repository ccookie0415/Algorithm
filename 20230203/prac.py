import sys
sys.stdin = open('input_당근.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    c_lst = list(map(int,input().split()))
    cnt = [1] * len(c_lst)

    count = 1

    for i in range(1, len(c_lst)):
        if c_lst[i-1] < c_lst[i]:
            cnt[count] += 1

        else:
            count += 1

    print(cnt)