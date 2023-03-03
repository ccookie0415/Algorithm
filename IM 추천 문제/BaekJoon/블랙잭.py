N,M = map(int,input().split())
data = list(map(int,input().split()))
A = len(data)
max_ = 0

for i in range(A):
    for j in range(i+1,A):
        for k in range(j+1,A):
            sum_ = data[i] + data[j] + data[k]

            if M >= sum_:
                if sum_ > max_:
                    max_ = sum_

print(max_)