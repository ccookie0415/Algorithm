T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(str, input())) for _ in range(5)]
    ans = []

    for j in range(15):
        for i in range(5):
            try:
                ans.append(arr[i][j])
            except:
                continue

    print(ans)

    ans = ''.join(ans)
    print(f'#{tc} {ans}')