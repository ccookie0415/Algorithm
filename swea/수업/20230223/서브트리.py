import sys
sys.stdin = open('서브트리.txt','r')

def find_node(n):
    if n:
        ans.append(n)
        find_node(left[n])
        find_node(right[n])

T = int(input())

for tc in range(1,T+1):
    E,N = map(int,input().split())
    data = list(map(int,input().split()))
    ans = []
    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        p = data[2*i]
        c = data[2*i+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    find_node(N)
    print(f'#{tc} {len(ans)}')