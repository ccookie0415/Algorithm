import sys
sys.stdin = open('베이비진게임.txt', 'r')

def find_winner(player_card):

    for i in range(len(player_card)):
        if player_card[i] == 3:
            return True

    for i in range(len(player_card)-3):
        if player_card[i] != 0 and player_card[i+1] != 0 and player_card[i+2] != 0:
            return True

    return False

T = int(input())

for tc in range(1,T+1):
    card_lst = list(map(int,input().split()))
    player_1_card = [0] * 10
    player_2_card = [0] * 10
    ans = 0

    for i in range(0,len(card_lst),2):
        player_1_card[card_lst[i]] += 1
        player_2_card[card_lst[i+1]] += 1

        if find_winner(player_1_card) == True and find_winner(player_2_card) == True:
            ans = 0
            break
        elif find_winner(player_1_card) == True and find_winner(player_2_card) == False:
            ans = 1
            break
        elif find_winner(player_1_card) == False and find_winner(player_2_card) == True:
            ans = 2
            break

    print(f'#{tc} {ans}')


    # for i in range(len(card_lst)):
    #     if i % 2 == 0:
    #         player_1_card[card_lst[i]] += 1
    #         if find_winner(player_1_card) == True:
    #             ans = 1
    #             break
    #
    #     else:
    #         player_2_card[card_lst[i]] += 1
    #         if find_winner(player_2_card) == True:
    #             ans = 2
    #             break