N = int(input())
data = list(input())
cnt = 1
check = 0
A = len(data)
ans = 0

for i in range(N):
    if data[i] == 'S':
        cnt += 1
    if data[i] == 'L':
        if check == 0:
            check = 1
        elif check == 1:
            check = 0
            cnt += 1

if A < cnt:
    ans = A
else:
    ans = cnt

print(ans)