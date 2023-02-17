import sys
sys.stdin = open('쇠막대기자르기.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    data = input()
    stack = []
    cnt = 0

    for i in range(len(data)):
        if data[i] == "(":
            stack.append(data[i])
        else:
            if data[i-1] == "(":
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1
    print(f'#{tc} {cnt}')