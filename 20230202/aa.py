import sys
sys.stdin = open('input_bus.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    charge_station = list(map(int, input().split()))
    count = current = 0

    while current + K < N:
        for step in range(K, 0, -1):
            if (current + step) in charge_station:
                current += step
                count += 1
                break
        else:
            count = 0
            break

    # 결과 출력
    print('#{} {}'.format(tc, count))
