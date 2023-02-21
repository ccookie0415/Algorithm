import sys
sys.stdin = open('input_정렬연습.txt', 'r')

T = int(input())


# 버블정렬

# for tc in range(1,T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#
#     for i in range(N-1):
#         for j in range(N-1-i):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#
#     print(nums)

# # 카운팅정렬
# for tc in range(1,T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     count = [0] * (max(nums)+1)
#
#     for num in nums:
#         count[num] += 1
#
#     for i in range(1,len(count)):
#         count[i] += count[i-1]
#
#     result = [0] * (len(nums))
#
#     for num in nums:
#         idx = count[num]
#         result[idx-1] = num
#         count[num] -= 1
#
#     print(result)

# 카운팅정렬 2

# for tc in range(1,T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     count = [0] * (max(nums)+1)
#
#     for a in nums:
#         count[a] += 1
#
#     print(count)
#
#     i = 0
#     for b in range(max(nums)+1):
#         for _ in range(count[b]):
#             nums[i] = b
#             i += 1
#
#     print(nums)

for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_ = max(nums)+1

    dic = {}
    for i in range(max_):
        dic[i] = 0

    for i in nums:
        dic[i] += 1

    for key,value in dic.items():
        for i in range(value):
            print(key)
