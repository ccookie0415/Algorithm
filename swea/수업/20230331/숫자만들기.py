import sys
sys.stdin = open('숫자만들기.txt','r')

def find(n,total):
    global max_
    global min_

    if n == N:
        if total > max_:
            max_ = total
        if total < min_:
            min_ = total

    for k in range(4):
        if operator[k] != 0:
            if k == 0:
                n_total = total + number[n]

            elif k == 1:
                n_total = total - number[n]

            elif k == 2:
                n_total = total * number[n]

            elif k == 3:
                n_total = int(total / number[n])

            operator[k] -= 1
            find(n+1, n_total)
            operator[k] += 1

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    operator = list(map(int,input().split()))
    number = list(map(int,input().split()))
    min_ = 100000001
    max_ = -100000001

    find(1,number[0])

    print(f'#{tc} {max_ - min_}')
