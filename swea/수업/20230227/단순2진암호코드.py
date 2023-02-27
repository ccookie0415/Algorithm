import sys
sys.stdin = open('단순2진암호코드.txt','r')

T = int(input())


dic = {'0001101':'0','0011001':'1','0010011':'2','0111101':'3','0100011':'4','0110001':'5','0101111':'6','0111011':'7','0110111':'8','0001011':'9'}


for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    data = []
    lst = []
    key = []
    max_i = 0
    max_j = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                max_i = i
                max_j = j

    data = arr[max_i][max_j-55:max_j+1]

    for i in range(0,56,7):
        lst.append(data[i:i+7])

    for i in lst:
        if ''.join(i) in dic.keys():
            key.append(dic[''.join(i)])

    total_1 = 0     # 홀수자리 합
    total_2 = 0     # 짝수자리 합
    ans = 0         # 옳을 때, 각 자리수 합

    for i in range(8):
        ans += int(key[i])
        if i%2 == 0:
            total_1 += int(key[i])
        else:
            total_2 += int(key[i])


    if ((total_1 * 3) + total_2) % 10 == 0:
        ans = ans
    else:
        ans = 0

    print(f'#{tc} {ans}')




