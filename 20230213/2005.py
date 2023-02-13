import sys
sys.stdin = open('2005.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    stack = []


    print(f'#{tc}')
    for i in range(N):
        tmp = []
        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(stack[i-1][j] + stack[i-1][j-1])
        stack.append(tmp)

        print(*stack[i])
