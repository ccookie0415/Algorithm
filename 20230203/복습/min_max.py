import sys
sys.stdin = open('input_minmax.txt', 'r')

T = int(input())

for tc in range(T):
    N= int(input())
    nums = list(map(int,input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0,i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

        answer = nums[-1] - nums[0]


    print(f'#{tc+1} {answer}')