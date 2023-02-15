import sys
sys.stdin = open('후위표기법변환.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    lst = list(input())
    stack = []
    ans = []
    op = ["*",  "+"]


    for token in lst:
        if token in op:
            if not stack:
                stack.append(token)
            elif stack and token == '+':
                while stack:
                    ans.append(stack.pop())
                else:
                    stack.append(token)
            elif stack and token == '*':
                if stack[-1] == '+':
                    stack.append(token)
                else:
                    ans.append(token)

        else:
            ans.append(token)

    while stack:
        ans.append(stack.pop())

    ans = ''.join(ans)
    print(f'#{tc} {ans}')