lst = list(map(int,input().split()))
N = len(lst)

while True:
    if lst == [1,2,3,4,5]:
        break
    else:
        for j in range(N-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                print(*lst)