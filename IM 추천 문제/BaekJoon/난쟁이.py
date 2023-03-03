height_lst = []
subset = [[]]
arr = []
ans = []

for _ in range(9):
    height = int(input())
    height_lst.append(height)

for i in range(8,0,-1):
    for j in range(i):
        if height_lst[j] > height_lst[j+1]:
            height_lst[j],height_lst[j+1] = height_lst[j+1],height_lst[j]

for i in height_lst:
    L = len(subset)
    for l in range(L):
        subset.append(subset[l] + [i])

for i in subset:
    if len(i) == 7:
        arr.append(i)

for i in arr:
    sum = 0
    for j in range(0,7):
        sum += i[j]
    if sum == 100:
        ans = i

for i in ans:
    print(i)
