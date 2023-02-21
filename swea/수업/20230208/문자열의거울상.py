import sys
sys.stdin = open('input_문자열의거울상.txt', 'r')

# b, d, p, q 거울상

# p, q, b, d

T = int(input())

for tc in range(1,T+1):
    str_ = list(input())
    N = len(str_)
    str_ = str_[::-1]

    for i in range(N):
        if str_[i] == 'q':
            str_[i] = 'p'
        elif str_[i] == 'p':
            str_[i] = 'q'
        elif str_[i] == 'd':
            str_[i] = 'b'
        elif str_[i] == 'b':
            str_[i] = 'd'
        ans = ''.join(str_)
    print(f'#{tc} {ans}')
