from itertools import combinations

n,k = map(int,input().split())
combination = combinations(range(n),k)

result = 0

for i in combination:
    result += 1

print(result)
