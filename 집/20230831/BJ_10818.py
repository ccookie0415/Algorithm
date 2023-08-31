N = int(input())
lst = list(map(int,input().split()))

# for i in range(N-1, 0, -1):
#     for j in range(0,i):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#
# min_ = lst[0]
# max_ = lst[-1]
#
# print(min_,max_)
min_ = 1000001
max_ = -1000001

for i in range(N):
    if lst[i] < min_:
        min_ = lst[i]
    if lst[i] > max_:
        max_ = lst[i]

print(min_, max_)




