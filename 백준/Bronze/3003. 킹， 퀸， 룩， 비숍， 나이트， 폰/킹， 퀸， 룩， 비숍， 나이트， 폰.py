import sys
input = sys.stdin.readline

arr = [int(x) for x in input().split()]
check = [1, 1, 2, 2, 2, 8]
result = [0] * 6

for i in range(6):
    if arr[i] < check[i] or arr[i] > check[i]:
        result[i] = check[i] - arr[i]

print(*result)
