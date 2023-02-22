import sys
sys.stdin = open('subtree.txt' ,'r')

def node(n):
    if n != 0:
        path.append(n)
        node(c1[n])
        node(c2[n])


T = int(input())

for tc in range(1,T+1):
    E,N = map(int,input().split())
    lst = list(map(int, input().split()))
    c1 = [0] * (E+2)
    c2 = [0] * (E+2)
    path = []

    for i in range(E):
        p = lst[2*i]
        c = lst[2*i+1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    node(N)

    print(f'#{tc} {len(path)}')

