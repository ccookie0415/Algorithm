N = 10
cnt = [0] * N
total = 1

for i in range(N):
    num = int(input())
    cnt[i] = num % 42

cnt.sort()

for i in range(N-1):
    if cnt[i] == cnt[i+1]:
        continue
    else:
        total += 1

print(total)
