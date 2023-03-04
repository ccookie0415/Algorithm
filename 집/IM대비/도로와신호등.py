N,L = map(int,input().split())
road = [0] * (L+1)
data = []
current = 1
second = 0

for _ in range(N):
    a = list(map(int,input().split()))
    data.append(a)
    road[a[0]] = 3

while True:
    if road[L] == 1:
        break
    second += 1
    for i in range(len(data)):
        if second%(data[i][1]+data[i][2]) >= data[i][1]:
            road[data[i][0]] = 0
        else:
            road[data[i][0]] = 3
    if road[current] == 0:
        road[current] = 1
        current += 1
print(second)









