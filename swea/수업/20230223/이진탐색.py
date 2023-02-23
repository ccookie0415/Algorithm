import sys
sys.stdin = open('이진탐색.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)
    root = 1

    for i in range(1,N+1):
        if i == root:
            continue
        else:
            if left[i//2] == 0:
                left[i//2] = i
            else:
                right[i//2] = i
        par[i] = i//2
    print(left)
    print(right)
    print(par)
    while par[root] != 0:
        root += 1

    print(root)