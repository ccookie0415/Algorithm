import sys
sys.stdin = open('비밀번호.txt', 'r')

T = 10

for tc in range(1,T+1):
    N, data = input().split()
    stack = []


    for i in data:
        if stack and stack[-1] == i:
                stack.pop()
        else:
            stack.append(i)


    ans = ''.join(stack)
    print(f'#{tc} {ans}')