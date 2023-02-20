import sys
sys.stdin = open('피자굽기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N,M = list(map(int,input().split()))        # N : 화덕의 크기, # M : 피자 개수
    lst = list(map(int,input().split()))
    q = []
    for i in range(M):
        q.append([i+1,lst[i]])

    in_ = q[:N]
    out_ = q[N:]

    while len(in_) > 1:
        check = in_.pop(0)
        check[1] //= 2
        if check[1] == 0:
            if out_:
                in_.append(out_.pop(0))
        else:
            in_.append(check)

    ans = in_[0][0]
    print(f'#{tc} {ans}')