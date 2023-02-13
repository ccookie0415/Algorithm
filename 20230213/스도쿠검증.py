import sys
sys.stdin = open('스도쿠검증.txt', 'r')

# 9 * 9

T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    new_arr = list(zip(*arr))
    dic = {}
    ans = 1


    for i in range(1,10):
        dic[i] = 0

    idx = 0
    for j in range(9):
        if arr[idx][j] in dic.keys():
            dic[j+1] += 1
            if dic.values() == [1] * 9:
                idx += 1
        print(dic)

    for j in range(9):
        if new_arr[idx][j] in dic.keys():
            dic[j+1] += 1
            if dic.values() == [1] * 9:
                idx += 1
        print(dic)

    # i = 0,3,6 일때 검사하면 됨
    for k in range(0,7,3):



