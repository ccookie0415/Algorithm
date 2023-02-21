# '1'은 스위치가 켜져 있음, '0'은 스위치가 꺼져 있음
# 남학생 1 : 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꿈
# 여학생 2 : 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로
#         좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서 그 구간에 속한 스위치의 상태를 모두 바꾼다.
#         이 때 구간에 속한 스위치 개수는 항상 홀수

N = int(input())                # 스위치 개수
lst = list(map(int,input().split()))        # 스위치 상태
A = int(input())                # 학생 수

for _ in range(A):
    gender, on_off = map(int,input().split())

    print(lst)

    if gender == 1:
        for i in range(0,N):
            if i % on_off == 0:
                if lst[i] == 0:
                    lst[i] = 1
                else:
                    lst[i] = 0

    print(lst)
    # else:
    #     for i in range(0,N):


