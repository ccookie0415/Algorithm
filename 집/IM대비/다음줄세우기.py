T = int(input())

for tc in range(1,T+1):
    data = list(map(int,input().split()))
    data = data[1:]
    cnt = 0

    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[j+1] < data[j]:
                data[j],data[j+1] = data[j+1],data[j]
                cnt += 1

    print(tc,cnt)