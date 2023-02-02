T = 10
for i in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    total = 0

    for j in range(2, N - 2):
        tmp = data[j - 2:j + 2 + 1]
        # data의 index 2가 주로 판단
        max_tmp = max(tmp)
        # index 2[가운데]가 가장 큰 값이면 2개의 옆건물의 조망권을 확보한 경우
        if max_tmp == tmp[2]:
            # 가장 큰 값 삭제
            del (tmp[2])
            # 가장 큰 값(고층)에서 2번째로 큰 값을 빼면 조망권 확보 층 개수
            total += (max_tmp - max(tmp))
    print("#{} {}".format(i + 1, total))
