
arr = [int(x) for x in input().split()]

def insert_sort(arr):

    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

result = insert_sort(arr)
print(*result)