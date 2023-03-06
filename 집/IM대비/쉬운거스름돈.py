import sys
sys.stdin = open('쉬운거스름돈.txt','r')

T = int(input())

for tc in range(1,T+1):
    money = int(input())
    ans = [0] * 8

    if money >= 50000:
        ans[0] = (money//50000)
        money = money % 50000

    if money >= 10000:
        ans[1] = (money//10000)
        money = money % 10000

    if money >= 5000:
        ans[2] = (money//5000)
        money = money % 5000

    if money >= 1000:
        ans[3] = (money//1000)
        money = money % 1000

    if money >= 500:
        ans[4] = (money//500)
        money = money % 500

    if money >= 100:
        ans[5] = (money//100)
        money = money % 100

    if money >= 50:
        ans[6] = (money//50)
        money = money % 50

    if money >= 10:
        ans[7] = (money//10)
        money = money % 10

    print(f'#{tc}')
    print(*ans)