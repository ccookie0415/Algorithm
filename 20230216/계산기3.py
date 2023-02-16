import sys
sys.stdin = open('계산기3.txt', 'r')

T = 10


for tc in range(1,T+1):
    N = int(input())
    lst = list(input())
    isp = {'(': 0, '*' : 2, '/' : 2, '+' : 1, '-' : 1}
    icp = {'(': 3, '*' : 2, '/' : 2, '+' : 1, '-' : 1}
    stack = []
    ans = []

    for token in lst:
        if token in isp.keys():
            if not stack:
                stack.append(token)
            elif stack:
                if icp[token] > isp[stack[-1]]:
                    stack.append(token)
                elif icp[token] <= isp[stack[-1]]:
                    while True:
                        ans.append(stack.pop())
                        if icp[token] > isp[stack[-1]]:
                            stack.append(token)
                            break
        elif token == ')':
            while True:
                ans.append(stack.pop())
                if icp[stack[-1]] == 3:
                    ans.append(stack.pop())
                    ans.append(token)
                    ans.remove('(')
                    ans.remove(')')
                    break
        else:
            ans.append(token)

    while stack:
        ans.append(stack.pop())


    for token in ans:
        if token not in isp.keys():
            stack.append(token)
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if token == '*' : stack.append(num1 * num2)
            elif token == '/': stack.append(num1 // num2)
            elif token == '+': stack.append(num1 + num2)
            elif token == '-': stack.append(num1 - num2)

    print(f'#{tc} {stack[0]}')

