import sys
sys.stdin = open('종이붙이기.txt', 'r')

T = int(input())

def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n-1) + 2 * paper(n-2)

for tc in range(1,T+1):
    N = int(input())
    n = N//10

    print(f'#{tc} {paper(n)}')
