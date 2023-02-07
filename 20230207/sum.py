import sys
sys.stdin = open('input_sum.txt', 'r')


for _ in range(10):
    T = int(input())
    arr = []

    for i in range(100):
        arr.append(list(map(int, input().split())))

    max_1 = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if sum > max_1:
            max_1 = sum

    max_2 = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        if sum > max_2:
            max_2 = sum

    max_3 = 0
    for i in range(100):
        sum1 = 0
        sum2 = 0
        sum1 += arr[i][i]
        sum2 += arr[i][99 - i]
    if max(sum1, sum2) > max_3:
        max_3 = max(sum1, sum2)

    print("#{} {}".format(T, max(max_1, max_2, max_3)))