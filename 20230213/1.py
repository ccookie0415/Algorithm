import sys
sys.stdin = open('알고리즘.txt' , 'r')

T = int(input())

for tc in range(1, T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans_lst = [0] * N

for i in range(N):
    ans = 0
    for j in range(i, i+K):
        if j <= N-1:
            ans += arr[i][j]
            ans_lst[i] = ans
# print(ans_lst)

for i in range(N-1,0,-1):
    for j in range(i):
        if ans_lst[j] > ans_lst[j+1]:
            ans_lst[j],ans_lst[j+1] = ans_lst[j+1],ans_lst[j]

# print(ans_lst)
result = ans_lst[-1]
print(f'#{tc} {result}')