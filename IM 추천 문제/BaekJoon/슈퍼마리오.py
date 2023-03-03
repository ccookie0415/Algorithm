mushroom = []
total = 0

for _ in range(10):
    a = int(input())
    mushroom.append(a)

for i in mushroom:
    tmp = total
    total += i
    if total >= 100:
        if 100 - tmp >= total - 100:
            total = total
        else:
            total = tmp
        break

print(total)