import sys
sys.stdin = open('중위순회.txt','r')

def inord(n):
    if 1 <= n <= N:
        inord(n*2)
        alst.append(lst[n])
        inord(n*2+1)
    return

T = 10

for tc in range(1,T+1):
    N = int(input())
    lst = [0] * (N+1)

    for i in range(1,N+1):
        tlst = input().split()
        lst[i] = tlst[1]

    print(lst)
    alst = []
    inord(1)

    print(f'#{tc} {"".join(alst)}')