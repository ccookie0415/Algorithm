# 가장 첫 줄에는 테스트 케이스의 개수 T
# 그 아래로 테스트 케이스 주어짐
# #t로 시작하고, 공백한칸 둔 다음 정답 출력

import sys
sys.stdin = open('input.txt', 'r')

Test_case = int(input())

for t in range(Test_case):
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]


    str_num = (' '.join(list(map(str, num))))

    print(f'#{t+1} {str_num}')
