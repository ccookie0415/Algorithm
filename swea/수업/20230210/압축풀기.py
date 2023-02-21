import sys
sys.stdin = open('input_압축풀기.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    alphas = ""

    for _ in range(N):
        alpha, value = input().split()
        value = int(value)
        alphas += alpha*value


    print(f'#{tc}')
    for i in range(len(alphas)):
        if (i+1) % 10 == 0:
            print(alphas[i])
        else:
            print(alphas[i], end="")
    print()
