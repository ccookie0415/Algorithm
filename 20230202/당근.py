import sys
sys.stdin = open('input_당근.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    c_lst = list(map(int,input().split()))
    print(c_lst)

    cnt = 1

    for i in range(1,N):
        if c_lst[i-1] < c_lst[i]:
            cnt += 1

        if c_lst[i] < c_lst[i-1]:
            cnt = 1

    print(f'#{tc+1} {cnt}')
