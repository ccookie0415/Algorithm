N,X = map(int,input().split())
lst = list(map(int,input().split()))
ans_lst = list()

for i in range(N):
    if lst[i] < X:
        ans_lst.append(lst[i])

print(*(ans_lst))