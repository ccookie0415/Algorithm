import sys
sys.stdin = open('영준이의카드카운팅.txt','r')

T = int(input())

for tc in range(1,T+1):
    data = list(map(str,input()))
    dic = {'S':0,'D':0,'H':0,'C':0}
    card_cnt = []
    cnt = 0
    ans = []

    for i in range(0,len(data),3):
        T = data[i]
        card_num = int(data[i+1]+data[i+2])
        cnt += 1

        if (T,card_num) not in card_cnt:
            card_cnt.append((T,card_num))
            dic[T] += 1

    if len(card_cnt) != cnt:
        print(f'#{tc}','ERROR')

    else:
        for value in dic.values():
            ans.append(13-value)
        print(f'#{tc}',*ans)


