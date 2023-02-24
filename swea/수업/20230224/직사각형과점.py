import sys
sys.stdin = open('직사각형과점.txt','r')

T = int(input())

for tc in range(1,T+1):
    x1,y1,x2,y2 = map(int,input().split())
    arr = [[0]*(x2-x1) for _ in range(y2-y1)]
    lst = []
    ans = []

    for i in range(y1+1,y2):            # 내부 점
        for j in range(x1+1,x2):
            lst.append(i)
            lst.append(j)

    N = int(input())
    dot_in = 0
    dot_ = 0
    dot_out = 0
    for _ in range(N):
        x,y = map(int,input().split())
        if x1 <= x <= x2 and y1 <= y <= y2:
            if x == x1 or x == x2 or y == y1 or y == y2:
                dot_ += 1
            else:
                dot_in += 1
        else:
            dot_out += 1


    ans.append(dot_in)
    ans.append(dot_)
    ans.append(dot_out)

    print(f'#{tc}', *ans)


