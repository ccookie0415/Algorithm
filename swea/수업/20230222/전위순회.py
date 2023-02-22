import sys
sys.stdin = open('전위순회.txt','r')

def preorder(n):
    if n:
        ans.append(n)
        preorder(c1[n])
        preorder(c2[n])

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)
    ans = []

    for i in range(0,N*2-2,2):
        p = arr[i]
        c = arr[i+1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    preorder(1)

    print(f'#{tc}', *ans)

