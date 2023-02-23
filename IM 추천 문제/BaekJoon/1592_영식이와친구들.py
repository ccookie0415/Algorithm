import sys
sys.stdin = open('영식이와친구들.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    current = 0
    cnt = [0] * N

    while cnt[current] != M:
        if cnt[current] % 2 == 0:
            current = (current - L) % N
            cnt[current] = cnt[current] + 1
        else:
            current = (current + L) % N
            cnt[current] = cnt[current] + 1

    total = 0
    for i in range(N):
        total += cnt[i]

    print(total-1)
