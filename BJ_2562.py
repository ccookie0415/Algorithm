cnt = 0
max_ = 0

for i in range(1,10):
    N = int(input())

    if N > max_:
        max_ = N
        cnt = i

print(max_)
print(cnt)