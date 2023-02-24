M,N = map(int,input().split())      #M 가로   #N 세로
cnt_0 = [0,N]
cnt_1 = [0,M]
max_0 = 0
max_1 = 0
A = int(input())

for _ in range(A):
    type,cut = map(int,input().split())

    if type == 0:
        cnt_0.append(cut)
    if type == 1:
        cnt_1.append(cut)

cnt_0.sort()
cnt_1.sort()

for i in range(len(cnt_0)-1):
    if cnt_0[i+1] - cnt_0[i] > max_0:
        max_0 = cnt_0[i+1] - cnt_0[i]
for i in range(len(cnt_1)-1):
    if cnt_1[i+1] - cnt_1[i] > max_1:
        max_1 = cnt_1[i+1] - cnt_1[i]

print(max_0 * max_1)


