N,M = map(int,input().split())
N_lst = []
M_lst = []
max_common = 0

for i in range(1,N+1):
    if N % i == 0:
        N_lst.append(i)

for j in range(1,M+1):
    if M % j == 0:
        if j in N_lst:
            if j > max_common:
                max_common = j

tmp1 = M // max_common
tmp2 = N // max_common

print(max_common)
print(max_common*tmp1*tmp2)