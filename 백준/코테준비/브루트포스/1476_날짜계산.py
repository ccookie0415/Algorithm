lst = list(map(int,input().split()))

while True:
    if lst[0]==lst[1]==lst[2]:
        break
    else:
        min_idx = 0
        min_ = 999999
        for i in range(3):
            if lst[i] < min_:
                min_ = lst[i]
                min_idx = i
        if min_idx == 0:
            lst[0] = lst[0] + 15
        elif min_idx == 1:
            lst[1] = lst[1] + 28
        elif min_idx == 2:
            lst[2] = lst[2] + 19

print(lst[0])


