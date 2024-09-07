import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

negative = []
positive = []

for i in arr:
    if i < 0:
        negative.append(-i)
    else:
        positive.append(i)

def radix_sort(arr, n):
    # Radix Sort
    k = 7
    p = 1
    for i in range(k):
        nums = [[] for _ in range(10)]

        for j in range(n):
            x = (arr[j] // p) % 10
            nums[x].append(arr[j])

        sorted_arr = []
        for a in range(9, -1, -1):
            for b in range(len(nums[a])):
                sorted_arr.append(nums[a][b])

        p *= 10
        arr = sorted_arr

    return arr

negative = radix_sort(negative, len(negative))
positive = radix_sort(positive, len(positive))

for i in positive:
    print(i)
for i in negative[::-1]:
    print(-i)