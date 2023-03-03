N = int(input())
cnt = 1
total = 1

while True:
    if total >= N:
        break
    total += 6 * cnt
    cnt += 1

print(cnt)
