N = int(input())
A = N // 3 + 1
sum_ = 0
min_ = 9999999

for i in range(0,A+1):
    for j in range(0,A+1):
        sum_ = (3*i) + (5*j)
        if sum_ == N:
            if i + j < min_:
                min_ = i + j

if min_ == 9999999:
    ans = -1
else:
    ans = min_

print(ans)
