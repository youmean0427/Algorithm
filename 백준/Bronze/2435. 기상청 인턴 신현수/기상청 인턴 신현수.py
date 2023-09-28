import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(x) for x in input().split()]
result = []
for i in range(N-K+1):

    start = i
    temp = 0
    cnt = 0
    while cnt < K:
        temp += arr[start + cnt]
        cnt += 1

    result.append(temp)

print(max(result))
