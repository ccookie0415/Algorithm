import sys
sys.stdin = open('파스칼의삼각형.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = []

    for i in range(1,N+1):
        lst = [1] * i
        data.append(lst)

    for i in range(N):
        for j in range(1,i):
            data[i][j] = data[i-1][j-1] + data[i-1][j]

    print(f'#{tc}')
    for i in range(N):
        print(*data[i])
