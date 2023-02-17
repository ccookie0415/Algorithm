import sys
sys.stdin = open('원재의bit.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    data = list(input())
    stack = []
    cnt = 0

    for token in data:
        if not stack and token == '1':
            stack.append(token)
            cnt += 1
        elif not stack and token == '0':
            stack.append(token)
        elif stack:
            if stack and stack[-1] == '1':
                if token == '0':
                    stack.pop()
                    stack.append(token)
                    cnt += 1
                elif token == '1':
                    pass
            elif stack and stack[-1] == '0':
                if token == '1':
                    stack.pop()
                    stack.append(token)
                    cnt += 1
                elif token == '0':
                    pass

    print(f'#{tc} {cnt}')

