def solve(n):
    global maxValue
    value = int(''.join(cards))
    if (n, value) in checked:
        return
    checked.add((n, value))
    if n == N:
        if value > maxValue:
            maxValue = value
        return
    for i in range(len(cards) - 1):
        for j in range(i + 1, len(cards)):
            cards[i], cards[j] = cards[j], cards[i]
            solve(n + 1)
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for tc in range(T):
    cards, N = input().split()
    cards = list(cards)
    N = int(N)
    maxValue = 0
    checked = set()
    solve(0)
    print(f'#{tc + 1} {maxValue}')