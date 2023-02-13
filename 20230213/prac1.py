T = int(input())
for t in range(T):
    Data = input()
    stack = []
    result = 0
    for i in range(len(Data)):
        if Data[i] == "(" or Data[i] == "{":  # 여는괄호가 올 경우 stack에 push
            stack.append(Data[i])
        elif Data[i] == ")" or Data[i] == "}":  # 닫는괄호 이며 stack이 빈 경우
            if len(stack) == 0:  # 처음부터 닫는 괄호가 오는 경우 (스택이 빈 경우)
                stack = [Data[i]]
                break  # 입력된 괄호와 stack의 top에 있는 괄호와 일치하지 않는 경우
            elif (Data[i] == "}" and stack[-1] != "{") or (Data[i] == ")" and stack[-1] != "("):
                stack = [Data[i]]
                break
            else:  # stack에 저장된 괄호와 일치하는 닫는 괄호가 오는 경우
                stack.pop()

    if len(stack) == 0:
        result = 1
    else:
        result = 0
    print("#{} {}".format(i + 1, result))