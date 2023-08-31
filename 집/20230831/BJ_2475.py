# 00000~99999
# 검증수 : 각각의 자리수들을 제곱한 후 더하고 10으로 나눈 수

lst = list(input().split())
ans = 0

for i in range(5):
    num = int(lst[i])
    ans += num * num

ans = ans % 10
print(ans)
