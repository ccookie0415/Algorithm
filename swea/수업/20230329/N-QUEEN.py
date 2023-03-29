import sys
sys.stdin = open('N-QUEEN.txt','r')

def queen(n):
    global ans

    if n == N:
        ans += 1
        return

    for j in range(N):
        if visited_1[j] == 0 and visited_2[n+j] == 0 and visited_3[n-j] == 0:
            visited_1[j] = visited_2[n+j] = visited_3[n-j] = 1
            queen(n+1)
            visited_1[j] = visited_2[n+j] = visited_3[n-j] = 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ans = 0

    visited_1 = [0] * N
    visited_2 = [0] * (2*N)
    visited_3 = [0] * (2*N)

    queen(0)

    print(f'#{tc} {ans}')