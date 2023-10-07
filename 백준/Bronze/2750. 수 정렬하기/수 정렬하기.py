import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

# 병합 정렬
def merge_sort(arr):

    N = len(arr)
    if N == 1:
        return arr

    mid = N // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    i1 = 0
    i2 = 0
    merged_arr = []

    while i1 < len(left) and i2 < len(right):
        if left[i1] < right[i2]:
            merged_arr.append(left[i1])
            i1 += 1
        else:
            merged_arr.append(right[i2])
            i2 += 1

    merged_arr += left[i1:]
    merged_arr += right[i2:]

    return merged_arr

result = merge_sort(arr)
for i in result:
    print(i)
