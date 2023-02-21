import sys
sys.stdin = open('input_1221.txt', 'r')

dic = {}
a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for i in range(len(a)):
    dic[a[i]] = i

T = int(input())

for tc in range(1, T + 1):
    tc_num, N = input().split()
    cnt_lst = [0] * 10
    num_lst = list(input().split())

    for i in range(int(N)):
        cnt_lst[dic[num_lst[i]]] += 1

    ans = []
    for j in range(10):
        for i in range(cnt_lst[j]):
            ans.append(a[j])

    result = ' '.join(list(map(str, ans)))
    print(tc_num)
    print(result)

