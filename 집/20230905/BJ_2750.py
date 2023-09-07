N = int(input())
lst = list()

for i in range(N):
    lst.append(int(input()))

lst.sort()

for j in range(N):
    print(lst[j])

