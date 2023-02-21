import sys
sys.stdin = open('부분집합의합.txt', 'r')

def f(i,k,key):
    global cnt
    global fcnt
    fcnt += 1
    if i == k:
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]
        if s == key:
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1, k, key)
        bit[i] = 0
        f(i+1, k, key)

T = int(input())

for tc in range(1,T+1):
    N, key = map(int,input().split())
    A = list(map(int,input().split()))
    bit = [0] * N
    cnt = 0
    fcnt = 0

    f(0,N,key)
    print(f'#{tc} {cnt} {fcnt}')

