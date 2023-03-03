import sys
sys.stdin = open('subtree.txt','r')

def subtree(n):
    global cnt
    if n:
        cnt += 1
        subtree(left[n])
        subtree(right[n])



T = int(input())

for tc in range(1,T+1):
    E,N = map(int,input().split())
    lst = list(map(int,input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    cnt = 0

    for i in range(E):
        p,c = lst[i*2], lst[i*2+1]

        if left[p] == 0:
            left[p] = c

        else:
            right[p] = c

    subtree(N)
    print(f'#{tc} {cnt}')