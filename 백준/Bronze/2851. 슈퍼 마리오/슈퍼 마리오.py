import sys
input = sys.stdin.readline

arr = [0]
for _ in range(10):
    arr.append(int(input()))

prefix = [0] * 11

min_diff = float('inf')
for i in range(1, 11):
    prefix[i] = prefix[i-1] + arr[i]
    diff =  abs(100 - prefix[i])
    if diff <= min_diff:
        min_diff = diff
        ans = prefix[i]

print(ans)