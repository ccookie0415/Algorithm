# ascending : 1부터 8까지
# descending : 8부터 1까지

lst = list(map(int,input().split()))
ans = ''
# check = 0
# cnt = 0
# ans = 'mixed'
#
# while True:
#     if check == 1:
#         print(ans)
#         break
#
#     if cnt == 7:
#         if lst[0] == 1:
#             print('ascending')
#             break
#         else:
#             print('descending')
#             break
#
#     if lst[0] == 1:
#         if lst[cnt + 1] == lst[cnt] + 1:
#             cnt += 1
#         else:
#             check = 1
#
#     if lst[0] == 8:
#         if lst[cnt + 1] == lst[cnt] - 1:
#             cnt += 1
#         else:
#             check = 1
#

if lst == [8,7,6,5,4,3,2,1]:
    ans = 'descending'

elif lst == [1,2,3,4,5,6,7,8]:
    ans = 'ascending'

else:
    ans = 'mixed'

print(ans)

