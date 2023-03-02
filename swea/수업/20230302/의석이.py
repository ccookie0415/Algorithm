import sys
sys.stdin = open('의석이의세로로.txt','r')

T = int(input())

for tc in range(1,T+1):
    data = [list(map(str,input())) for _ in range(5)]
    ans = []

    for j in range(15):
        for i in range(5):
            try:
                ans.append(data[i][j])
            except:
                continue

    ans = ''.join(ans)

    print(f'#{tc}',ans)