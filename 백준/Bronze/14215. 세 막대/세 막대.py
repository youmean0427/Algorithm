import sys
input = sys.stdin.readline

arr = [int(x) for x in input().split()]
arr.sort()

val = arr[0] + arr[1]
if arr[0] + arr[1] <= arr[-1]:
    print(val + val - 1)
else:
    print(sum(arr))