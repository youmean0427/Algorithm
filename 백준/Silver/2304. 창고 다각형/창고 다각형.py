N = int(input())
arr = [0] * 1001
for tc in range(N):
    L, H = map(int, input().split())
    arr[L] = H

# print(arr)
count = 0
for i in range(1, len(arr)):
    if arr[i] <= arr[i-1]:
        arr[i] = arr[i-1]
    if arr[i] == max(arr):
        count += 1
        ii = i
        break

# print(count)
# print(count, ii)
for k in range(len(arr)-1, ii, -1):
    if arr[k] >= arr[k-1]:
        arr[k-1] = arr[k]
    if arr[k] == max(arr):
        for m in range(k, ii, -1):
            arr[m] = max(arr)
        break
# print(arr)
print(sum(arr))