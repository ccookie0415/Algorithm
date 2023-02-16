import sys
sys.stdin = open('토너먼트카드게임.txt', 'r')

def solve(s,e):
    # 종료조건 : 더 이상 승부를 보지 않는 인원 1명
    if s == e:
        return s

    a = solve(s, (s+e)//2)
    b = solve((s+e)//2+1,e)

    if (lst[a]%3)+1 == lst[b]:
        return b
    return a

T = int(input())

for tc in range(1,T+1):
    N = int(input())                        # 인원수
    lst = [0]+list(map(int,input().split()))

    ans = solve(1,N)
    print(f'#{tc} {ans}')
