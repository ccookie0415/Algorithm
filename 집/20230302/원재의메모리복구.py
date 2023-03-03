# import sys
# sys.stdin = open('원재의메모리복구.txt','r')

T = int(input())

for tc in range(1,T+1):
    data = list(map(int,input()))
    stack = []
    cnt = 0

    for i in range(len(data)):
        if data[i] == 1:
            first_one = i
            break

    data = data[first_one:]

    for i in data:
        if not stack:
            stack.append(i)
            cnt += 1
        else:
            if i == 1 and stack[-1] == 0:
                stack.pop()
                stack.append(i)
                cnt += 1
            elif i == 0 and stack[-1] == 1:
                stack.pop()
                stack.append(i)
                cnt += 1

    print(f'#{tc} {cnt}')
