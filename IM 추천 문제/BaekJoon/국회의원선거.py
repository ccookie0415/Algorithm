N = int(input())
lst = []

for i in range(N):
    a = int(input())
    lst.append(a)


cnt = 0

while True:
    max_ = 0
    max_idx = 0
    min_ = 101
    min_idx = 0
    for i in range(N):
        if lst[i] >= max_:
            max_ = lst[i]
            max_idx = i
    lst[0] += 1
    lst[max_idx] -= 1
    if max_idx == 0:
        break
    cnt += 1
print(cnt)
