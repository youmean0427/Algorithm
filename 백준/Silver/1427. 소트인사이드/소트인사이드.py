import sys
input = sys.stdin.readline

N = input().rstrip()
arr = []

for i in N:
    arr.append(int(i))

def quick_sort(arr, start, end):

    if start < end:
        pivot = arr[start]
        first = start
        last = end

        while start <= end:

            # pivot보다 큰 수 찾기
            while start <= end and arr[start] <= pivot:
                start += 1
            # pivot보다 작은 수 찾기
            while start <= end and arr[end] >= pivot:
                end -= 1

            if start < end:
                arr[start], arr[end] = arr[end], arr[start]

        arr[first], arr[end] = arr[end], arr[first]

        quick_sort(arr, first, end - 1)
        quick_sort(arr, end + 1, last)

        return arr[::-1]
    return arr

arr = quick_sort(arr, 0, len(arr)-1)

result = ''
for i in arr:
    result += str(i)
print(result)