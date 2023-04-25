def find(n,total):
    global max_
    global min_

    if n == N:
        if total > max_:
            max_ = total
        if total < min_:
            min_ = total

    for k in range(4):
        if operator[k] != 0:
            if k == 0:
                n_total = total + number[n]

            elif k == 1:
                n_total = total - number[n]

            elif k == 2:
                n_total = total * number[n]

            elif k == 3:
                n_total = int(total / number[n])

            operator[k] -= 1
            find(n+1, n_total)
            operator[k] += 1


N = int(input())
number = list(map(int,input().split()))
operator = list(map(int,input().split()))
min_ = 1000000001
max_ = -1000000001

find(1,number[0])

print(max_)
print(min_)
