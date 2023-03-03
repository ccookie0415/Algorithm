T = int(input())

for tc in range(1,T+1):
    data = list(input())
    total = 0
    cnt = 0

    for i in range(len(data)):
        if data[i] == 'O':
            cnt += 1
            total += cnt
        elif data[i] == 'X':
            cnt = 0

    print(total)
