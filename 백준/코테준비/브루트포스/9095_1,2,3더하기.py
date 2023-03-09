T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ans = [1,2,4]

    if N >=3:
        for i in range(3,N):
            ans.append(ans[i-3]+ans[i-2]+ans[i-1])

        print(ans[-1])

    else:
        print(ans[N-1])
