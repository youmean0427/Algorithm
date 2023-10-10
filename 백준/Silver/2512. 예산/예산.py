import sys
input = sys.stdin.readline

N = int(input())
arr = [int(x) for x in input().split()]
M = int(input())

start = 0
end = max(arr)
result = 0

while start <= end:
    sum_arr = 0
    mid = (start + end) // 2
    for i in arr:
        if i < mid:
            sum_arr += i

        else:
            sum_arr += mid

    if sum_arr > M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)