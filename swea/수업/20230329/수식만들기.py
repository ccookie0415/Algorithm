import sys
sys.stdin = open('수식만들기.txt','r')


def find(n, total):
    global min_, max_

    if n == N - 1:
        if total <= min_:
            min_ = total
        if max_ <= total:
            max_ = total
        return

    for i in range(4):
        if operator[i] != 0:
            operator[i] -= 1
            if i == 0:
                n_total = total + number[n + 1]
            elif i == 1:
                n_total = total - number[n + 1]
            elif i == 2:
                n_total = total * number[n + 1]
            else:
                n_total = int(total / number[n + 1])
            find(n + 1, n_total)
            operator[i] += 1

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    min_ = 100000001
    max_ = -100000001
    operator = list(map(int,input().split()))       # +, -, *, /
    number = list(map(int,input().split()))

    find(0,number[0])
    print(f'#{tc} {max_-min_}')
