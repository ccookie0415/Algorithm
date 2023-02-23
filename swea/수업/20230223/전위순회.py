import sys
sys.stdin = open('전위순회.txt','r')

def preorder(n):
    if n:
        ans.append(n)
        preorder(left[n])
        preorder(right[n])


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    left = [0] * (N+1)
    right = [0] * (N+1)
    ans = []
    root = 1

    for i in range(N-1):
        p = data[2*i]
        c = data[2*i+1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    preorder(root)
    print(f'#{tc}', *ans)