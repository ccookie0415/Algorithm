import sys
sys.stdin = open('input_bus.txt', 'r')

T = int(input())

for tc in range(T):
    K,N,M = list(map(int,input().split()))
    charge = list(map(int,input().split()))
    current = cnt = 0

    while current + K < N:
        for step in range(K, 0, -1):
            if (current + step) in charge:
                current += step
                cnt += 1
                break

        else:
             cnt = 0
             break

    print(f'#{tc+1} {cnt}')


