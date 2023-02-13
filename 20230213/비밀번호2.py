Test_case = 10

for t in range(Test_case):
    N, string = input().split()
    stack = []
    for s in string:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    result = ''.join(list(map(str, stack)))
    print(f'#{t + 1} {result}')