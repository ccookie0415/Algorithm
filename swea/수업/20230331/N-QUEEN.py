import sys
sys.stdin = open('N-QUEEN.txt','r')

def find(n):
    global ans

    if n == N:
        ans += 1

    for j in range(N):
        if visited_j[j] == visited_r[n + j] == visited_l[n - j] == 0:
            visited_j[j] = visited_r[n + j] = visited_l[n - j] = 1
            find(n+1)
            visited_j[j] = visited_r[n + j] = visited_l[n - j] = 0


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ans = 0
    visited_j = [0] * N
    visited_r = [0] * 2*N
    visited_l = [0] * 2*N

    find(0)
    print(f'#{tc} {ans}')