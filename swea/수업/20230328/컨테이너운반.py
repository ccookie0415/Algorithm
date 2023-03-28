import sys
sys.stdin = open('컨테이너운반.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    w_lst = list(map(int,input().split()))
    t_lst = list(map(int,input().split()))
    A = len(w_lst)
    B = len(t_lst)
    a = 0
    b = 0
    ans = 0

    w_lst.sort(reverse=True)
    t_lst.sort(reverse=True)

    while True:
        if b==B or a==A:
            break
        else:
            if w_lst[a] <= t_lst[b]:
                ans += w_lst[a]
                a += 1
                b += 1
            else:
                a += 1

    print(f'#{tc} {ans}')




