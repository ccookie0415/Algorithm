T = int(input())

for tc in range(T):
    N = int(input())
    num = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    for i in range(len(num)):
        while True:
            if N % num[i] == 0:
                N = N // num[i]
                cnt[i] += 1

            else:
                break

    answer = ' '.join(map(str, cnt))

    print(f'#{tc + 1} {answer}')