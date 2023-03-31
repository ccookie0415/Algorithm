import sys
sys.stdin = open('베이비진2.txt', 'r')

T = int(input())

def check(player):


    for i in range(10):
        if player[i] == 3:
            return True

    for j in range(8):
        if player[j] and player[j+1] and player[j+2]:
            return True

    return False

for tc in range(1,T+1):
    cards = list(map(int,input().split()))
    player_1 = [0] * 10
    player_2 = [0] * 10
    ans = 0

    for i in range(len(cards)//2):
        player_1[cards[2*i]] += 1
        player_2[cards[2*i+1]] += 1
        if check(player_1) == True:
            ans = 1
            break
        if check(player_2) == True:
            ans = 2
            break

    print(f'#{tc} {ans}')