N,K = map(int,input().split())
data = list(map(int,input().split()))
max_ = 0

for i in range(N-K+1):
    sum_ = 0
    for j in range(i,i+K):
        sum_ += data[j]
    if sum_ > max_:
        max_ = sum_
print(max_)
