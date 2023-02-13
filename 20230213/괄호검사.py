import sys
sys.stdin = open('괄호검사.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    Data = input()
    stack = []
    result = 0

    for i in range(len(Data)):
        if Data[i] == "(" or Data[i] == "{":
            stack.append(Data[i])
        elif Data[i] == ")" or Data[i] == "}":
            if len(stack) == 0:
                stack = [Data[i]]
                break
            elif ((Data[i] == ")" and stack[-1] != "(") or ((Data[i] == "}") and stack[-1] != "{")):
                stack = [Data[i]]
                break
            else:
                stack.pop()


    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
