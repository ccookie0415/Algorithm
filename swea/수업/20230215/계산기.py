import sys
sys.stdin = open('계산기.txt', 'r')

T = 10

for tc in range(1,T+1):
    N = int(input())
    lst = list(input())
    stack = []
    ans = []

    for token in lst:
        if token == '+':
            if not stack:
                stack.append(token)
            elif stack:
                ans.append(token)
        else:
            ans.append(token)

    while stack:
        ans.append(stack.pop())


    for token in ans:
        if not stack:
            stack.append(token)
        else:
            if token == '+':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 + num2)
            else:
                stack.append(token)


    print(f'#{tc} {stack[0]}')

