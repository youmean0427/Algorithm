import sys
input = sys.stdin.readline

N = int(input())
arr = [int(x) for x in input().split()]
result = [0] * N
for i in range(len(arr)):

    if i == 0:
        result[arr[i]] = 1

    else:
        x = arr[i]
        while result[x]:
            x += 1

        while result[:x].count(0) < arr[i]:
            x += 1

        while result[x]:
            x += 1
        result[x] = i + 1

print(*result)