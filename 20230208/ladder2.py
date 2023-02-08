import sys
sys.stdin = open('input_ladder2.txt', 'r')

T = 10
for tc in range(1, T+1):
    tc_num = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

# start = [0][col] == 1
# end = [row][0] == 1
    for row in range(100):
        for col in range(100):
            if arr[row][99] == 1:
                print(row)



    #     if arr[0][col] == 1:
    #         print(col)
    #         # elif



