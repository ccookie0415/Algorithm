import sys
sys.stdin = open('피자굽기.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    pizza = list(map(int,input().split()))
    cheese = []

    for i in range(1,M+1):
        cheese.append((i,pizza[i-1]))

    in_ = cheese[:N]
    out_ = cheese[N:]

    while len(in_) != 1:
        idx,C = in_.pop(0)
        C = C//2
        if C != 0:
            in_.append((idx,C))
        else:
            if len(out_) != 0:
                in_.append(out_.pop(0))

    ans = in_[0][0]
    print(f'#{tc} {ans}')

