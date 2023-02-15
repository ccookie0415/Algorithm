import sys
sys.stdin = open('forth.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    lst = (input().split())
    stack = []
    op = ["*", "+", '.', '-', '/']
    ans = 0


    for token in lst:
        if token == '.':
            break
        elif token not in op:
            stack.append(token)
        elif token in op:
            if len(stack) >= 2:
                if token == '+':
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num2 + num1)
                elif token == "*":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num2 * num1)
                elif token == '/':
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num2 // num1)
                elif token == '-':
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num2 - num1)
            else:
                ans = 'error'
                break

        if len(stack) == 1:
            ans = stack[0]
        else: ans = 'error'

    print(f'#{tc} {ans}')
