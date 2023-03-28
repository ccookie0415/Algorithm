T = int(input())

for tc in range(T):
    data = list(map(int, input()))
    card_cnt = [0] * (12)
    for t in range(0, len(data)):
        card_cnt[data[t]] += 1

    i = tri_cnt = run_cnt = 0

    while i < 10:
        if card_cnt[i] >= 3:
            tri_cnt += 1
            card_cnt[i] -= 3
            continue

        if card_cnt[i] >= 1 and card_cnt[i + 1] >= 1 and card_cnt[i + 2] >= 1:
            run_cnt += 1
            card_cnt[i] -= 1
            card_cnt[i + 1] -= 1
            card_cnt[i + 2] -= 1
            continue
        i += 1
    if tri_cnt + run_cnt == 2:
        print(f'#{tc + 1} 1')
    else:
        print(f'#{tc + 1} 0')