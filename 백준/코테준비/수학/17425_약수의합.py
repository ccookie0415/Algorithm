T = int(input())

for tc in range(1,T+1):
    N = int(input())
    total = 0

    for i in range(1,N+1):
        total += i * (N//i)

    print(total)