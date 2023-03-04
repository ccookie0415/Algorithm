sum_ = 0
height_lst = []
except_ = []

for _ in range(9):
    a = int(input())
    height_lst.append(a)

for i in height_lst:
    sum_ += i

for i in range(9):
    for j in range(i+1,9):
        if sum_ - (height_lst[i] + height_lst[j]) == 100:
            a = height_lst[i]
            b = height_lst[j]
            break

height_lst.remove(a)
height_lst.remove(b)
height_lst.sort()

for i in height_lst:
    print(i)


