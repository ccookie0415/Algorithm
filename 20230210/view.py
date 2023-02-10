import sys
sys.stdin = open('input_view.txt', 'r')


T = 3
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    M = 2  # 2가 아닌 일반화
    ans = 0
    for i in range(M, N - M):
        mx = lst[i - M]
        for j in range(i - M + 1, i + M + 1):
            if i == j:
                continue  # 기준값을 제외한 값 중 최대값
            else:
                if mx < lst[j]:
                    mx = lst[j]
        if lst[i] > mx:  # 기준값이 가장크면 조망권 있음
            ans += lst[i] - mx

    print(f'#{test_case} {ans}')



