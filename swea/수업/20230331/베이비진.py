import sys
sys.stdin = open('베이비진.txt','r')


T = int(input())

def check(player, run_, tri_):
    global ans

    if run_ + tri_ == 2:
        ans = 1

    for j in range(10):
        if player[j] == 3:
            player[j] -= 3
            check(player, run_, tri_ + 1)
            player[j] += 3

    for k in range(8):
        if player[k] and player[k + 1] and player[k + 2]:
            player[k] -= 1
            player[k+1] -= 1
            player[k+2] -= 1
            check(player, run_ + 1, tri_)
            player[k] += 1
            player[k+1] += 1
            player[k+2] += 1

for tc in range(1, T + 1):
    cards = list(map(int, input()))
    lst = [0] * 10
    ans = 0


    for i in cards:
        lst[i] += 1

    check(lst,0,0)
    print(f'#{tc} {ans}')