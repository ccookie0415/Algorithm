import sys
sys.stdin = open('이진수.txt','r')

T = int(input())
dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

for tc in range(1,T+1):
    N,data = map(str,input().split())
    N = int(N)
    ans = []

    for n in data:
        if n in dic.keys():
            n = dic[n]
        else:
            n = int(n)

        ans.append(f'{n:04b}')

    print(f'#{tc}',''.join(ans))
