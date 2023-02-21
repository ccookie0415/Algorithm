import sys
sys.stdin = open('input_글자수.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    str1 = list(input())
    str2 = list(input())
    N = len(str1)
    M = len(str2)

    dic = {}
    for i in range(N):
        dic[str1[i]] = 0

    for j in str2:
        if j in dic.keys():
            dic[j] += 1

    lst = []

    for value in dic.values():
        lst.append(value)

    A = len(lst)

    for i in range(A-1, 0, -1):
        for j in range(0,i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]

    print(f'#{tc} {lst[-1]}')




