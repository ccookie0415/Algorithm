import sys
sys.stdin = open('이진수의십진수.txt','r')

T = int(input())

for tc in range(1,T+1):
    data = list(map(int,input()))
    N = len(data)
    ans = []

    for i in range(0,N,7):
        total = 0
        for j in range(7):
            if j == 0:
                if data[i:i+7][::-1][j] == 1:
                    total += 1
            elif data[i:i+7][::-1][j] == 1:
                total += (2 ** j)
        ans.append(total)

    print(f'#{tc}', *ans)

