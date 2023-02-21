import sys
sys.stdin = open('반복문자지우기.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    Data = input()
    stack = []

    for i in Data:
        if len(stack) == 0:
            stack.append(i)
        elif len(stack) != 0:
            if i == stack[-1]:
                stack.pop()
            elif i != stack[-1]:
                stack.append(i)

    print(f'#{tc} {len(stack)}')