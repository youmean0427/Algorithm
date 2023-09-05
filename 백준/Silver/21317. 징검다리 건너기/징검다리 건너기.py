import sys
input = sys.stdin.readline

N = int(input())
arr = []
dp = [float('inf')] * (N+1)
for i in range(N-1):
    a, b = map(int, input().split())
    arr.append((a, b))

if N == 1:
    print(0)
else:
    K = int(input())
    dp[2] = arr[0][0]
    dp[1] = 0
    result = []
    
    # 작은 점프, 큰 점프를 하는 경우
    for i in range(3, N+1):
        dp[i] = min(dp[i-1] + arr[i-2][0], dp[i-2] + arr[i-3][1])

    result.append(dp[-1])

    # 각각의 돌에서 매우 큰 점프를 하는 경우
    for k in range(4, N+1):
        dp2 = [float('inf')] * (N + 1)
        dp2[:k] = dp[:k]

        dp2[k] = dp2[k - 3] + K
        dp2[1] = 0

        for j in range(k, N+1):
            dp2[j] = min(dp2[j], dp2[j - 1] + arr[j - 2][0], dp2[j - 2] + arr[j - 3][1])

        result.append(dp2[-1])

    print(min(result))