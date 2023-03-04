N = int(input())
lst = [0] * (N+1)
data = [0]+list(map(int,input().split()))

for i in range(1,N+1):
    lst[i] = i
    a = i
    for _ in range(data[i]):
        lst[a-1],lst[a] = lst[a],lst[a-1]
        a -= 1

print(*lst[1:])