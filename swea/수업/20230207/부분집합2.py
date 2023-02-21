import sys
sys.stdin = open('input_부분집합2.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N,K = map(int,input().split())
    lst = [n for n in range(1, 13)]  # 1~12 lst 생성
    ans = 0

    for bit in range(1 << 12):  # 12비트(개의 원소)로 만들수 있는 모든조합
        sm = 0
        cnt = 0
        for j in range(12):
            if bit & (1 << j):
                sm += lst[j]
                cnt += 1
        if sm == K and cnt == N:
            ans += 1

    print(f'#{tc} {ans}')