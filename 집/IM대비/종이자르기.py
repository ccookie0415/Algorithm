width,height = map(int,input().split())
width_lst = [0]
height_lst = [0]
width_lst.append(width)
height_lst.append(height)

N = int(input())
max_width = 0
max_height = 0

for _ in range(N):
    cut_dir,cut_ = map(int,input().split())
    if cut_dir == 1:
        width_lst.append(cut_)
    else:
        height_lst.append(cut_)

for i in range(len(width_lst)-1,0,-1):
    for j in range(i):
        if width_lst[j] > width_lst[j+1]:
            width_lst[j],width_lst[j+1] = width_lst[j+1],width_lst[j]

for i in range(len(height_lst)-1,0,-1):
    for j in range(i):
        if height_lst[j] > height_lst[j+1]:
            height_lst[j],height_lst[j+1] = height_lst[j+1],height_lst[j]

for i in range(len(width_lst)-1):
    if (width_lst[i+1] - width_lst[i]) > max_width:
        max_width = width_lst[i+1] - width_lst[i]

for j in range(len(height_lst)-1):
    if (height_lst[j+1] - height_lst[j]) > max_height:
        max_height = height_lst[j+1] - height_lst[j]

print(max_width*max_height)


