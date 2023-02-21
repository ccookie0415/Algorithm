import sys
sys.stdin = open('input_card.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    card_lst = list(map(int,input()))
    card_cnt = [0] * 10

    for i in range(0, len(card_lst)):
        card_cnt[card_lst[i]] += 1

    max_card_idx = 0
    max_card_num = 0

    for j in range(len(card_cnt)):
        if card_cnt[j] >= max_card_num:
            max_card_num = card_cnt[j]
            max_card_idx = j

    print(f'#{tc+1} {max_card_idx} {max_card_num}')