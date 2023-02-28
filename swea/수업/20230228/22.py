import sys
sys.stdin = open('영준이의카드카운팅.txt','r')

card_pattern = ['S','D','H','C']

T = int(input())

for tc in range(1,T+1):
    card = list(input())
    card_lst = []
    dic = {'S': 0, 'D': 0, 'H': 0, 'C': 0}
    ans = []
    tmp = ''

    for i in range(0,len(card),3):
        card_lst.append(card[i:i+3])

    for i in range(len(card_lst)):
        T = card_lst[i][0]      # S,D,H,C
        X = card_lst[i][1]
        Y = card_lst[i][2]
        card_num = int(X+Y)     # 카드 번호
        card_check = [0] * 14

        for k in range(4):
            if T == card_pattern[k]:
                if card_check[card_num] == 0:
                    card_check[card_num] = 1
                elif card_check[card_num] != 0:
                    print(card_num)

        for l in card_check:
            if l == 1:
                dic[T] += 1

    for value in dic.values():
        ans.append(13-value)

    print(f'#{tc}', *ans)
