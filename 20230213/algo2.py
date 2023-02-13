import sys
sys.stdin = open('algo2_sample_in.txt', 'r')

# 1<= N <= 10
# 1<= K <= 20
# 0 <= A,B < 10
# N번 내민다
# 두더지를 때리면 1점 획득
# K초 동안 머무른 뒤 다시 게임판 아래로 들어감


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    r, c = map(int,input().split())

    score = 0
    for i in range(N):
        A,B,K = map(int,input().split())


    for _ in range(K):
        if c != B  :
            if B > c:
                c += 1
            elif B < c:
                c -= 1

        elif c == B :
            if A == B:
                score += 1
            elif A > r:
                r += 1
            elif A > r:
                r -= 1


    print(f'#{tc} {score}')