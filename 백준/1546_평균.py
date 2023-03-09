N = int(input())
data = list(map(int,input().split()))
ans_data = [0]*N
sum_ = 0
M = 0

for i in data:
    if i > M:
        M = i

for i in range(N):
    data[i] = data[i]/M*100
    sum_ += data[i]

print(sum_/N)


